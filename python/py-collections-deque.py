# py-collections-deque.py

"""
** Task:
Perform append, pop, popleft and appendleft methods on an empty deque `d`.

** Input Format:
The first line contains an integer `N`, the number of operations.
The next `N` lines contains the space separated names of methods and their values.

** Output Format
Print the space separated elements of deque `d`.

** Sample Input
6
append 1
append 2
append 3
appendleft 4
pop
popleft

** Sample Output
1 2
"""

from collections import deque

def main():
    N = int(input())
    d = deque()
    for _ in range(N):
        cmd, *args = input().split()
        if cmd == "print":
            print(d)
        else:
            getattr(d, cmd)(*map(int, args))
    print(*d)

if __name__ == "__main__":
    main()


