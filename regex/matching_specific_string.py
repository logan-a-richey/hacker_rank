"""
HackerRank - Regex Tutorial
matching_specific_string.py
"""

"""
TASK:
Match the exact string "hackerrank".
"""

import re

def main():
    re_p = r'hackerrank' # Do not delete 'r'. This is for designating a raw string.
    ts = input()
    m = re.findall(re_p, ts)
    print(f"Number of matches : {len(m)}")

if __name__ == "__main__":
    main()

