# python-mod-divmod.py

def gi():
    return int(input())

def main():
    a = gi()
    b = gi()
    dm = divmod(a,b)
    print(dm[0])
    print(dm[1])
    print(dm)
    
    return None

if __name__ == "__main__":
    main()
