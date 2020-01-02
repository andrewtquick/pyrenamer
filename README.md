# pyrenamer

Rename directories and files using regular expressions
substitution. If you need assistance with creating your regular
expression operation, visit http://www.regexr.com or your favorite
source.

-----------------------------------------------------------------------
usage: pyrenamer.py --help -d -f -re OPERATION -sub VALUE path

example: "python pyrenamer.py -d -re '(\056)' -sub ' ' D:\\Temp"

The example above replaces all periods with a whitespace in the
names of directories.
-----------------------------------------------------------------------

All completed renames are output to a completed.txt file in the working
directory with the command that was ran.

