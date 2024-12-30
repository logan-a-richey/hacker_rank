# piling-up.py

"""
There is a horizontal row of `n` cubes. The length of each cube is given.
You need to create a new veritical pile of cubes. 

The new pile should following these directions: if cube[i] is on top of cube[j], then:
sideLength[j] >= sideLength[i].

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time.
Print "Yes" if it is possible to stack cubes. Otherwise, print "No".

e.g.
blocks = [1,2,3,8,7]
Result: "No"

After choosing the rightmost element, 7, choose the leftmost element, 1.
After that, the choices are 2 and 8.
These are both larger than the top block of size 1.

blocks = [1,2,3,7,8]
Result: "Yes"

Choose blocks from right to left in order to successfully stack the blocks. 

** Input Format:
The 1st line contains a single integer `T`, the number of test cases.
For each test cases, there are  lines.
The 1st line of each test case contains `n`, the number of cubes.
The 2nd line contains `n` space seperated integers, denoting the sideLengths of each cube in that order.

** Output Format:
For each test case, output a single line containing either "Yes" or "No"

** Sample Input:
STDIN        Function
-----        --------
2            T = 2
6            blocks[] size n = 6
4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
3            blocks[] size n = 3
1 3 2        blocks = [1, 3, 2]


** Sample Output:
Yes
No
"""

from collections import deque

def main():
    T = int(input())
    
    for _ in range(T):
        n = int(input())
        blocks = deque(map(int, input().split()))
        
        last_block = float('inf')  # Start with an infinitely large last block size
        
        possible = True
        
        while blocks:
            # If both left and right are valid choices, we pick the smaller one
            if blocks[0] <= blocks[-1] and blocks[0] <= last_block:
                last_block = blocks.popleft()  # Remove leftmost element
            elif blocks[-1] <= blocks[0] and blocks[-1] <= last_block:
                last_block = blocks.pop()  # Remove rightmost element
            else:
                possible = False
                break
        
        if possible:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()

