"""
--- Day 18: Like a Rogue ---

As you enter this room, you hear a loud click! Some of the tiles in the floor
here seem to be pressure plates for traps, and the trap you just triggered has
run out of... whatever it tried to do to you. You doubt you'll be so lucky next
time.

Upon closer examination, the traps and safe tiles in this room seem to follow a
pattern. The tiles are arranged into rows that are all the same width; you take
note of the safe tiles (.) and traps (^) in the first row (your puzzle input).

The type of tile (trapped or safe) in each row is based on the types of the
tiles in the same position, and to either side of that position, in the
previous row. (If either side is off either end of the row, it counts as
"safe" because there isn't a trap embedded in the wall.)

For example, suppose you know the first row (with tiles marked by letters) and
want to determine the next row (with tiles marked by numbers):

ABCDE
12345

The type of tile 2 is based on the types of tiles A, B, and C; the type of tile
5 is based on tiles D, E, and an imaginary "safe" tile. Let's call these three
tiles from the previous row the left, center, and right tiles, respectively.
Then, a new tile is a trap only in one of the following situations:

    Its left and center tiles are traps, but its right tile is not.
    Its center and right tiles are traps, but its left tile is not.
    Only its left tile is a trap.
    Only its right tile is a trap.

In any other situation, the new tile is safe.

Then, starting with the row ..^^., you can determine the next row by applying
those rules to each new tile:

    The leftmost character on the next row considers the left (nonexistent, so
    we assume "safe"), center (the first ., which means "safe"), and right
    (the second ., also "safe") tiles on the previous row. Because all of the
    trap rules require a trap in at least one of the previous three tiles, the
    first tile on this new row is also safe, ..

    The second character on the next row considers its left (.), center (.),
     and right (^) tiles from the previous row. This matches the fourth rule:
     only the right tile is a trap. Therefore, the next tile in this new row is
     a trap, ^.

    The third character considers .^^, which matches the second trap rule: its
    center and right tiles are traps, but its left tile is not. Therefore,
    this tile is also a trap, ^.

    The last two characters in this new row match the first and third rules,
    respectively, and so they are both also traps, ^.

After these steps, we now know the next row of tiles in the room: .^^^^. Then,
we continue on to the next row, using the same rules, and get ^^..^. After
determining two new rows, our map looks like this:

..^^.
.^^^^
^^..^

Here's a larger example with ten tiles per row and ten rows:

.^^.^.^^^^
^^^...^..^
^.^^.^.^^.
..^^...^^^
.^^^^.^^.^
^^..^.^^..
^^^^..^^^.
^..^^^^.^^
.^^^..^.^^
^^.^^^..^^

In ten rows, this larger example has 38 safe tiles.

Starting with the map in your puzzle input, in a total of 40 rows (including
the starting row), how many safe tiles are there?

--- Part Two ---

How many safe tiles are there in a total of 400000 rows?

"""


class Tile(object):

    val = None

    def __init__(self, val):
        self.val = val

    @staticmethod
    def checkTile(left, middle, right):
        """
            Its left and center tiles are traps, but its right tile is not.
            Its center and right tiles are traps, but its left tile is not.
            Only its left tile is a trap.
            Only its right tile is a trap.
        """

        return any([
            middle == left == True and right == False,
            middle == right == True and left == False,
            left == True and middle == right == False,
            right == True and middle == left == False
        ])

    def __eq__(self, other):
        return self.val == other

    def __repr__(self):
        return "^" if self.val else "."



class TrapTile(Tile):

    def __init__(self):
        self.val = True

    def __repr__(self):
        return "^"


class SafeTile(Tile):

    def __init__(self):
        self.val = False

    def __repr__(self):
        return "."


class Row(object):

    def process(self, row_to_process, row_len):
        self.row = []
        row_to_process = row_to_process

        # First Tile
        left, middle, right  = SafeTile(), row_to_process[0], row_to_process[1]
        _tile = Tile.checkTile(left, middle, right)
        self.row.append(Tile(_tile))

        for i in xrange(1,row_len-1):
            left, middle, right  = row_to_process[i-1], row_to_process[i], row_to_process[i + 1]
            _tile = Tile.checkTile(left, middle, right)
            self.row.append(Tile(_tile))

        # LAST Tile
        left, middle, right  = row_to_process[-2], row_to_process[-1], SafeTile()
        _tile = Tile.checkTile(left, middle, right)
        self.row.append(Tile(_tile))

        return row_len - sum(x.val for x in self.row)

