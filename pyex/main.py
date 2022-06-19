import argparse
import logging
import os
import sys
from argparse import RawTextHelpFormatter

import waitress

from pyex import VERSION
from pyex.api.app import create_app
from pyex.reader import Reader
from pyex.writer import JSONWriter

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
                        help="Specify host of API service")
    parser.add_argument("--port", type=int, default=int(os.environ.get("PYEX_PORT", 5000)),
                        help="Specify port of API service")
    parser.add_argument("--input", "-i", type=str, help="Input file path. Must be excel (xlsx) file.")
    parser.add_argument("--output", "-o", type=str, help="Output file. Should be .json extension.")
    parser.add_argument("--exclude", "-e", type=str, default=os.environ.get("PYEX_EXCLUDE"),
                        help="Exclude sheet by name if match pattern.")
    parser.add_argument("--ffill", type=str, default=os.environ.get("PYEX_FFILL", ""),
                        help="FFill columns. Format: [0-9]+,[0-9]+,..,[0-9]+")
    parser.add_argument("--default", type=str, default=os.environ.get("PYEX_DEFAULT", "undefined"),
                        help="Default value for missing data")
    parser.add_argument("--verbose", "-v", action="store_true", help="Run with verbose mode")
    args = parser.parse_args()

    LOGGER.info(f"Run pyex with arguments: ffills={args.ffill}, exclude={args.exclude}, default={args.default}")

    ffill_list = [int(i.strip()) for i in args.ffill.split(",")] if args.ffill else []
    configurations = {
        "exclude": args.exclude,
        "default": args.default,
        "ffill": ffill_list
    }
    verbose = args.verbose or os.environ.get("PYEX_VERBOSE", "false") == "true"
    if args.serve:
        app = create_app(configurations)
        if verbose:
            app.run(host=args.host, port=args.port)
        else:
            waitress.serve(app, host=args.host, port=args.port)
    else:
        if verbose:
            LOGGER.setLevel(logging.DEBUG)
        else:
            LOGGER.setLevel(logging.INFO)
        reader = Reader(args.input)
        writer = JSONWriter(args.output)
        writer.write(reader.read(**configurations))


if __name__ == "__main__":
    run()
