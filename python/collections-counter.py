#!/usr/bin/python3
# collections-counter.py
"""
cat collections-counter-input.txt | ./collections-counter.py 
./collections-counter.py < collections-counter-input.txt 
"""

"""
Bob is a shop owner. He has `X` number of shoes.
There are `N` nmber of customers who are willing to pay `xi` amount of money onley if they get the shoe of their desired size.
Calc the amount that Bob earned.
"""

from collections import Counter

def main():
    X = int(input()) # number of shoes
    shoe_sizes = map(int, input().split())
    """
    stock = {}
    for i in range(2,21):
        stock[i] = 0
    for s in shoe_sizes:
        if s in stock:
            stock[s] += 1
    """
    stock = Counter(shoe_sizes)

    N = int(input()) # number of customers
    
    total_sales = 0
    for i in range(N):
        customer_desired_size, shoe_price = map(int, input().split())
        if customer_desired_size in stock:
            if stock[customer_desired_size] <= 0:
                continue
            # if we have it:
            total_sales += shoe_price
            stock[customer_desired_size] -= 1

    print(total_sales)
    pass

if __name__ == "__main__":
    main()

