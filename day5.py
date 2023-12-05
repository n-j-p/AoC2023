fpath = './day5_input.txt'

example_input = ['seeds: 79 14 55 13',
                 '',
                 'seed-to-soil map:',
                 '50 98 2',
                 '52 50 48',
                 '',
                 'soil-to-fertilizer map:',
                 '0 15 37',
                 '37 52 2',
                 '39 0 15',
                 '',
                 'fertilizer-to-water map:',
                 '49 53 8',
                 '0 11 42',
                 '42 0 7',
                 '57 7 4',
                 '',
                 'water-to-light map:',
                 '88 18 7',
                 '18 25 70',
                 '',
                 'light-to-temperature map:',
                 '45 77 23',
                 '81 45 19',
                 '68 64 13',
                 '',
                 'temperature-to-humidity map:',
                 '0 69 1',
                 '1 0 69',
                 '',
                 'humidity-to-location map:',
                 '60 56 37',
                 '56 93 4']

actual_input = open(fpath).read().split('\n')[:-1]

class Map():
    def __init__(self, ranges):
        self.sources = []
        self.dests = []
        for row in ranges:
            xn = [int(xs) for xs in row.split()]
            self.dests.append((xn[0], xn[0] + xn[2]))
            self.sources.append((xn[1], xn[1] + xn[2]))
    def f(self, x):
        for dest, source in zip(self.dests, self.sources):
            if x >= source[0] and x < source[1]:
                delta = x - source[0]
                # Assume no overlap in the ranges, so we can return now
                return dest[0] + delta
        return x

#seeds = [int(x) for x in example_input[0].split(':')[1].split()]
seeds = [int(x) for x in actual_input[0].split(':')[1].split()]

# Create maps:
maps = []
#for row in example_input[2:]:
for row in actual_input[2:]:
    if 'map' in row:
        input_rows = []
        continue
    if len(row) == 0:
        maps.append(Map(input_rows))
    else:
        input_rows.append(row)
maps.append(Map(input_rows)) # Final map

lowest = 10**12
for seed in seeds:
    mapped = [seed,]
    for map in maps:
        mapped.append(map.f(mapped[-1]))

    print('Seed %d, soil %d, fertilizer %d, water %d, light %d, temperature %d, humidity %d, location %d' % tuple(mapped))
    lowest = min(lowest, mapped[-1])

print('\nlowest location =',lowest)
if lowest == 10**12:
    print('  check')

