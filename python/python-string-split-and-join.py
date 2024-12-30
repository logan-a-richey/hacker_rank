# python-string-split-and-join.py

def split_and_join(line):
    return "-".join(line.split())

def main():
    line = input()
    res = split_and_join(line)
    print(res)

if __name__ == "__main__":
    main()

