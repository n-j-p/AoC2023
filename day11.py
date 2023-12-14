example_input = ['...#......',
                 '.......#..',
                 '#.........',
                 '..........',
                 '......#...',
                 '.#........',
                 '.........#',
                 '..........',
                 '.......#..',
                 '#...#.....']

actual_input = open('./day11_input.txt').read().split('\n')[:-1]

testing = False
if testing:
    inp = example_input
else:
    inp = actual_input

def transpose(pattern_):
    return [''.join([x[i] for x in pattern_]) for i in range(len(pattern_[0]))]
def find_zero_rows(pattern_):
    ans = []
    for i,row in enumerate(pattern_):
        if '#' not in row:
            ans.append(i)
    return ans
def xpand(pattern_, m=1):
    
    xpand_rows = find_zero_rows(pattern_)
    xpand_cols = find_zero_rows(transpose(pattern_))

    for i in xpand_rows[::-1]:
        pattern_ = pattern_[:i] + \
            [pattern_[i],] * (m+1) + \
            pattern_[(i+1):]
    pattern_ = transpose(pattern_)
    for i in xpand_cols[::-1]:
        pattern_ = pattern_[:i] + \
            [pattern_[i],] * (m+1) + \
            pattern_[(i+1):]
    return transpose(pattern_),xpand_rows,xpand_cols

def get_hash_coords(pattern_):
    n = 0
    for i,row in enumerate(pattern_):
        j0 = -1
        for _ in range(row.count('#')):
            j = row.index('#', j0+1)
            yield (i,j)
            j0 = j
            n += 1
    
def d(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

print()
import itertools as it


for x in inp:
    print(x)
print()
print(list(get_hash_coords(inp)))
print()
expanded_input, rows, cols = xpand(list(inp), 9)
for x in expanded_input:
    print(x)
print()
print(list(get_hash_coords(expanded_input)))
print()

c = 0
for xy in it.combinations(get_hash_coords(expanded_input),
                          r=2):
    
    print(xy, d(*xy))
    c += d(*xy)
print()
print(c)
print()


import bisect

multiplier = 10**6-1

c = 0
for xy in it.combinations(get_hash_coords(inp),
                          r=2):
    exp_xyx = list(xy[0])
    expanded_x = list(xy[0])
    expanded_y = list(xy[1])
    expanded_x[1] += bisect.bisect(cols, expanded_x[1]) * multiplier
    expanded_x[0] += bisect.bisect(rows, expanded_x[0]) * multiplier
    expanded_y[1] += bisect.bisect(cols, expanded_y[1]) * multiplier
    expanded_y[0] += bisect.bisect(rows, expanded_y[0]) * multiplier

    print((expanded_x, expanded_y),
          d(expanded_x, expanded_y))
    c += d(expanded_x, expanded_y)

print(c)
#print(rows, cols)
