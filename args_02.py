import sys

sys.argv = [0, 1, 2, 3, 4]
# NOTE: [1:] excludes the first item at index 0, i.e script name
argv_len = len(sys.argv[1:])
if not argv_len == 4:
 sys.exit(f'invalid number of arguments (expected 2, given: {argv_len})')
print('two arguments are:', sys.argv[1:])