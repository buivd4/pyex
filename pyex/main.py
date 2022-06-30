import argparse
import logging
import os
import sys
from argparse import RawTextHelpFormatter
import datetime
import waitress
from multiprocessing import Process
import json


from pyex import VERSION
from pyex.api.app import create_app
from pyex.converter import *
from pyex.processor_chain import ProcessorChain
from pyex.utils import *

LOGGER = logging.getLogger("pyex")
LOGGING_HANDLER = logging.StreamHandler(sys.stdout)
LOGGING_HANDLER.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] - %(message)s'))
LOGGER.addHandler(LOGGING_HANDLER)


def introduction():
    text = ""
    text += """ ___   _     ____  _    
| |_) \ \_/ | |_  \ \_/ 
|_|    |_|  |_|__ /_/ \ \n"""
    text += "Excel to JSON converter.\n"
    text += "Author: buivd4@hotmail.com\n"
    text += f"Version: {VERSION}\n"
    return text


def run():
    parser = argparse.ArgumentParser(description=introduction(), formatter_class=RawTextHelpFormatter)
    parser.add_argument("--serve", "-s", action="store_true", help="Run pyex API service")
    parser.add_argument("--host", type=str, default=os.environ.get("PYEX_HOST", "localhost"),
                        help="specify host of API service")
    parser.add_argument("--port", type=int, default=int(os.environ.get("PYEX_PORT", 5000)),
                        help="specify port of API service")
    parser.add_argument("--input", "-iF", type=str, help="input file path. Must be excel (xlsx) file.")
    parser.add_argument("--output", "-oF", type=str, help="output file. Should be .json extension.")
    parser.add_argument("--input-directory", "-iD", type=str, help="input directory.")
    parser.add_argument("--output-directory", "-oD", type=str, help="output directory.")
    parser.add_argument("--max-concurrent",  type=int, help="max concurrent processor.")    
    parser.add_argument("--one-file", action="store_true", help="output should be 1 file.")    
    parser.add_argument("--exclude", "-e", type=str, default=os.environ.get("PYEX_EXCLUDE"),
                        help="exclude sheet by name if match pattern.")
    parser.add_argument("--ffill", type=str, default=os.environ.get("PYEX_FFILL", ""),
                        help="ffill columns. Format: [0-9]+,[0-9]+,..,[0-9]+")
    parser.add_argument("--default", type=str, default=os.environ.get("PYEX_DEFAULT", "undefined"),
                        help="default value for missing data")
    parser.add_argument("--flatten", default=os.environ.get("PYEX_FLATTEN", "false")=="true", action="store_true",
                        help="write output in flatten json format")
    parser.add_argument("--processors", type=str, nargs='*',
                        help="processor classes")
    parser.add_argument("--verbose", "-v", action="store_true", help="run with verbose mode")
    args = parser.parse_args()

    LOGGER.info(f"Run pyex with arguments: ffills={args.ffill}, exclude={args.exclude}, default={args.default}")

    ffill_list = [int(i.strip()) for i in args.ffill.split(",")] if args.ffill else []
    configurations = {
        "exclude": args.exclude,
        "default": args.default,
        "ffill": ffill_list,
        "flatten": args.flatten
    }
    verbose = args.verbose or os.environ.get("PYEX_VERBOSE", "false") == "true"
    print(f"Verbose mode: {verbose}")
    if verbose:
        LOGGER.setLevel(logging.DEBUG)
    else:
        LOGGER.setLevel(logging.INFO)    
    processor_chain = ProcessorChain()
    if args.processors:
        for processor in args.processors:
            processor_chain.register(processor)
            LOGGER.info(f"Processor loaded: {processor}")

    if args.serve:
        app = create_app(configurations)
        if verbose:
            app.run(host=args.host, port=args.port)
        else:
            waitress.serve(app, host=args.host, port=args.port)
    elif args.input_directory:
        if not args.output_directory:
            LOGGER.error("Missing argument: output_directory")
            exit()
        if not os.path.exists(args.output_directory):
            os.mkdir(args.output_directory)
        process_list = []
        start_time = datetime.datetime.now()
        for fp in os.listdir(args.input_directory):
            if is_file_of_extension(fp, "xlsx"):
                converter = Converter(fin = os.path.join(args.input_directory, fp) ,fout = os.path.join(args.output_directory, change_extension(fp, "json")), processor_chain=processor_chain, configurations = configurations)
                p = Process(name=fp,target=converter.convert)
                process_list.append(p)
                p.start()
                LOGGER.info(f"Folk new process for {fp}")
        for p in process_list:
            p.join()
        end_time = datetime.datetime.now()
        LOGGER.info(f"Processed {len(process_list)} files in {(end_time-start_time).seconds} second(s)")
        if args.one_file:
            if not args.output:
                LOGGER.error("Must provide output file when --one-file flag is on")
            output = []
            target_files = [fp for fp in os.listdir(args.output_directory) if is_file_of_extension(fp, "json")]
            for i in range(0, len(target_files), args.max_concurrent):
                for fp in target_files[i:i+args.max_concurrent]:
                    with open(os.path.join(args.output_directory, fp), "r") as f:              
                        output.extend(json.load(f))
                os.remove(os.path.join(args.output_directory, fp))
            with open(args.output,"w+") as fout:
                json.dump(output, fout, indent=4)
    else:
        start_time = datetime.datetime.now()
        converter = Converter(fin = args.input, fout= args.output ,processor_chain=processor_chain,configurations=configurations)
        converter.run()
        end_time = datetime.datetime.now()
        LOGGER.info(f"Processed file in {(end_time-start_time).seconds} second(s)")

if __name__ == "__main__":
    run()