class StartRow(Row):

    def __init__(self, row_str):
        self.row = []
        for tile in row_str:
            self.row.append(self.process_char(tile))

    def process_char(self, char):
        return SafeTile() if char == '.' else TrapTile()

    def count_start_row(self):
        return len(self.row) - sum(x.val for x in self.row)


class Room(object):

    def __init__(self, starter_row_str, total_tiles):
        self.rows = []
        self.total_tiles = total_tiles
        self.rows.append(StartRow(starter_row_str).row)

        cols = len(starter_row_str)
        num_rows = total_tiles/cols

        for i in xrange(num_rows-1):
            row = Row()
            row.process(self.rows[i], cols)
            self.rows.append(row.row)

    def print_room(self):
        for row in self.rows:
            print ''.join([str(x) for x in row])

    def count_tiles(self):
        return self.total_tiles - sum(y.val for x in self.rows for y in x)


from collections import deque



class QuickRow(object):


    d = {
        "..^": True,
        "...": False,
        ".^^": True,
        ".^.": False,
        "...": False,
        "^^^": False,
        "^^.": True,
        "^..": True,
        "^.^": False
    }

    def process(self, row_to_process, row_len):
        #self.row = []
        count = 0
        tile_str=''

        # First Tile
        left, middle, right  = '.', row_to_process[0], row_to_process[1]
        tile = (self.d[''.join([left, middle, right])])
        count += int(tile)
        tile_str += '^' if tile else '.'

        for i in xrange(1,row_len-1):
            left, middle, right  = row_to_process[i-1], row_to_process[i], row_to_process[i + 1]
            tile = (self.d[''.join([left, middle, right])])
            count += int(tile)
            tile_str += '^' if tile else '.'

        # LAST Tile
        left, middle, right  = row_to_process[-2], row_to_process[-1], '.'
        tile = (self.d[''.join([left, middle, right])])
        count += int(tile)
        tile_str += '^' if tile else '.'

        return tile_str, count


class QuickStartRow(Row):
    def __init__(self, row_str):
        self.row = []
        for tile in row_str:
            self.row.append(tile)

    def process_char(self, char):
        return SafeTile() if char == '.' else TrapTile()

    def count_start_row(self):
        return len(self.row) - sum(x for x in self.row)

class RoomQuick(object):

    def __init__(self, starter_row_str, total_tiles):
        self.rows = deque([])
        self.count = 0
        self.total_tiles = total_tiles
        self.rows.append(starter_row_str)
        self.draw_str = starter_row_str + '\n'
        cols = len(starter_row_str)
        num_rows = total_tiles/cols
        self.count = starter_row_str.count('.')
        row = QuickRow()
        while num_rows > 1:
            tile_str, tile_count = row.process(self.rows.popleft(), cols)
            self.rows.append(tile_str)
            self.count += cols-tile_count
            self.draw_str += tile_str + '\n'
            num_rows -= 1

    def count_tiles(self):
        return self.count

    def print_room(self):
        print self.draw_str


# 15 tiles
startrow_str = '..^^.'

# Create room
room = Room(startrow_str, 15)
room.print_room()
print room.count_tiles()  # 6

# Create room
room = RoomQuick(startrow_str, 15)
room.print_room()
print room.count_tiles()  # 6

# 100 tiles
startrow_str = '.^^.^.^^^^'

# Create room
room100 = RoomQuick(startrow_str, 100)
#room100.print_room()
print room100.count_tiles()  # 38

# 4000 tiles
startrow_str = "......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^.."

# Create room
room4000 = RoomQuick(startrow_str, 4000)
print room4000.count_tiles()  # 1963


# Create room
room4m = RoomQuick(startrow_str, 40000000)
print room4m.count_tiles()  # 20009568
