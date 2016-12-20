"""
--- Day 20: Firewall Rules ---

You'd like to set up a small hidden computer here so you can use it to get back
into the network later. However, the corporate firewall only allows
communication with certain external IP addresses.

You've retrieved the list of blocked IPs from the firewall, but the list seems
to be messy and poorly maintained, and it's not clear which IPs are allowed.
Also, rather than being written in dot-decimal notation, they are written as
plain 32-bit integers, which can have any value from 0 through 4294967295,
inclusive.

For example, suppose only the values 0 through 9 were valid, and that you
retrieved the following blacklist:

5-8
0-2
4-7

The blacklist specifies ranges of IPs (inclusive of both the start and end
value) that are not allowed. Then, the only IPs that this firewall allows are
3 and 9, since those are the only numbers not in any range.

Given the list of blocked IPs you retrieved from the firewall (your puzzle
input), what is the lowest-valued IP that is not blocked?

--- Part Two ---
How many IPs are allowed by the blacklist?
"""

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()


def main(my_range, ls, first_result=True):

    nls = sorted(map(int, x.split('-')) for x in ls)

    count = 0
    occurs = 0

    while count <= 4294967295:

        for x, y in nls:
            if (x <= count <= y):

                # Skip ahead - we know count->y is no good
                count = y + 1
                continue

        if first_result:
            return count

        occurs += 1
        count += 1

    return occurs
    
# Part 1
print main(4294967296, lines)  # 31053880

# Part 2
print main(4294967296, lines, first_result=False)  # 118
