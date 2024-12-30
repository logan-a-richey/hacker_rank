"""
HackerRank - Regex Tutorial
matching_anything_but_a_newline.py
"""

"""
TASK:

You have a test string S.
Your task is to write a regex that matches only and exactly strings of the form:
abc.def.ghi.jkx where each variable a,b,c,d,e,f,g,h,i,j,k,x can be any character
except the newline.
"""

import re
import sys

def main():
    # Matches a string with four parts of 3 characters each, separated by dots,
    # with no extra characters or newline.
    regex_pattern = r"^.{3}\..{3}\..{3}\..{3}$"
    
    test_string = input()
    match = re.match(regex_pattern, test_string) is not None
    print(str(match).lower())

if __name__ == "__main__":
    main()

