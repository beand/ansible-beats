#!/usr/bin/env python3
import fileinput
import os

"""
This script is used to bump beats versions before a new release

Usage:
- Change the values of `old_versions` and `new_versions``
- Run the script: `./bumper.py`
- That's all
"""

os.chdir(os.path.join(os.path.dirname(__file__), '..'))

old_versions = {
    6: '6.8.5',
    7: '7.5.1',
}

new_versions = {
    6: '6.8.6',
    7: '7.5.2',
}

files = [
    'README.md',
    'defaults/main.yml',
    'test/integration/standard-6x.yml',
    '.kitchen.yml',
]

for major, version in old_versions.items():
    for file in files:
        print(file)
        for line in fileinput.input([file], inplace=True):
            print(line.replace(version, new_versions[major]), end='')
