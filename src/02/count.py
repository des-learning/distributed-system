import sys

lines_number = 0
for line in sys.stdin:
    lines_number = lines_number + 1

sys.stdout.write(str(lines_number))
sys.stdout.write('\n')
