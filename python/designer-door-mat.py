# designer-door-mat.py

"""
Size: 7 x 21 
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------

Size: 11 x 33
---------------.|.---------------
------------.|..|..|.------------
---------.|..|..|..|..|.---------
------.|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|.---
-------------WELCOME-------------
---.|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|.------
---------.|..|..|..|..|.---------
------------.|..|..|.------------
---------------.|.---------------
"""

def main():
    # get input
    n, m = map(int,input().split())

    # error checking
    if n % 2==0:
        raise ValueError("N needs to be odd.")
    if m != 3*n:
        raise ValueError("M needs to be 3 times N")
    msg = "WELCOME"

    # print the doormat (top)
    for i in range(n//2):
        j = int((2*i)+1)
        print(('.|.'*j).center(m, '-'))
    print('WELCOME'.center(m,'-'))

    # print the doormat (bottom)
    for i in reversed(range(n//2)):
        j = int((2*i)+1)
        print(('.|.'*j).center(m, '-'))
    
    return None

if __name__ == "__main__":
    main()

