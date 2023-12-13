example_input = ['#.##..##.',
                 '..#.##.#.',
                 '##......#',
                 '##......#',
                 '..#.##.#.',
                 '..##..##.',
                 '#.#.##.#.',
                 '',
                 '#...##..#',
                 '#....#..#',
                 '..##..###',
                 '#####.##.',
                 '#####.##.',
                 '..##..###',
                 '#....#..#']

actual_input = open('./day13_input.txt').read().split('\n')[:-1]

testing = False

if testing:
    inp = example_input
else:
    inp = actual_input

def delta(row1, row2):
    return sum([r1i != row2[i] for i,r1i in enumerate(row1)])

r1 = '#.##..##.'
r2 = '..##..##.'
print(delta(r1, r2))
print(delta('..####..#', r2))
print(delta(r1, r1))

def find_poss(pattern_):
    for i,row in enumerate(pattern_[1:]):
        d = delta(pattern_[i], row)
        if d < 2:
            print('possible',i,'-',i+1, f'({d})')
            yield i

def find_sym(pattern_, start):
    d2 = 1
    for i in range(start,-1,-1):
        row = pattern_[i]
        try:
            reflected_row = pattern_[2*start - i + 1]
        except IndexError:
            break
        d = delta(reflected_row, row)
        if d > d2:
            return False
        d2 -= d
    if d2 == 0:
        return True
    else:
        return False
            
def transpose(pattern_):
    return [''.join([x[i] for x in pattern_]) for i in range(len(pattern_[0]))]

def score(pattern_):
    c = 0
    for s in find_poss(pattern_):
        #print(s)
        if find_sym(pattern_, s):
            print('horizontal', s+1)
            c += 100 * (s+1)
            print( 100 * (s+1))
    tp = transpose(pattern_)
    for s in find_poss(tp):
        if find_sym(tp, s):
            print('vertical', s+1)
            c += s+1
            print(s+1)
    return c

tc = 0
n = 1
pattern = []
for row in inp:
    if len(row) > 0:
        pattern.append(row)
    else:
        print('---',n,'---')
        n += 1
        for x in pattern:
            print(x)
        tc += score(pattern)
        print('')
        pattern = []

print('---',n,'---')
for x in pattern:
    print(x)
tc += score(pattern)
#for s in find_poss(pattern):
#    print(find_sym(pattern, s))
#print()
#tp = transpose(pattern)
#for x in tp:
#    print(x)
#
#for s in find_poss(tp):
#    print(find_sym(tp, s))
print('\n',tc,'\n')

    
        
