'''
@Author: Andrew Quick
@Date Created: 01/01/2020
@Date Updated: 01/10/2020
@github.com/andrewtquick
'''

import re
import os
import sys
import datetime
import argparse
import pathlib
from subprocess import Popen


parser = argparse.ArgumentParser(
    prog='pyrenamer',
    usage='pyrenamer.py [--help -d -f] <path> <filters> <replace>',
    description='''Please review the README.md for proper usage. Rename
    directories and files using regular expressions substitution. If you need
    assistance with creating your regular expression operation, visit
    http://www.regexr.com or your favorite source.''',
    epilog='''PyRenamer by Andrew Quick || github.com/andrewtquick''')

parser.add_argument(
    '-d',
    '-dirs',
    action='store_true',
    help='use to rename directories'
)

parser.add_argument(
    '-f',
    '-files',
    action='store_true',
    help='use to rename files'
)

parser.add_argument(
    'Path',
    metavar='path',
    action='store',
    type=str,
    nargs='?',
    help='string, path (ex. C:/<my directory> or /home/<user>/<directory>)'
)

parser.add_argument(
    'filters',
    action='store',
    help='file, file list entry as .txt'
)

parser.add_argument(
    'replace',
    action='store',
    help='string, replace match with entry'
)

args = parser.parse_args()

if not os.path.isdir(args.Path):
    print('The path specified does not exist.')
    print('Exiting...')
    sys.exit()


def collect_files(path: str) -> list:

    file_list = []

    for root, _, files in os.walk(path):
        if args.f:
            for item in files:
                file_list.append(os.path.join(root, item))
        else:
            file_list.append(root)

    if path in file_list:
        file_list.remove(path)

    return file_list


def regex_rename(path: str) -> str:

    file_collection = collect_files(path)
    filters = open(args.filters, 'r').read().splitlines()
    regex_compile = re.compile(r'|'.join(filters))

    for item in file_collection:
        regex_replace = re.sub(regex_compile, args.replace, item)
        run_command(item, regex_replace)


def run_command(path: str, rename: str) -> None:

    if sys.platform == 'linux' or sys.platform == 'linux2':
        if args.f:
            filename, fileext = rename.rsplit('.', 1)
            destname = f'{filename.strip()}.{fileext}'
            Popen(f'mv "{path}" "{destname}"', shell=True).wait()
            completed(path, rename)
        else:
            Popen(f'mv "{path}" "{rename}/"', shell=True).wait()
            completed(path, rename)

    if sys.platform == 'win32':
        name = pathlib.Path(rename).name
        if args.f:
            filename, fileext = name.rsplit('.', 1)
            destname = f'{filename.strip()}.{fileext}'
            Popen(f'ren "{path}" "{destname}"', shell=True).wait()
            completed(path, destname)
        else:
            Popen(f'ren "{path}" "{name}"', shell=True).wait()
            completed(path, name)


def completed(path: str, name: str) -> None:

    now = datetime.datetime.now()
    completed = open('completed.txt', 'a')
    completed_msg = f'{now} :: Completed :: {path} {name}'
    completed.write(completed_msg + '\n')
    completed.close()


regex_rename(args.Path)
