actual_input = open('day10_input.txt').read().split('\n')[:-1]
start_row = [i for i,row in enumerate(actual_input) if 'S' in row][0]
start_col = actual_input[start_row].index('S')
print(actual_input[start_row][start_col])

legend = {'|': 'NS',
          '-': 'EW',
          'L': 'NE',
          'J': 'NW',
          '7': 'SW',
          'F': 'SE',
          '.': ''}
def opposite(direction):
    if direction == 'S':
        return 'N'
    if direction == 'N':
        return 'S'
    if direction == 'E':
        return 'W'
    if direction == 'W':
        return 'E'

def get_new_direction(r,c,previous_direction):
    inout = get_char(r,c)
    return legend[inout].replace(opposite(previous_direction),'')
    
def get_char(r,c):
    return actual_input[r][c]

def get_box(r, c):
    print(actual_input[r-1][(c-1):(c+2)])
    print(actual_input[r][(c-1):(c+2)])
    print(actual_input[r+1][(c-1):(c+2)])
get_box(start_row, start_col)

positions = [[start_row, start_col],
             [start_row, start_col]]
directions = ['N','E']
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

i = 0
while i == 0 or positions[0] != positions[1]:
    i += 1
    print(positions, directions)
    step()
print(positions, directions)
print(i)
