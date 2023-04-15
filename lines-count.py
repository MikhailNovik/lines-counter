import sys

print(f'sys.argv: {sys.argv[1]}')

with open(sys.argv[1], 'r') as f:
    data = f.readlines()

print(f'Количество строк в файле: {len(data)}')