import re
import time

tt = time.time()

fpath = './day1_input.txt'
input = open(fpath).read().split('\n')

digits = re.compile('\d')
xtracted_digits = [digits.findall(row) for row in input]
first_last = [(x[0], x[0]) if len(x) == 1 \
              else ((x[0], x[-1]) if len(x) > 1 \
                    else ('0','0')) for x in xtracted_digits] 
calibration_values = [int(''.join(x)) for x in first_last] 
print(f'Done in {(time.time()-tt)*10**6:.1f}us')
print(sum(calibration_values))

