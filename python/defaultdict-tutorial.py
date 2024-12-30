#!/usr/bin/python3
# defaultdict-tutorial.py

"""
Input:
5 2
a
a
b
a
b
a
b

Output:
1 2 4
3 5
"""

input_n, input_m = map(int, input().split())

d = {}

# Process input and queries in a single loop
for i in range(input_n + input_m):
    res = input()
    
    if i < input_n:
        # Collecting the input data
        if res not in d:
            d[res] = []
        d[res].append(i + 1)
    else:
        # Processing the query part
        if res in d:
            print(*d[res])
        else:
            print(-1)

