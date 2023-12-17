# Advent of Code 2023

My solutions to problems from [Advent of Code 2023](https://adventofcode.com/).

I found the wording in part 2 of problem 10 pretty unclear: "Any tile that isn't part of the main loop can count as being enclosed by the loop." What this doesn't mean is that loops in pipes that are not the main loop can count as interior points. Rather, it means we can clear out all the "junk pipe" that's not part of the main loop, and then apply the interior-exterior point algorithm to what's left.

Incidentally, the ["even-odd" rule](https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule) for calculating whether a point is interior or exterior to a closed curve is a [notoriously difficult mathematical theorem](https://en.wikipedia.org/wiki/Jordan_curve_theorem). 

Since the leaderboard is stupidly impossible to achieve, I post my [personal leaderboard](https://github.com/n-j-p/AoC2023/blob/main/Personal_leaderboard.txt).
