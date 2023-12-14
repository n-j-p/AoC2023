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
def xpand(pattern_):
    
    xpand_rows = find_zero_rows(pattern_)
    xpand_cols = find_zero_rows(transpose(pattern_))

    for i in xpand_rows[::-1]:
        pattern_ = pattern_[:i] + \
            [pattern_[i],] * 2 + \
            pattern_[(i+1):]
    pattern_ = transpose(pattern_)
    for i in xpand_cols[::-1]:
        pattern_ = pattern_[:i] + \
            [pattern_[i],] * 2 + \
            pattern_[(i+1):]
    return transpose(pattern_)

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
expanded_input = xpand(list(inp))
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
    
