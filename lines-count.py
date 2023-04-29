#!/usr/bin/env python3

import os
import sys

if len(sys.argv) != 2:
    print(f'Usage: lines-counter.py <filename>', file=sys.stderr)

else:
    filename = sys.argv[1]
    path_to_file = os.path.relpath(filename)
    if os.path.isfile(path_to_file):
        with open(path_to_file, 'r') as f:
            data = f.readlines()
            print(f'{filename}\t{len(data)}')
    else:
        print(f'No such file <{filename}>', file=sys.stderr)
