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

def lexsort(alist):
    sorted_list = list(alist)
    n = len(alist[0][0])
    for i in range(n):
        print([y[0][n-i-1] for y in alist])
        sorted_list = sorted(sorted_list,
                             key = lambda y: mapping[y[0][n-i-1]])
        print(sorted_list)
    return sorted_list

if testing:
    ranked = sorted(lexsort([x.split() for x in example_input]),
                    key = lambda y: classify(y))
else:
    ranked = sorted(lexsort([x.split() for x in actual_input]),
                    key = lambda y: classify(y))

winnings = 0
for x in zip(range(1,len(ranked)+1),ranked[::-1]):
    rank = x[0]
    bid = int(x[1][1])
    winnings += rank * bid
    print(x)
print('\n',winnings)
