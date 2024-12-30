# python-quest-1.py

def gi():
    return int(input())

N = gi()

#build string
bs = ""
for i in range(N):
    for j in range(i):
        bs += f"{i}"
    bs += "\n"

print(bs)

