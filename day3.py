import re
from collections import Counter

fpath = './day3_input.txt'
maze = open(fpath).read().split('\n')[:-1]

# Sets of strings:
numerals = set(('1','2','3','4','5','6','7','8','9','0'))

chars = set(())
for y in [set(x) for x in maze]:
    chars = chars.union(y)
syms = chars.difference(numerals)
parts = syms.difference(['.'])

# Return symbol at coordinates (x,y). If it is off the grid,
# return '.'
def lkup(x,y):
    try:
        symbol = maze[x][y]
    except IndexError:
        return '.'
    return symbol

t = 0
nums = re.compile('\d+')
c = 0
gearno = 0
gears = {}
numno = 0
numbers = {}
for rowno, row in enumerate(maze):
    for z in nums.finditer(row):
        numbers[numno] = (rowno, z.start(), row[z.start():z.end()])
        numno += 1
        t += 1
        touching = False

        for r in range(rowno-1, rowno+2):
            for i in range(z.start()-1, z.end()+1):
                sym = lkup(r,i)
                if sym in parts: 
                    touching = True
                if sym == '*':
                    gears[gearno] = ((r,i), numno-1)
                    gearno += 1
        if touching:
            c += int(z.group())


ratio_sum = 0
cc = Counter()
for g in gears.values():
    cc.update((g[0],))
actual_gear_coords = [x[0] for x in cc.items() if x[1] == 2]

for gr in actual_gear_coords:
    print('Gear at',gr, end=' connects ')
    ratio = 1
    for num_coords in gears.values():
        if gr == num_coords[0]:
            print(numbers[num_coords[1]], end=', ')
            ratio *= int(numbers[num_coords[1]][2])
        
    print('ratio is',ratio)
    ratio_sum += ratio
print()
print('Answer to part 1:',c)
print('Answer to part 2:',ratio_sum)


