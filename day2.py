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


def minimal_set(agame):
    minimals = {'red': 0, 'green': 0, 'blue': 0}
    for move in game:
        for col in move.keys():
            minimals[col] = max(move[col], minimals[col])
    return minimals

def power(minimals):
    p = minimals['red'] * minimals['green'] * minimals['blue']
    return p

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
    game_power = power(minimal_set(game))
    print('  ',game_power)
    c += game_power

print(c)
    
print(f'\nDone in {(time.time()-tt)*10**3:.1f}ms')


