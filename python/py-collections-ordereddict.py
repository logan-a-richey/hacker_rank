#!/usr/bin/python3
# py-collections-ordereddict.py

"""
# INPUT
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

# OUTPUT
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
"""

from collections import OrderedDict

def main():
    d = OrderedDict()

    N = int(input())

    for _ in range(N):
        data = input()
        res = data.rsplit(" ", 1)
        k, v = res[0], int(res[1])
        d[k] = d.get(k, 0) + v
        
    for k, v in d.items():
        print("{} {}".format(k, v))

if __name__ == "__main__":
    main()

