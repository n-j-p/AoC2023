actual_input = open('day12_input.txt').read().split('\n')[:-1]

example_input = ['???.### 1,1,3',
                 '.??..??...?##. 1,1,3',
                 '?#?#?#?#?#?#?#? 1,3,1,6',
                 '????.#...#... 4,1,1',
                 '????.######..#####. 1,6,5',
                 '?###???????? 3,2,1']
testing = False
if testing:
    inp = example_input
else:
    inp = actual_input

import rle
import itertools as it

def encode(rec):
    if rec[0] == '#':
        return rle.encode(rec)[1][::2]
    else:
        return rle.encode(rec)[1][1::2]
assert encode('#.#.###')==[1,1,3]
assert encode('.#...#....###.') ==[1,1,3]
assert encode('.#.###.#.######') ==[1,3,1,6]
assert encode('####.#...#...') ==[4,1,1]
assert encode('#....######..#####.') ==[1,6,5]
assert encode('.###.##....#') ==[3,2,1]

def replaceQ(rec, nhash):
    nQ = rec.count('?')
    iQ = [-1]
    for n in range(nQ):
        iQ.append(rec.index('?',iQ[-1]+1))
    iQ.pop(0)
                  
    replacements = it.combinations(iQ, nhash)
    for repl in replacements:
        newrec = list(rec)
        for j,i in enumerate(iQ):
            if i in repl:
                newrec[i] = '#'
            else:
                newrec[i] = '.'
            #    newhand[i] = repl[j]
        yield ''.join(newrec)


c = 0
for row in inp:
    ci = 0
    record, groups = row.split(' ')
    groups = [int(x) for x in groups.split(',')]
    xtra = sum(groups) - record.count('#')
    for newrecord in replaceQ(record, xtra):
        ans = encode(newrecord)
        if ans == groups:
            print(newrecord)
            ci += 1
    c += ci
    print(ci,
          '\n')
print('\n',c)
