fpath = './day6_input.txt'

actual_input = open(fpath).read().split('\n')[:-1]
#print(actual_input)
example_input = ['Time:      7  15   30',
                 'Distance:  9  40  200']

testing = False

if testing:
    print(example_input)
    times = [int(x) for x in example_input[0].split()[1:]]
    dists = [int(x) for x in example_input[1].split()[1:]]
else:
    print(actual_input)
    times = [int(x) for x in actual_input[0].split()[1:]]
    dists = [int(x) for x in actual_input[1].split()[1:]]
    

'''
let x be time button is held down.


Then the remaining race duration is t-x, speed is x.
Distance travelled is then (t-x)x

We need to calculate how many integers x satisfy (t-x)x > d

tx-x^2 > d
-x^2+tx-d > 0
x^2 - tx + d < 0 
(x-t/2)^2 - t^2/4 + d < 0
(x-t/2 \pm \sqrt(t^2/4 - d)) < 0

i.e. x = t/2 - delta, t/2 + delta
where
delta = sqrt(t^2/4 - d)

'''
from math import sqrt, ceil

p = 1
def calc_n(t,d):
    delta = sqrt(t**2/4 - d)
    min_hold = ceil(t/2-delta)
    max_hold = int(t/2+delta)

    if (t-min_hold)*min_hold - d == 0:
        return max_hold-min_hold + 1 - 2 
    else:
        return max_hold-min_hold + 1
    
for t,d in zip(times, dists):
    n = calc_n(t,d)
    print(t,d,n)
    p *= n
print('\n',p)

    
### Part 2 ###
print('\n--- Part 2 ---\n')

if testing:
    t = ''.join(example_input[0].split(':')[1].split())
    d = ''.join(example_input[1].split(':')[1].split())
    print(t,d)
else:
    t = ''.join(actual_input[0].split(':')[1].split())
    d = ''.join(actual_input[1].split(':')[1].split())
    print(t,d)

print('\n', calc_n(int(t),int(d)))
