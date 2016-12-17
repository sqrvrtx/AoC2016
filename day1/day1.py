"""
--- Day 1: No Time for a Taxicab ---

Santa's sleigh uses a very high-precision clock to guide its movements, and the
clock's oscillator is regulated by stars. Unfortunately, the stars have been
stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve
all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each
day in the advent calendar; the second puzzle is unlocked when you complete the
first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near",
unfortunately, is as close as you can get - the instructions on the Easter Bunny
Recruiting Document the Elves intercepted start here, and nobody had time to
work them out further.

The Document indicates that you should start at the given coordinates (where
you just landed) and face North. Then, follow the provided sequence: either turn
left (L) or right (R) 90 degrees, then walk forward the given number of blocks,
ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you
take a moment and work out the destination. Given that you can only walk on the
street grid of the city, how far is the shortest path to the destination?

For example:

    Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks
    away.
    R2, R2, R2 leaves you 2 blocks due South of your starting position, which is
    2 blocks away.
    R5, L5, R5, R3 leaves you 12 blocks away.

How many blocks away is Easter Bunny HQ?

Your puzzle answer was 236.

--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting
Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you
visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?

Your puzzle answer was 182.

Both parts of this puzzle are complete! They provide two gold stars: **

At this point, you should return to your advent calendar and try another puzzle.

"""

ts1 = "R2, L3"
ts2 = "R2, R2, R2"
ts3 = "R5, L5, R5, R3"

with open('data.txt', 'r') as f:
    input_s = f.read()

# Part 1: 236
path = [(0, 0)]
def calc(input_str):
    input_ls = [x.strip() for x in input_str.split(',')]

    x = y = 0
    heading = 0

    for val in input_ls:

        direction, steps = val[0], int(val[1:])

        if direction == 'L':
            heading = (heading + 1) % 4
        else:
            heading = (heading - 1) % 4

        for i in range(steps):
            if heading == 0:
                y += 1
            elif heading == 1:
                x += 1
            elif heading == 2:
                y -= 1
            elif heading == 3:
                x -= 1
            if path is not None:
                path.append((x, y))

    coord = ((x,y))

    return sum([abs(x) for x in coord])

assert calc(ts1) == 5, calc(ts1)
assert calc(ts2) == 2
assert calc(ts3) == 12, calc(ts3)

# Part 2: 182
path = [(0, 0)]
print calc(input_s)
n_path = []
for coord in path:
    if coord in n_path:
        print "Returned:", sum([abs(x) for x in coord])
        break
    else:
        n_path.append(coord)
