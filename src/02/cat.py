import sys

with open(sys.argv[1]) as f:
    for line in f:
        sys.stdout.write(line)
