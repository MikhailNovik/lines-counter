#!/usr/bin/env python3

import sys


if len(sys.argv) != 2:
    print(f'Usage: lines-counter.py <filename>')
else:
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        data = f.readlines()
        print(f'{filename}\t{len(data)}')
