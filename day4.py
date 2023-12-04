fpath = './day4_input.txt'

c = 0

for line in open(fpath).read().split('\n'):
    if len(line) == 0:
        break
    print(line)
    pre, nums = line.split(':')
    winners, actual = nums.split('|')
    wnum = [int(x) for x in winners.split()]
    nums = [int(x) for x in actual.split()]
    winning_numbers = set(wnum).intersection(nums)
    if len(winning_numbers) == 0:
        score = 0
    else:
        score = 2**(len(winning_numbers)-1)
    print(f'  {len(winning_numbers)} numbers: score = {score}')
    c += score
print('\n',c)
