ex1 = ['7-F7-',
       '.FJ|7',
       'SJLL7',
       '|F--J',
       'LJ.LJ']
ex2 = ['.F----7F7F7F7F-7....',
       '.|F--7||||||||FJ....',
       '.||.FJ||||||||L7....',
       'FJL7L7LJLJ||LJ.L-7..',
       'L--J.L7...LJS7F-7L7.',
       '....F-J..F7FJ|L7L7L7',
       '....L7.F7||L7|.L7L7|',
       '.....|FJLJ|FJ|F7|.LJ',
       '....FJL-7.||.||||...',
       '....L---J.LJ.LJLJ...']
ex3 = ['FF7FSF7F7F7F7F7F---7',
       'L|LJ||||||||||||F--J',
       'FL-7LJLJ||||||LJL-77',
       'F--JF--7||LJLJ7F7FJ-',
       'L---JF-JLJ.||-FJLJJ7',
       '|F|F-JF---7F7-L7L|7|',
       '|FFJF7L7F-JF7|JL---7',
       '7-L-JL7||F7|L7F-7F7|',
       'L.L7LFJ|||||FJL7||LJ',
       'L7JLJL-JLJLJL--JLJ.L']

actual_input = open('day10_input.txt').read().split('\n')[:-1]

testing = False

legend = {'|': 'NS',
          '-': 'EW',
          'L': 'NE',
          'J': 'NW',
          '7': 'SW',
          'F': 'SE',
          '.': ''}
    
def print_box(r, c, inp_):
    # Print a 3x3 box from the map
    print(inp_[r-1][(c-1):(c+2)])
    print(inp_[r][(c-1):(c+2)])
    print(inp_[r+1][(c-1):(c+2)])
    
def get_char(r,c,inp_):
    return inp_[r][c]

def get_start(inp_):
    srow = [i for i,row in enumerate(inp_) if 'S' in row][0]
    scol = inp_[srow].index('S')

    N = get_char(srow-1, scol, inp_)
    S = get_char(srow+1, scol, inp_)
    E = get_char(srow, scol+1, inp_)
    W = get_char(srow, scol-1, inp_)

    directions = []
    if 'S' in legend[N]:
        directions.append('N')
    if 'W' in legend[E]:
        directions.append('E')
    if 'N' in legend[S]:
        directions.append('S')
    if 'E' in legend[W]:
        directions.append('W')

    assert len(directions) == 2
    
    return (srow, scol), directions

def opposite(direction):
    if direction == 'S':
        return 'N'
    if direction == 'N':
        return 'S'
    if direction == 'E':
        return 'W'
    if direction == 'W':
        return 'E'

def print_with_seen(inp_, seen_):
    print()
    for r,x in enumerate(inp_):
        row = list(x)
        for coord in seen_:
            if coord[0] == r:
                row[coord[1]] = '#'
        print(''.join(row))
    print()
    
    

def walkthrough(inp_, VERBOSE=False):
    def get_new_direction(r,c,previous_direction):
        inout = get_char(r,c, inp_)
        return legend[inout].replace(opposite(previous_direction),'')

    def step():
        for i,d in enumerate(directions):
            r,c=positions[i]
            if d == 'N':
                r -= 1
            elif d == 'S':
                r += 1
            elif d == 'E':
                c += 1
            else:
                c -= 1
            positions[i] = [r,c]
            directions[i] = get_new_direction(r,c,directions[i])
    
    (start_row, start_col), start_directions = get_start(inp_)

    positions = [[start_row, start_col],
                 [start_row, start_col]]
    directions = list(start_directions)

    seen_positions = set(())
    
    i = 0
    while i == 0 or positions[0] != positions[1]:
        i += 1
        #print(positions, directions)
        seen_positions.add(tuple(positions[0]))
        seen_positions.add(tuple(positions[1]))
        step()
        if VERBOSE:
            print_with_seen(inp_, seen_positions)
    seen_positions.add(tuple(positions[0]))
    if VERBOSE:
        print_with_seen(inp_, seen_positions)
    #print(positions, directions)
    #print(i)
    return i, seen_positions

### --- Part 1 --- ###

if testing:
    inp = ex3
else:
    inp = actual_input
R = len(inp)
C = len(inp[0])

length, seen = walkthrough(inp)
print_with_seen(inp, seen)
print('\n', length)
      

### --- Part 2 --- ###

# First clear out the junk pipe (i.e. set anything not traversed in part 1
# to clear ground ".")

for r,x in enumerate(inp):
    xrow = list(x)
    for col in range(C):
        if (r, col) not in seen:
            xrow[col] = '.'
    inp[r] = ''.join(xrow)

IOs = {}
for r in range(R):
    for c in range(C):
        if get_char(r,c,inp) == '.':
            print(r,c,'interior')
            toE = inp[r][:c]
            vertical_wall_count = toE.count('|')
            # Also L7 and FJ (with any '-' in between)
            # counts as a wall
            toE = toE.replace('-','')
            vertical_wall_count += toE.count('L7')
            vertical_wall_count += toE.count('FJ')
            if vertical_wall_count % 2 == 1:
                print('I')
                IOs[(r,c)] = 'I'
            else:
                print('O')
                IOs[(r,c)] = 'O'
for r,x in enumerate(inp):
    x2 = list(x)
    for k in IOs.keys():
        if k[0] == r:
            x2[k[1]] = IOs[k]
    print(''.join(x2))
ctot = len([x for x in IOs.values() if x == 'I'])
print('\n',ctot)
