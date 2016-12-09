"""
Day 7
=====

--- Day 7: Internet Protocol Version 7 ---

While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited).
You'd like to figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA.
An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair,
such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

For example:

    abba[mnop]qrst supports TLS (abba outside square brackets).
    abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
    aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
    ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).

How many IPs in your puzzle input support TLS?
"""

p = lambda s: s == s[::-1] if s[0] != s[1] else False

palindrome = lambda t: any([p(t[i:i+4]) for i in range(len(t)-3)])

tc1 =  "abba"
tc2 = "abcd"
tc3 = "aaaa"
tc4 = "ioxxoj"

assert palindrome(tc1)
assert not palindrome(tc2)
assert not palindrome(tc3)
assert palindrome(tc4)

import re

tc5 = 'abba[mnop]qrst' # supports TLS (abba outside square brackets).
tc6 = 'abcd[bddb]xyyx' # does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
tc7 = 'aaaa[qwer]tyui' # does not support TLS (aaaa is invalid; the interior characters must be different).
tc8 = 'ioxxoj[asdfgh]zxcvbn' # supports TLS (oxxo is outside square brackets, even though it's within a larger string).


def process_result(ls):
    result = []
    for z in ls:
        res =  re.split(r'(\[\w+\])', z )

        res1 = any([palindrome(x) for x in res if not x.startswith('[')])
        res2 = any([palindrome(x) for x in res if x.startswith('[')])
        if res1 - res2 == 1:
            result.append(z)

    return len(result)

ls = [tc5, tc6, tc7, tc8]
print process_result(ls)

with open('input.txt', 'r') as f:
    ls = f.read().splitlines()

print process_result(ls)

tc10 = 'aba[bab]xyz' # supports SSL (aba outside square brackets with corresponding bab within square brackets).
tc11 = 'xyx[xyx]xyx'  # does not support SSL (xyx, but no corresponding yxy).
tc12 = 'aaa[kek]eke' # supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
tc13 = 'zazbz[bzb]cdb' # supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
f = lambda x: x[1]+x[0]+x[1]

def process_result2(ls):
    count = 0
    result = []
    for z in ls:

        res =  re.split(r'(\[\w+\])', z )

        # need to loop every 3
        if any(set([f(res[i:i+2]) for i in range(len(res)-2)]) & set(filter(lambda x: x.startswith('['), res))):
            count+=1
    return count
ls = [tc10, tc11, tc12, tc13]
print process_result2(ls)
