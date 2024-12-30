# itertools-permutations.py

"""
** Task:
You are given a string S
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

** Input Format
A single line containing the space-separated string S and the int val k.

** Constraints:
0 < k <= len(S)
The string contains only UPPERCASE chars

** Output Format:
Print the permutaions of the string S on separate lines.

** Sample Input:
HACK 2

** Sample Output:
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
"""

import itertools

def main():
    S, k = input().split()
    k = int(k)
    
    permutations = sorted(itertools.permutations(S, k))
    
    for perm in permutations:
        print("".join(perm))

if __name__ == "__main__":
    main()

