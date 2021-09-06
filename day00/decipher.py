import sys

print(''.join([word[0] for word in sys.argv[1].strip('\n').lower().split()]))
