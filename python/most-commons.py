# most-commons.py

"""
** Input Format
A single line of input containing the string S.
3 < len(S) < 10**4
S has at least 3 different characters

** Output Format
Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order. 

** Sample Input 
aabbbccde

** Sample Output
b 3
a 2
c 2
"""

from collections import Counter

# gpt method
def main():
    s = input()
    
    # Count the frequency of each character using Counter
    counter = Counter(s)
    
    # Sort the items: first by frequency (descending), then by character (ascending)
    sorted_counts = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    
    # Print the top 3 characters with their frequencies
    for i in range(3):
        print(sorted_counts[i][0], sorted_counts[i][1])
    
    return None

"""
# my method
def main():
    s = input()
    d = {}
    
    # get the frequency of each character
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    
    # sort the dictionary
    sorted_items = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    
    # print the 3 most frequent characters and their frequency
    for i in range(3):
        print(sorted_items[i][0], sorted_items[i][1])
    
    return None
"""

if __name__ == "__main__":
    main()
