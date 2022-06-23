# pyex

Excel to JSON converter.

Version: 0.0.1 <br>
License: <a href="http://www.apache.org/licenses/LICENSE-2.0.html">Apache 2.0</a>

Author: buivd4@hotmail.com

## Install

```shell
./pyex> python3 -m pip install .
```

## Docker

To build a docker image:

```shell
./pyex> docker build -t pyex:0.0.1 .
```

Run with environment variables:

```shell
$ docker run --name pyex -p 5001:5000 \
                -e "PYEX_EXCLUDE=<PYEX_EXCLUDE>" \
                -e "PYEX_DEFAULT=<PYEX_DEFAULT>" \
                -e "PYEX_FFILL=<PYEX_FFILL>" \
                -e "PYEX_VERBOSE=<true|false>" \
                 pyex 
```

## API Specification

Please check Open API Specification at:

```shell
pyex_oas.yml
```

## Processing steps
```bash
  Reader -> Processor1 -> Processor2 -> ... -> ProcessorN -> Writer
```

To define processor(s), using flag ```--processors```

For example:

```bash
.\pyex> pyex -i "file.xlsx" -o "file.json" -e "(How to fill Skill set|Title|Programming Language|Revision History)" --ffill "0,1" --processors \
.\pyex\example_processor\add_user_info.py:AddUserInfoProcessor \
.\pyex\example_processor\change_header.py:ChangeHeaderProcessor \
.\pyex\example_processor\remove_invalid_data.py:RemoveInvalidDataProcessor
```

Note that the order of processors is matter. To define your own processor, check ```example_processor```.

We can also create a "lazy" processor ie. an shorcut to run many processors at a time

```bash
.\pyex> pyex -i "file.xlsx" -o "file.json" -e "(How to fill Skill set|Title|Programming Language|Revision History)" --ffill "0,1" --processors \
.\pyex\example_processor\lazy_processor.py:LazyProcessor
```


## Usage

```shell
$ pyex -h
usage: pyex [-h] [--serve] [--host HOST] [--port PORT] [--input INPUT]
            [--output OUTPUT] [--exclude EXCLUDE] [--ffill FFILL]
            [--default DEFAULT] [--verbose]

 ___   _     ____  _    
| |_) \ \_/ | |_  \ \_/ 
|_|    |_|  |_|__ /_/ \ 
Excel to JSON converter.
Author: buivd4@hotmail.com
Version: 0.0.1

optional arguments:
  -h, --help            show this help message and exit
  --serve, -s           Run pyex API service
  --host HOST           Specify host of API service
  --port PORT           Specify port of API service
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