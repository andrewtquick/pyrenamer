# PyRenamer

> Using regular expressions to manipulate the names of multiple files and directories

![Python Version](https://img.shields.io/badge/python-v3.8.1-green) ![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux-lightgrey)

PyRenamer accepts in a text file of regular expressions, parses the expressions, and runs the file name or directory through each regular expression eliminating the specified targets. PyRenamer will put all completed expressions into a 'completed.txt', at your current working directory, file for your viewing.

For building the right regular expression, regexr.com is recommended, but please use your favorite source.

For identifying the escaped hex code for a particular character, I recommend asciitable.com

## Installation

```sh
git clone https://github.com/andrewtquick/pyrenamer.git
```

## Usage Example

PyRenamer is using the argparse module to pass through your choices.

PyRenamer accepts arguments from your CLI, usage standard is as follows:

```sh
usage: pyrenamer.py [--help -d -f] <path> <filters> <replace>
```

```sh
pyrenamer.py --help

positional arguments:
  path        string, path (ex. C:/<my directory> or /home/<user>/<directory>)
  filters     file, file list entry as .txt
  replace     string, replace match with entry

optional arguments:
  -h, --help  show this help message and exit
  -d, -dirs   use to rename directories
  -f, -files  use to rename files
```

##### Directory rename usage hint:

Replace all directory names from your matches in your filters.txt file to a whitespace

```sh
pyrenamer.py -d /home/user/path/ filters.txt '\040'
```

##### File rename usage hint:

Replace all file names from your matches in your filters.txt file to Today-9AM

```sh
pyrenamer.py -f C:\\My Files\\ filters.txt 'Today-9AM'
```

## Filters.txt Setup

Add the regular expressions you'd like to filter with into a text file, separated by a newline, \n. The name of the file does not matter. If the file is in a different location then pyrenamer, ensure you include the path with the file name.

There is no limit to the amount of expressions you can include. Please be mindful of your replace expression.

##### Expression File Formatting

If the expression does not find a match, the file will be skipped.

```
\s\133Testing\135 -> Looking for ' [Testing]'
\s\s+             -> Looking for '  '
\sTesting-\135    -> Looking for ' Testing-]'
(?!\046)\s[a-z]+  -> Looking for words after an ampersand that are lowercase
```
