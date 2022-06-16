import argparse
from pyex import VERSION
from pyex.reader import Reader
from pyex.writer import JSONWriter
from argparse import RawTextHelpFormatter
import logging
import sys

LOGGER = logging.getLogger("pyex")
LOGGING_HANDLER = logging.StreamHandler(sys.stdout)
LOGGING_HANDLER.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] - %(message)s'))
LOGGER.addHandler(LOGGING_HANDLER)

def introduction():
    text = ""
    text+=""" ___   _     ____  _    
| |_) \ \_/ | |_  \ \_/ 
|_|    |_|  |_|__ /_/ \ \n"""
    text+="Excel to JSON converter.\n"
    text+="Author: buivd4@hotmail.com\n"
    text+=f"Version: {VERSION}\n"
    return text

def run():
    parser = argparse.ArgumentParser(description=introduction(),formatter_class=RawTextHelpFormatter)
    parser.add_argument("--input","-i", type=str, help="Input file path. Must be excel (xlsx) file.")
    parser.add_argument("--output","-o", type=str, help="Output file. Should be .json extension.")    
    parser.add_argument("--exclude","-e", type=str, default=None, help="Exclude sheet by name if match pattern.")
    parser.add_argument("--ffill", type=str, default="", help="FFill columns. Format: [0-9]+,[0-9]+,..,[0-9]+")
    parser.add_argument("--default", type=str, default="undefined", help="Default value for missing data")    
    parser.add_argument("--verbose", "-v", action="store_true", help="Run with verbose mode")
    args = parser.parse_args()
    
    if args.verbose:
        LOGGER.setLevel(logging.DEBUG)
    else:
        LOGGER.setLevel(logging.INFO)

    ffill= [int(i.strip()) for i in args.ffill.split(",")] if args.ffill else []
    reader = Reader(args.input)
    writer = JSONWriter(args.output)
    writer.write(reader.read(exclude = args.exclude,default=args.default, ffill=ffill))

if __name__ == "__main__":
    run()