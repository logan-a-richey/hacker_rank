# python-integers-come-in-all-sizes.py

"""
Print the following number tree using at most 2 print statements and no string methods

** Sample Input:
5

** Sample Output:
1
22
333
4444
"""

"""
def gi():
    return int(input())

N = gi()

#build string
lst = []
for i in range(N):
    val = 0
    for j in range(i):
        val += i + 10**i
    lst.append(val)

print("\n".join(lst))
"""

# only using 2 lines of code:
for i in range(1, int(input())): 
    print((10**i // 9) * i)
