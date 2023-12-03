import re # Use the re module to parse strings
import time

tt = time.time()


# Read in data
fpath = './day2_input.txt'
input = open(fpath).read().split('\n')
#print(input)

def parse_input(input_line):
    drop_game_string = input_line[(input_line.index(':')+2):]
    moves = drop_game_string.split(';')
    moves_split = [x.split(',') for x in moves]
    moves_split2 = [[y.lstrip().split(' ') for y in x] for x in moves_split]
    return moves_split2


def check_move_possible(amove):
    possible = True
    max_cubes = {'red': 12,
                 'green': 13,
                 'blue': 14}
    for col in max_cubes.keys():
        try:
            possible = possible & (amove[col] <= max_cubes[col])
        except KeyError:
            pass
    return possible

def check_game_possible(agame):
    for move in game:
        if not check_move_possible(move):
            return False
    return True

c = 0

for i, row in enumerate(input):
    if len(row) == 0:
        break
    game = []
    for x in parse_input(row):
        move = {}
        for y in x:
            move[y[1]] = int(y[0])
        game.append(move)
    print(f'Game {i+1}:',game)
    poss = check_game_possible(game)
    print('  ',poss)
    if poss:
        c += i+1

print(c)
    
print(f'\nDone in {(time.time()-tt)*10**3:.1f}ms')


