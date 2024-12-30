# compress-the-string.py

"""
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools.

You are given a string S. Suppose a character 'c' occurs consecutively X times in the string.
Replace these consecutive occurances of the character 'c' with (X, c) in the string.

** Input Format
A single line of input consisting of the string S.

** Output Format
A single line of output consisting of the modified string.

** Sample Input
1222311

** Sample Out
(1, 1) (3, 2) (1, 3) (2, 1)

** Hint
First the char 1 occurs only once. It is replaced be (1, 1).
Then the char 2 occurs 3 times, and it is replaced by (3, 2) and so on.
Also note the single space within each compression and between the compressions.

"""

import itertools

def main():
    S = input()
    
    # Use groupby to group consecutive characters in the string
    result = [(len(list(group)), key) for key, group in itertools.groupby(S)]
    
    # Print the results as requested in the format "(X, c)"
    print(" ".join(f"({x}, {y})" for x, y in result))

if __name__ == "__main__":
    main()

