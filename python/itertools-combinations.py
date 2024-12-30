# itertools-combinations.py

"""
** Task:
You are given a string S.
Your task is to print all possible combinations up to size k of the string in lexicographic sorted order.

** Input Format:
A single line containing the string S and int val k sep by space.

** Constraints:
0 < k < len(S)
string contains only uppercase

** Output Format
print the different combinations of S on sep lines

** Sample Input:
HACK 2

** Sample Output:
A
C
H
K
AC
AH
AK
CH
CK
HK
"""

import itertools

def main():
    S, k = input().split()
    k = int(k)
    
    # Sort the string to ensure lexicographical order
    S = ''.join(sorted(S))
    
    for size in range(1, k + 1):
        combinations = itertools.combinations(S, size)
        for comb in combinations:
            print("".join(comb))

if __name__ == "__main__":
    main()

