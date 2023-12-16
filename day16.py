# Use V instead of \ to prevent escapes:

example_input=['.|...V....',
               '|.-.V.....',
               '.....|-...',
               '........|.',
               '..........',
               '.........V',
               '..../.VV..',
               '.-.-/..|..',
               '.|....-|.V',
               '..//.|....']
testing = False
if testing:
    inp = example_input
else:
    inp = open('./day16_input.txt').read().replace('\\','V').split('\n')[:-1]

R = len(inp)
C = len(inp[0])

nrgised = set(())

# Directions are: 0 = 'N', 1 = 'E', 2 = 'S', 3 = 'W'
start = (0,0,1) # x pos, y pos, direction

# Trace one beam
def trace_beam(cur_):
    while True:
        nrgised.add(cur_)

        cur_symbol = inp[cur_[0]][cur_[1]] 
        cur_dir = cur_[2]
        
        # Check if beam is being split:
        if cur_symbol == '|':
            if cur_dir in [1,3]:
                # returned values get put back into Queue
                return [(cur_[0], cur_[1], 0),
                        (cur_[0], cur_[1], 2)]
        elif cur_symbol == '-':
            if cur_dir in [0,2]:
                return [(cur_[0], cur_[1], 1),
                        (cur_[0], cur_[1], 3)]
        # Otherwise, continue beam journey:
        # Change direction if we encounter a mirror
        if cur_symbol == '/':
            if cur_dir == 0:
                nxt_dir = 1
            elif cur_dir == 1:
                nxt_dir = 0
            elif cur_dir == 2:
                nxt_dir = 3
            else:
                nxt_dir = 2
        elif cur_symbol == 'V': # i.e. \ E(1) -> S(2), N(0) -> W(3),
                                #        W(3) -> N(0), S(2) -> E(1)
            if cur_dir == 0:
                import pdb
                #pdb.set_trace()
                nxt_dir = 3
            elif cur_dir == 1:
                nxt_dir = 2
            elif cur_dir == 2:
                nxt_dir = 1
            else: #cur_dir == 3
                nxt_dir = 0
        else:
            nxt_dir = cur_dir

        nxt = []
        if nxt_dir == 0:
            nxt = [cur_[0]-1,
                   cur_[1]]
        elif nxt_dir == 1:
            nxt = [cur_[0],
                   cur_[1]+1]
        elif nxt_dir == 2:
            nxt = [cur_[0]+1,
                   cur_[1]]
        else: # nxt_dir == 3
            nxt = [cur_[0],
                   cur_[1]-1]

        nxt.append(nxt_dir)

        # Check if we have left the grid:
        if nxt[0] < 0 or nxt[0] >= R or nxt[1] < 0 or nxt[1] >= C:
            print('left grid')
            break

        tnxt = tuple(nxt)
        if tnxt not in nrgised: # eliminate identical beam pos/directions:
            cur_ = tnxt
        else:
            return []
    return []

Q = [start]
print(Q)
while len(Q) > 0:
    cur = Q.pop(0)
    print(cur)
    split_beams = trace_beam(cur)
    for beam in split_beams:
        Q.append(beam)
    
# Output:
for x in inp:
    print(x)
print()
print(nrgised)
#nrg_grid = [['.',]*C for _ in range(R)]
nrg_grid = [list(x) for x in inp]
for x in nrgised:
    nrg_grid[x[0]][x[1]] = '#'
for x in nrg_grid:
    print(''.join(x))

print('\n',len(set([x[:2] for x in nrgised])))
                                        
