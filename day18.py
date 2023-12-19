example_input_orig = ['R 6 (#70c710)',
                 'D 5 (#0dc571)',
                 'L 2 (#5713f0)',
                 'D 2 (#d2c081)',
                 'R 2 (#59c680)',
                 'D 2 (#411b91)',
                 'L 5 (#8ceee2)',
                 'U 2 (#caa173)',
                 'L 1 (#1b58a2)',
                 'U 2 (#caa171)',
                 'R 2 (#7807d2)',
                 'U 3 (#a77fa3)',
                 'L 2 (#015232)',
                 'U 2 (#7a21e3)']
example_input = ['R 1 (#70c710)',
                 'U 3 ()',
                 'R 3 ()',
                 'D 3 ()',
                 'R 2 ()',
                 'U 3 ()',
                 'R 3 ()',
                 'D 5 ()',
                 'L 3 ()',
                 'D 3 (#0dc571)',
                 'L 2 (#5713f0)',
                 'D 2 (#d2c081)',
                 'R 2 (#59c680)',
                 'D 2 (#411b91)',
                 'L 2 (#8ceee2)',
                 'D 2 ()',
                 'L 2 ()',
                 'U 2 ()',
                 'L 1 ()',
                 'U 2 (#caa173)',
                 'L 1 (#1b58a2)',
                 'U 2 (#caa171)',
                 'R 2 (#7807d2)',
                 'U 3 (#a77fa3)',
                 'L 2 (#015232)',
                 'U 2 (#7a21e3)']
actual_input = open('./day18_input.txt').read().split('\n')[:-1]

testing = True

if testing:
    inp = [x.split() for x in example_input_orig]
else:
    inp = [x.split() for x in actual_input]


cur = (0,0)
dug = []
for row in inp:
    direction, distance, colour = row
    for i in range(int(distance)):
        if direction == 'R':
            cur = (cur[0], cur[1]+1)
        elif direction == 'L':
            cur = (cur[0], cur[1]-1)
        elif direction == 'D':
            cur = (cur[0]+1, cur[1])
        elif direction == 'U':
            cur = (cur[0]-1, cur[1])
        else:
            raise Exception('Unknown direction')
        dug.append(cur)
print((0,7) in dug)
print(dug)
Rn = min([x[0] for x in dug])
Rx = max([x[0] for x in dug])+1
Cn = min([x[1] for x in dug])
Cx = max([x[1] for x in dug])+1
print(dug)
for i,x in enumerate(dug):
    dug[i] = (x[0]-Rn, x[1]-Cn)
    
print(dug)
print(Rn,Rx,Cn,Cx)

R = Rx - Rn
C = Cx - Cn

import re
repr = []
from tqdm import tqdm
if True:
    
    for r in tqdm(range(R)):
        row = ['.' for _ in range(C)]
        for c in range(C):
            if (r,c) in dug:
                row[c] = '#'
        last = '.'
        lastc = max([x[1] for x in dug if x[0] == r])
        
        #interior = False
        #for c in range(Cn,Cx):
        #    if c > lastc:
        #        break
        #    if row[c] == '#' and last == '.':
        #        interior = True
        #    if row[c] == '.' and interior:
        #        row[c] = 'I'
        #        
        #    last = row[c]
        #
        if testing:
            print(''.join(row[:80]))
        repr.append(''.join(row))
else:
    interior = []
    from tqdm import tqdm
    for r in tqdm(range(R)):
        rdug = [x for x in dug if x[0] == r]
        #print(len(rdug)
        try:
            last = rdug[0][1]
        except IndexError:
            continue
        #print(last)
        srdug = sorted(rdug)
        inside = False
        if r == 11:
            import pdb
            #pdb.set_trace()
        for c in range(C):
            if c > last:
                break
            if inside and (r,c) not in dug:
                interior.append((r,c))

            if (r,c) in dug and (c == 0 or (r, c-1) not in dug):
                inside = not inside


    import matplotlib.pyplot as plt
    plt.plot([x[1] for x in dug],
             [-x[0] for x in dug], 'ro')
    plt.plot([x[1] for x in interior],
             [-x[0] for x in interior], 'bo')
    plt.show()
1/0
#print()
repr.insert(0, '.' * (Cx-Cn))
repr.append('.' * (Cx-Cn))
repr2 = [['.',] + list(rr) + ['.',] for rr in repr]
#for row in repr2:
#    print(row)
newrepr2 = [list(x) for x in repr2]
for r in tqdm(range(1, len(repr2)-1)):
    for c in range(1, len(repr2[0])-1):
        if repr2[r][c] == '#':
            if repr2[r][c-1] == '#' and repr2[r][c+1] == '#':
                newrepr2[r][c] = '-'
            elif repr2[r-1][c] == '#' and repr2[r+1][c] == '#':
                newrepr2[r][c] = '|'
            elif repr2[r-1][c] == '#' and repr2[r][c+1] == '#':
                newrepr2[r][c] = 'L'
            elif repr2[r+1][c] == '#' and repr2[r][c+1] == '#':
                newrepr2[r][c] = 'F'
            elif repr2[r-1][c] == '#' and repr2[r][c-1] == '#':
                newrepr2[r][c] = 'J'
            elif repr2[r+1][c] == '#' and repr2[r][c-1] == '#':
                newrepr2[r][c] = '7'
        if testing:
            print(newrepr2[r][c], end='')
    if testing:
        print()
inp2 = [''.join(x) for x in newrepr2]
for x in inp2:
    print(x)

R = len(inp2)
C = len(inp2[0])

def get_char(r,c,inp_):
    return inp_[r][c]


IOs = {}
for r,rx in enumerate(range(Rn,Rx)):
    for c,cx in enumerate(range(Cn,Cx)):
        if get_char(r,c,inp2) == '.':
            if testing:
                print(r,c,'interior')
            toE = inp2[r][:c]
            if testing:
                print(toE)
            vertical_wall_count = toE.count('|')
            # Also L7 and FJ (with any '-' in between)
            # counts as a wall
            toE = toE.replace('-','')
            vertical_wall_count += toE.count('L7')
            vertical_wall_count += toE.count('FJ')
            if vertical_wall_count % 2 == 1:
                if testing:
                    print('I')
                IOs[(rx,cx)] = 'I'
            else:
                if testing:
                    print('O')
                IOs[(rx,cx)] = 'O'
ctot = 0
if testing:
    for r,x in enumerate(inp2):
        x2 = list(x)
        for k in IOs.keys():
            if k[0] == r:
                x2[k[1]] = IOs[k]
        print(''.join(x2))
if True:
    import matplotlib.pyplot as plt
    plt.plot([x[0] for x in dug],
             [x[1] for x in dug], 'rx')
    plt.plot([x[0]-1 for x in IOs if IOs[x] == 'I'],
             [x[1]-1 for x in IOs if IOs[x] == 'I'], 'bo')
    plt.show()
ctot = len([x for x in IOs.values() if x == 'I']) + len(set(dug))
print('\n',ctot)
