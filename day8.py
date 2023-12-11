actual_input = open('./day8_input.txt').read().split('\n')[:-1]

example_input = ['LLR',
                 '',
                 'AAA = (BBB, BBB)',
                 'BBB = (AAA, ZZZ)',
                 'ZZZ = (ZZZ, ZZZ)']

testing = False
if testing:
    inp = example_input
else:
    inp = actual_input
lr = inp[0]
states = {}
for row in inp[2:]:
    rowsp = row.split('=')
    LR = rowsp[1].split(',')
    L = LR[0].replace('(','').strip()
    R = LR[1].replace(')','').strip()
    states[rowsp[0].strip()] = {'L': L, 'R': R}
print(states)

state = 'AAA'
print(f'{0}: {state}')
step = 0
while True:
    for direction in lr:
        step += 1
        state = states[state][direction]
        print(f'{step}: {state}')
        if state == 'ZZZ':
            break
    if state == 'ZZZ':
        break
print('\n',step)
