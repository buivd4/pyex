# pyex
Excel to JSON converter


## Install
```shell
./pyex> python3 -m pip install .
```

## Usage
```shell
$ pyex -h
usage: pyex [-h] [--input INPUT] [--output OUTPUT] [--exclude EXCLUDE] [--ffill FFILL] [--default DEFAULT] [--verbose]

 ___   _     ____  _
| |_) \ \_/ | |_  \ \_/
|_|    |_|  |_|__ /_/ \
Excel to JSON converter.
Author: buivd4@hotmail.com
Version: 0.0.1

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        Input file path. Must be excel (xlsx) file.
  --output OUTPUT, -o OUTPUT
                        Output file. Should be .json extension.
  --exclude EXCLUDE, -e EXCLUDE
                        Exclude sheet by name if match pattern.
  --ffill FFILL         FFill columns. Format: [0-9]+,[0-9]+,..,[0-9]+
  --default DEFAULT     Default value for missing data
  --verbose, -v         Run with verbose mode
```