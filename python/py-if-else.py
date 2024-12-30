# HackerRank
# py-if-else.py

"""
Task: Given an int n:
    if n is odd, print "Weird"
    if n is even and in the range [2,5] print "Not Weird"
    if n is even and in the range [6,20] print "Weird"
    if n is even and greater than 20, print "Not Weird"
"""

def main():
    n = int(input())

    # Check for "Weird" or "Not Weird"
    if n % 2 == 1:
        # Odd numbers are always "Weird"
        print("Weird")
    else:
        # Even numbers in the range [2, 5]
        if 2 <= n <= 5:
            print("Not Weird")
        # Even numbers in the range [6, 20]
        elif 6 <= n <= 20:
            print("Weird")
        # Even numbers greater than 20
        else:  
            print("Not Weird")

if __name__ == "__main__":
    main()
