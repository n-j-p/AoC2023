actual_input = open('./day9_input.txt').read().split('\n')[:-1]
example_input = ['0 3 6 9 12 15',
                 '1 3 6 10 15 21',
                 '10 13 16 21 30 45']

def diff(seq):
    dseq = []
    last = seq[0]
    for i,nxt in enumerate(seq[1:]):
        dseq.append(nxt - last)
        last = nxt
    return dseq

def same(seq):
    first = seq[0]
    for n in seq[1:]:
        if n != first:
            return False
    return True

testing = False
if testing:
    inp = example_input
else:
    inp = actual_input

cf = 0
cb = 0
for row in inp:
    seq = [int(x) for x in row.split()]
    diffs = [seq]
    #print(same(diffs[-1]))
    while not same(diffs[-1]):
        diffs.append(diff(diffs[-1]))
        #print(diffs)
        #print(same(diffs[-1]))
    first = 0
    last = 0
    for x in diffs[::-1]:
        x.append(x[-1] + last)
        x.insert(0,x[0]-first)
        last = x[-1]
        first = x[0]
    print(' ',diffs[0][-1], diffs[0][0])
    cf += diffs[0][-1]
    cb += diffs[0][0]

print('\n')
print(cf,cb)
