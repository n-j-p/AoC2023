fpath = './day4_input.txt'

c = 0

scores = {}
copies = {}
card = 1
for line in open(fpath).read().split('\n'):
    if len(line) == 0:
        break
    print(line)
    if card not in copies:
        copies[card] = 0
    pre, nums = line.split(':')
    winners, actual = nums.split('|')
    wnum = [int(x) for x in winners.split()]
    nums = [int(x) for x in actual.split()]
    winning_numbers = set(wnum).intersection(nums)
    original_score = len(winning_numbers)
    print(f'  {original_score} matching numbers, multiplier = {copies[card]+1}')
    for i in range(original_score):
        try:
            copies[card + i + 1] += copies[card] + 1
        except KeyError:
            copies[card + i + 1] = copies[card] + 1
    print('  ',copies)

    card += 1


print('\n',sum(copies.values()) + card-1)
