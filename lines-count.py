#!/usr/bin/env python3

import os
import sys

if len(sys.argv) != 2:
    print(f'Usage: lines-counter.py <filename>', file=sys.stderr)
else:
    filename = sys.argv[1]
    path_to_file = os.path.relpath(filename)
    
    try:
        fp = open(path_to_file, 'r')
    except FileNotFoundError:
        print(f"File is requested but doesn't exist", file=sys.stderr)
    except PermissionError:
        print(f'Trying to run an operation without the adequate access rights', file=sys.stderr)
    
    else:
        with fp:
            data = fp.readlines()
            print(f'{filename}\t{len(data)}')

