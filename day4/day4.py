"""
--- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. Of course,
the list is encrypted and full of decoy data, but the instructions to decode the
list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes)
followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in
the encrypted name, in order, with ties broken by alphabetization. For example:

    aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters
    are a (5), b (3), and then a tie between x, y, and z, which are listed
    alphabetically.
    a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are
    all tied (1 of each), the first five are listed alphabetically.
    not-a-real-room-404[oarel] is a real room.
    totally-real-room-200[decoy] is not.

Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?

Your puzzle answer was 245102.
--- Part Two ---

With all the decoy data out of the way, it's time to decrypt this list and get
moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly
unbreakable without the right software. However, the information kiosk designers
at Easter Bunny HQ were not expecting to deal with a master cryptographer like
yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number
of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A,
and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?

Your puzzle answer was 324.

Both parts of this puzzle are complete! They provide two gold stars: **

At this point, you should return to your advent calendar and try another puzzle.
"""

import re

from collections import Counter

with open('4.in', 'r') as f:
    ls = f.read().splitlines()

real_num = 0

for line in ls:
    txt, num, grp = re.search(r'(.*)-(\d+)\[(.*)\]', line).groups()

    # remove '-' from txt
    txt = filter(lambda x: x != '-', txt)
    most_common = Counter(txt).most_common()

    # Sort by highest num firdt, then 'lowest' letter
    res = sorted(most_common, key=lambda x:(-x[1],x[0]))[:5]

    # Convert list ['a','b','c'] to 'abc'
    gen_grp = ''.join([x[0] for x in res])
    if gen_grp == grp:
        real_num  += int(num)

# 245102
print real_num

# part 2
def calc(txt, forward_factor):
    retn_words = ""
    word_list = txt.split('-')
    for word in word_list:
        new_word = ''
        for letter in word:
            forward_val = (ord(letter) - 97) + int(forward_factor)
            new_word +=  chr(forward_val%26 + 97)

        retn_words += new_word + " "

    return retn_words.strip()


assert calc('qzmt-zixmtkozy-ivhz', '343') == 'very encrypted name'


for line in ls:
    txt, num, grp = re.search(r'(.*)-(\d+)\[(.*)\]', line).groups()
    if calc(txt, num) == 'northpole object storage':
        print 'northpole object storage', num
