#!/usr/bin/python3
# py-collections-namedtuple.py

"""
## TEST 01:
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   

RESULT 01:
78.00

## TEST 02:
5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5

RESULT 02:
81.00
"""

from collections import namedtuple

N = int(input())  # Number of entries

Student = namedtuple('Student', input().split())

total_marks = 0

for _ in range(N):
    student_data = input().split()
    student = Student(*student_data)
    total_marks += int(student.MARKS)

average_marks = total_marks / N
print(f"{average_marks:.2f}")






