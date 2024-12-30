# python-tuples.py

def main():
    n = int(input())
    int_list = map(int,input().split())
    t = tuple(int_list)
    print(hash(t))

if __name__ == "__main__":
    main()



