actual_input = open('day7_input.txt').read().split('\n')[:-1]

testing = False

example_input = ['32T3K 765',
                 'T55J5 684',
                 'KK677 28',
                 'KTJJT 220',
                 'QQQJA 483']

from collections import Counter

def classify(hand):
    c = Counter(hand[0])
    cv = c.values()
    if len(c) == 1:
        return 0#'five'
    if len(c) == 2:
        if max(cv) == 4:
            return 1#'four'
        if max(cv) == 3:
            return 2#'full'
    if len(c) == 3:
        if max(cv) == 3:
            return 3#'thre'
        if max(cv) == 2:
            return 4#'twop'
    if len(c) == 4:
        return 5#'onep'
    return 6#'highc'

mapping = {x:i for i,x in enumerate(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'])}
mapping2 = {x:i for i,x in enumerate(['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'])}

def lexsort(alist,mapping_):
    sorted_list = list(alist)
    n = len(alist[0][0])
    for i in range(n):
        #print([y[0][n-i-1] for y in alist])
        sorted_list = sorted(sorted_list,
                             key = lambda y: mapping_[y[0][n-i-1]])
        #print(sorted_list)
    return sorted_list

import itertools as it
nonJ = [x for x in mapping.keys() if x != 'J']
def replaceJ(hand):
    nJ = hand.count('J')
    iJ = [-1]
    for n in range(nJ):
        iJ.append(hand.index('J',iJ[-1]+1))
    iJ.pop(0)
                  
    replacements = it.product(nonJ, repeat=nJ)
    for repl in replacements:
        newhand = list(hand)
        for j,i in enumerate(iJ):
            newhand[i] = repl[j]
        yield ''.join(newhand)

def classify_wild(hand):
    #print(hand)
    if 'J' not in hand[0]:
        return classify(hand)
    best_rank = 999
    replaced = [(x,classify([x,None])) for x in replaceJ(hand[0])]
    #print('  ',sorted(replaced, key=lambda x:x[1]))
    return min([x[1] for x in replaced])
        
if testing:
    ranked = sorted(lexsort([x.split() for x in example_input], mapping),
                    key = lambda y: classify(y))
else:
    ranked = sorted(lexsort([x.split() for x in actual_input], mapping),
                    key = lambda y: classify(y))

winnings = 0
for x in zip(range(1,len(ranked)+1),ranked[::-1]):
    rank = x[0]
    bid = int(x[1][1])
    winnings += rank * bid
    print(x)
print('\n',winnings)

### Part 2 ###

if testing:
    #print('\n')
    #print(lexsort([x.split() for x in example_input], mapping2))
    #print('\n')
    #print([(y, classify_wild(y)) for y in lexsort([x.split() for x in example_input], mapping2)])
    #print('\n')
    ranked = sorted(lexsort([x.split() for x in example_input], mapping2),
                    key = lambda y: classify_wild(y))
else:
    ranked = sorted(lexsort([x.split() for x in actual_input], mapping2),
                    key = lambda y: classify_wild(y))

winnings = 0
for x in zip(range(1,len(ranked)+1),ranked[::-1]):
    rank = x[0]
    bid = int(x[1][1])
    winnings += rank * bid
    print(x)
print('\n',winnings)
