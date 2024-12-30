# iterables-and-iterators.py

"""
The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python. 

You are given a list of N lowercase English letters.
For a given int K, you can select any K indices (assume 1-based indexing) with a uniform probabilty from the list.

** Input Format:
The input consists of three lines. The first line contains the integer N, denoting the len of the list.
The next line consists of N space-sep lowercase English letters, denoting the elements of the list.
The 3rd and last line of input contains the int K, denoting the number of indices to be selected.

** Output Format:
Output a single line consisting of the probabilty that at least one of the K indices selected contains the letter: 'a'.

** Sample Input:
4 
a a c d
2

** Sample Output:
0.8333
"""

import itertools

def main():
    N = int(input())
    letters = input().split()
    K = int(input())
    
    total_combinations = list(itertools.combinations(letters, K))
    favorable_combinations = [comb for comb in total_combinations if 'a' in comb]
    
    probability = len(favorable_combinations) / len(total_combinations)
    print(f"{probability:.4f}")

if __name__ == "__main__":
    main()

