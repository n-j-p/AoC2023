example_input = ['O....#....',
                 'O.OO#....#',
                 '.....##...',
                 'OO.#O....O',
                 '.O.....O#.',
                 'O.#..O.#.#',
                 '..O..#O..O',
                 '.......O..',
                 '#....###..',
                 '#OO..#....']
actual_input = open('./day14_input.txt').read().split('\n')[:-1]

testing = False
if testing:
    inp = example_input
else:
    inp = actual_input

def calculate_load_from_coords(coords_, N=len(inp)):
    loads = [N-x[0] for x in coords_]
    return sum(loads)
    
def get_coords(pattern, char):
    n = 0
    for i,row in enumerate(pattern):
        j0 = -1
        for _ in range(row.count(char)):
            j = row.index(char, j0+1)
            yield [i,j]
            j0 = j
            n += 1
rounds = list(get_coords(inp, 'O'))
cubes = list(get_coords(inp, '#'))
print('Rounds')
print(rounds)
print('\nCubes')
print(cubes)
print()

def rocks_in_col(j, r, c=cubes):
    return sorted([('O',i,x) for i,x in enumerate(r) if x[1] == j] + \
                  [('#',i,x) for i,x in enumerate(cubes) if x[1] == j],
                  key = lambda y: y[2][0])

def rocks_in_row(i, r, c=cubes):
    return sorted([('O',j,x) for j,x in enumerate(r) if x[0] == i] + \
                  [('#',j,x) for j,x in enumerate(cubes) if x[0] == i],
                  key = lambda y: y[2][1])
def cycle(rounds_):
    # Tilt north
    #print()
    newrounds = []
    load = 0
    mx = len(inp)
    for col in range(len(inp[0])):
        #print(col)
        mn = -1
        t = rocks_in_col(col, rounds_)
        ##print(t)
        for j,r in enumerate(t):
            if t[j][0] == 'O':
                t[j] = (t[j][0], t[j][1], [mn+1,t[j][2][1]])
                newrounds.append([mn+1,t[j][2][1]])
                mn += 1
                ## Replace entries in "rounds" list
                #rounds[t[j][1]] = t[j][2]
            else:
                mn = t[j][2][0]

        #print(t)

    new_input = [x.replace('O','.') for x in inp]
    for r in newrounds:
        new_input[r[0]] = new_input[r[0]][:r[1]] + 'O' + new_input[r[0]][(r[1]+1):]
    #for x in new_input:
    #    print(x)
    #print(newrounds)
    #print(calculate_load_from_coords(newrounds))

    ##print(rocks_in_row(1))


    ## Next: tilt west

    #print()
    rounds_ = [list(x) for x in newrounds]
    newrounds = []
    load = 0
    mx = len(inp)
    for row in range(len(inp)):
        #print(row)
        mn = -1
        t = rocks_in_row(row, rounds_)
        ##print(t)
        for j,r in enumerate(t):
            if t[j][0] == 'O':
                t[j] = (t[j][0], t[j][1], [t[j][2][0],mn+1])
                newrounds.append([t[j][2][0],mn+1])
                mn += 1
            else:
                mn = t[j][2][1]

        #print(t)

    new_input = [x.replace('O','.') for x in inp]
    for r in newrounds:
        new_input[r[0]] = new_input[r[0]][:r[1]] + 'O' + new_input[r[0]][(r[1]+1):]
 #   for x in new_input:
#        #print(x)

    ##print(rocks_in_row(1))


    ## Next: tilt south

    #print()
    rounds_ = [list(x) for x in newrounds]
    newrounds = []
    load = 0
    mx = len(inp)
    for col in range(len(inp[0])):
        #print(col)
        t = rocks_in_col(col, rounds_)
        mn = len(inp)
        ##print(t)
        for j,r in enumerate(t[::-1]):
            jj = len(t)-1-j
            if t[jj][0] == 'O':
                t[jj] = (t[jj][0], t[jj][1], [mn-1,t[jj][2][1]])
                newrounds.append([mn-1,t[jj][2][1]])
                mn -= 1
            else:
                mn = t[jj][2][0]

        #print(t)

    new_input = [x.replace('O','.') for x in inp]
    for r in newrounds:
        new_input[r[0]] = new_input[r[0]][:r[1]] + 'O' + new_input[r[0]][(r[1]+1):]
#    for x in new_input:
        #print(x)

    ##print(rocks_in_row(1))


    ## Finally: tilt east

    #print()
    rounds_ = [list(x) for x in newrounds]
    newrounds = []
    load = 0
    mx = len(inp)
    for row in range(len(inp)):
        #print(row)
        t = rocks_in_row(row, rounds_)
        mn = len(inp)

        for j,r in enumerate(t[::-1]):
            jj = len(t)-1-j
            if t[jj][0] == 'O':
                t[jj] = (t[jj][0], t[jj][1], [t[jj][2][0],mn-1])
                newrounds.append([t[jj][2][0],mn-1])
                mn -= 1
            else:
                mn = t[jj][2][1]

        #print(t)

    new_input = [x.replace('O','.') for x in inp]
    for r in newrounds:
        new_input[r[0]] = new_input[r[0]][:r[1]] + 'O' + new_input[r[0]][(r[1]+1):]
#    for x in new_input:
        #print(x)

    #print(rocks_in_row(1))

    return new_input

#for x in inp:
#    print(x)

loads = []
for i in range(200):
    print('\n\n\n\n')
    cycled = cycle(list(rounds))
    for x in cycled:
        print(x)

    newrounds = list(get_coords(cycled, 'O'))
    print(newrounds)
    load = calculate_load_from_coords(newrounds)
    print(load)
    loads.append(load)
    rounds = list(newrounds)

print(loads)
