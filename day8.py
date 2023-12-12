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

### Part 2 ###

allstates = [x for x in states.keys() if x[-1] == 'A']

print(f'{0}: {allstates}')
step = 0
Zs = [[] for _ in range(len(allstates))]
brk = False
while True:
    for direction in lr:
        step += 1
        nxt = []
        for i,state in enumerate(allstates):
            nxtstate = states[allstates[i]][direction]
            #print(nxtstate)
            nxt.append(nxtstate)
        print(f'{step}: {nxt}')
        #print('  ',[x[-1] for x in nxt])
        #print(''.join([x[-1] for x in nxt]))
        if ''.join([x[-1] for x in nxt]) == 'Z'*len(allstates):
            break
        for i,x in enumerate(nxt):
            if x[-1] == 'Z':
                Zs[i].append(step)
                
        if sum([len(x)>0 for x in Zs]) == len(allstates):
            brk = True
            break
        
        allstates = list(nxt)
    if brk:
        break
for x in Zs:
    print(x)
import math
print('\n',math.lcm(*[x[0] for x in Zs]))

