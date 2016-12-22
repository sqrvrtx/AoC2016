
"""
--- Day 8: Two-Factor Authentication ---

You come across a door implementing what you can only assume is an
implementation of two-factor authentication after a long game of requirements
telephone.

To get past the door, you first swipe a keycard (no problem; there was one
on a nearby desk). Then, it displays a code on a little screen, and you type
that code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken
everything apart and figured out how it works. Now you just have to work out
what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for
the screen; these instructions are your puzzle input. The screen is 50 pixels
wide and 6 pixels tall, all of which start off, and is capable of three somewhat
peculiar operations:

    rect AxB turns on all of the pixels in a rectangle at the top-left of the
    screen which is A wide and B tall.

    rotate row y=A by B shifts all of the pixels in row A (0 is the top row)
    right by B pixels. Pixels that would fall off the right end appear at the
    left end of the row.

    rotate column x=A by B shifts all of the pixels in column A
    (0 is the left column) down by B pixels. Pixels that would fall
    off the bottom appear at the top of the column.

For example, here is a simple sequence on a smaller screen:

    rect 3x2 creates a small rectangle in the top-left corner:

    ###....
    ###....
    .......

    rotate column x=1 by 1 rotates the second column down by one pixel:

    #.#....
    ###....
    .#.....

    rotate row y=0 by 4 rotates the top row right by four pixels:

    ....#.#
    ###....
    .#.....

    rotate column x=1 by 1 again rotates the second column down by one pixel,
    causing the bottom pixel to wrap back to the top:

    .#..#.#
    #.#....
    .#.....

As you can see, this display technology is extremely powerful, and will soon
dominate the tiny-code-displaying-screen market. That's what the advertisement
on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display:
after you swipe your card, if the screen did work, how many pixels should be
lit?

--- Part Two ---

You notice that the screen is only capable of displaying capital letters; in
the font it uses, each letter is 5 pixels wide and 6 tall.

After you swipe your card, what code is the screen trying to display?

"""

import operator


def run(commands, height, width):

    rect = []
    for i in range(height):
        rect.append([False for x in range(width)])

    for command in commands:
        actions = command.split()
        if actions[0] == 'rect':

            # Apply rectangle
            x, y = map(int, actions[1].split('x'))
            for i in range(y):
                for j in range(x):
                    rect[i][j] = True

        elif actions[0] == 'rotate' and actions[1] == 'column':
            col_num = int(actions[2].split('=')[-1])
            factor = int(actions[4])

            unzipped = zip(*rect)
            new_col = unzipped[col_num][-factor:] + unzipped[col_num][:-factor]
            unzipped[col_num] = new_col
            rect = [list(x) for x in zip(*unzipped)]

        elif actions[0] == 'rotate' and actions[1] == 'row':
            row_num = int(actions[2].split('=')[-1])
            factor = int(actions[4])
            rect[row_num] = rect[row_num][-factor:] + rect[row_num][:-factor]

    return rect


def count_pixels(commands, height, width):
    transformed_rect = run(commands, height, width)
    for x in transformed_rect:
        for y in x:
            if y:
                print '*',
            else:
                print '-',
        print "\n"

    return sum(reduce(operator.add, transformed_rect))

# Test Case:
height = 3
width = 7

commands = [
    'rect 3x2',
    'rotate column x=1 by 1',
    'rotate row y=0 by 4',
    'rotate column x=1 by 1'
]

print count_pixels(commands, height, width)

with open('8.in', 'r') as f:
    commands1 = f.read().splitlines()

# For Real
height = 6
width = 50

print count_pixels(commands1, height, width) # not 64, 69 - too low no 72, 58
