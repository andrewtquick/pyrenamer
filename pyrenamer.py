'''
Rename directories and files using regular expressions
substitution. If you need assistance with creating your regular
expression operation, visit http://www.regexr.com or your favorite
source.

-----------------------------------------------------------------------
usage: pyrenamer.py [--help -d -f] [-re OPERATION] [-sub VALUE] path

example: "python pyrenamer.py -d -re '\056' -sub '\040 ' D:\\Temp"

The example above replaces all periods with a whitespace in the
names of directories.
-----------------------------------------------------------------------

All completed renames are output to a completed.txt file in the working
directory with the command that was ran.

@Author: Andrew Quick
@Date Created: 01/01/2020
@github.com/andrewtquick
'''

import re
import os
import sys
from subprocess import Popen
import datetime
import argparse
import pathlib


parser = argparse.ArgumentParser(
    prog='pyrenamer',
    usage='pyrenamer.py [--help -d -f] [-re OPERATION] [-sub VALUE] path',
    description='''Rename directories and files using regular expressions
    substitution. If you need assistance with creating your regular
    expression operation, visit http://www.regexr.com or your favorite
    source.''',
    epilog='''PyRenamer by Andrew Quick || github.com/andrewtquick''')

parser.add_argument(
    '-d',
    '-dirs',
    action='store_true',
    help='use to rename directories')

parser.add_argument(
    '-f',
    '-files',
    action='store_true',
    help='use to rename files')

parser.add_argument(
    '-re',
    metavar='OPERATION',
    action='store',
    help='string, regular expression operation',
    required=True)

parser.add_argument(
    '-sub',
    metavar='VALUE',
    action='store',
    help='string, replace with input for operation',
    required=True)

parser.add_argument(
    'Path',
    metavar='path',
    action='store',
    type=str,
    nargs='?',
    help='string, path (ex. C:/<my directory> or /home/<user>/<directory>)')

args = parser.parse_args()


def collect_files(path):

    fileList = []

    for root, _, files in os.walk(path):
        for movie in files:
            fileList.append(os.path.join(root, movie))

    if path in fileList:
        fileList.remove(path)

    return fileList


def collect_dirs(path):

    dirList = []

    for root, _, _ in os.walk(path):
        dirList.append(root)

    if path in dirList:
        dirList.remove(path)

    return dirList


def rename_path(path, argChoice):

    filePaths = collect_files(path)
    dirPaths = collect_dirs(path)

    if argChoice == 'files':
        for item in filePaths:
            _filePath = pathlib.Path(item).parent
            _fileName = pathlib.Path(item).name
            editedName = regex_rename(_filePath, _fileName)
            run_command(editedName)
    if argChoice == 'dirs':
        for item in dirPaths:
            _filePath = pathlib.Path(item).parent
            _fileName = pathlib.Path(item).name
            editedName = regex_rename(_filePath, _fileName)
            run_command(editedName)


def regex_rename(path, item):

    renamed = re.sub(args.re, args.sub, str(item))

    if sys.platform == 'linux' or sys.platform == 'linux2':
        cmd = f'mv "{path}/{str(item)}" "{path}/{renamed}"'
    elif sys.platform == 'win32':
        cmd = f'ren "{path}\\{str(item)}" "{renamed}"'
    return cmd


def run_command(cmd):

    Popen(cmd, shell=True).wait()
    completed(cmd)


def completed(cmd):

    now = datetime.datetime.now()
    completed = open('completed.txt', 'a')
    completed_msg = f'{now} :: Completed :: {cmd}'
    completed.write(completed_msg + '\n')
    completed.close()


if __name__ == '__main__':

    if not os.path.isdir(args.Path):
        print('The path specified does not exist.')
        print('Exiting...')
        sys.exit()

    if args.f:
        rename_path(args.Path, 'files')

    if args.d:
        rename_path(args.Path, 'dirs')
