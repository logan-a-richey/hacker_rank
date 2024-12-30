# python-lists.py

"""
** Sample Input:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

** Sample Output:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""

def main():
    N = int(input())
    lst = []
    for _ in range(N):
        cmd, *args = input().split()
        if cmd == "print":
            print(lst)
        else:
            getattr(lst, cmd)(*map(int, args))

if __name__ == "__main__":
    main()
