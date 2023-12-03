import re # Use the re module to parse strings
import time

tt = time.time()

written_numbers = ['zero',
                   'one',
                   'two',
                   'three',
                   'four',
                   'five',
                   'six',
                   'seven',
                   'eight',
                   'nine']

string_digits = ['0','1','2','3','4','5','6','7','8','9']

# Dictionary to decode strings into integers
decode = {x:str(i%10) for i,x in enumerate(written_numbers + string_digits)}

# Read in data
fpath = './day1_input.txt'
input = open(fpath).read().split('\n')

# Standard re search fails on overlapping strings, use a
# "look-ahead assertion", cf. https://stackoverflow.com/a/39765790
digits = re.compile('(?=(\d|' + '|'.join(written_numbers) + '))')

# Extract all digits (written or numerals) in input rows:
xtracted_digits = [digits.findall(row) for row in input]

# Take the first and last digits, or repeat the first if only one is present
first_last = [(x[0], x[0]) if len(x) == 1 \
              else ((x[0], x[-1]) if len(x) > 1 \
                    else ('0','0')) for x in xtracted_digits]

# Decode and convert to int
calibration_values = [int("".join([decode[y] for y in x])) for x in first_last]
for x in zip(input, calibration_values):
    print(x)

print(f'Done in {(time.time()-tt)*10**3:.1f}ms')
print(sum(calibration_values))

