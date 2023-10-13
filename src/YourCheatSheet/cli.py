#!/usr/bin/env python3
import argparse, shutil, pathlib, os
from sys import argv
from main import Parser

db_file = ''
home_dir = (pathlib.Path.home())
os_name = os.name

##Check user os
if os_name == 'posix':
    db_file = f'{home_dir}/.config/YourCheatSheet.md'
else:
    print('Version for your OS is not available!')
    os.exit(1)

##Check if MD file in .config directory
try:
    md_file = pathlib.Path(db_file)
    docs = Parser(md_file)
    docs.get_data(*argv[1:])
##Ask user to specified MD file
except(NotADirectoryError,FileNotFoundError):

    parser = argparse.ArgumentParser(
        prog='YourCheatSheet',
        description="Parse your MD CheetSheets",
        epilog='2023 Open-source license'
        )

    parser.add_argument('--init','-i', type=str, help='specified your .MD file or folder')

    args = parser.parse_args()

    if args.init:
        print(f'Going to copy {args.init}')
        shutil.copy(args.init, db_file)


