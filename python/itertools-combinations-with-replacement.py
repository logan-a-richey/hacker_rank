# itertools-combinations-with-replacement.py

import itertools

def main():
    S, k = input().split()
    k = int(k)
    
    # sort to ensure lexicographical order
    S = ''.join(sorted(S))
    
    combinations = itertools.combinations_with_replacement(S, k)
    
    for comb in combinations:
        print("".join(comb))

if __name__ == "__main__":
    main()
