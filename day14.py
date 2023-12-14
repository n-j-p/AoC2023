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

print(rounds)
print(cubes)

def rocks_in_col(j):
    return sorted([('O',i,x) for i,x in enumerate(rounds) if x[1] == j] + \
                  [('#',i,x) for i,x in enumerate(cubes) if x[1] == j],
                  key = lambda y: y[2][0])

print(rocks_in_col(2))

load = 0
mx = len(inp)
for col in range(len(inp[0])):
    print(col)
    mn = -1
    t = rocks_in_col(col)
    #print(t)
    for j,r in enumerate(t):
        if t[j][0] == 'O':
            t[j] = (t[j][0], t[j][1], [mn+1,t[j][2][1]])
            mn += 1
        else:
            mn = t[j][2][0]
    print(t)
    for r in t:
        if r[0] == 'O':
            load += mx - r[2][0]

print(load)
