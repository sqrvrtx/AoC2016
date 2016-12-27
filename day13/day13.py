"""
--- Day 13: A Maze of Twisty Little Cubicles ---

You arrive at the first floor of this new building to discover a much less
welcoming environment than the shiny atrium of the last one. Instead, you are
in a maze of twisty little cubicles, all alike.

Every location in this area is addressed by a pair of non-negative integers
(x,y). Each such coordinate is either a wall or an open space. You can't move
diagonally. The cube maze starts at 0,0 and seems to extend infinitely toward
positive x and y; negative values are invalid, as they represent a location
outside the building. You are in a small waiting area at 1,1.

While it seems chaotic, a nearby morale-boosting poster explains, the layout is
actually quite logical. You can determine whether a given x,y coordinate will
be a wall or an open space using a simple system:

    Find x*x + 3*x + 2*x*y + y + y*y.
    Add the office designer's favorite number (your puzzle input).
    Find the binary representation of that sum; count the number of bits that
    are 1.
        If the number of bits that are 1 is even, it's an open space.
        If the number of bits that are 1 is odd, it's a wall.

For example, if the office designer's favorite number were 10, drawing walls
as # and open spaces as ., the corner of the building containing 0,0 would
look like this:

  0123456789
0 .#.####.##
1 ..#..#...#
2 #....##...
3 ###.#.###.
4 .##..#..#.
5 ..##....#.
6 #...##.###

Now, suppose you wanted to reach 7,4. The shortest route you could take
is marked as O:

  0123456789
0 .#.####.##
1 .O#..#...#
2 #OOO.##...
3 ###O#.###.
4 .##OO#OO#.
5 ..##OOO.#.
6 #...##.###

Thus, reaching 7,4 would take a minimum of 11 steps (starting from your
current location, 1,1).

What is the fewest number of steps required for you to reach 31,39?

Your puzzle input is 1358.

--- Part Two ---

How many locations (distinct x,y coordinates, including your starting location)
can you reach in at most 50 steps?

"""

is_wall = lambda x, y, z: (bin(x*x + 3*x + 2*x*y + y + y*y + z)).count('1')%2


def get_moves(x, y, fav_num, visited):
    moves = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    return [(x, y) for (x, y) in moves if x >= 0 and \
            y >= 0 and (x, y) not in visited and \
            not is_wall(x,y,fav_num)]

def process(fav_num, start, target, max_steps=None):

    result = None
    visited = {start}
    new_coords = visited.copy()
    steps=0

    while True:
        new_pos = new_coords.copy()
        for x, y in new_pos:
            for px, py in get_moves(x, y, fav_num, visited):
                new_coords.add((px,py))
                visited.add((px,py))

        steps +=1

        if target in visited and not max_steps:
            result = steps
            break
        elif max_steps and steps == max_steps:
            result = len(visited)
            break

    return result

print process(10, start=(1,1), target=(7,4))
print process(1358, start=(1,1), target=(31,39))
print process(1358, start=(1,1), target=(31,39), max_steps=50)

assert process(10, start=(1,1), target=(7,4)) == 11
assert process(1358, start=(1,1), target=(31,39)) == 96
assert process(1358, start=(1,1), target=(31,39), max_steps=50) == 141
