# maximize-it.py

import itertools

"""
** Input Format:
The first line contains 2 space separated integers K and M. 
The next K lines each contain an integer Ni, denoting the number of elements in the ith list, 
followed by Ni space separated integers denoting the elements in the list.

** Output Format:
Output a single integer denoting the value Smax.

** Sample Input:
3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 

** Sample Output:
206
"""

import itertools

def main():
    K, M = map(int, input().split())
    lists = [list(map(int, input().split()))[1:] for _ in range(K)]
    
    max_value = 0
    for combo in itertools.product(*lists):
        value = sum(x**2 for x in combo) % M
        max_value = max(max_value, value)
    
    print(max_value)

if __name__ == "__main__":
    main()
