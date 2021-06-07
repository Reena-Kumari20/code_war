'''[9:26 am, 10/05/2021] REENA KUMARI: Complete the function that takes a non-negative 
integer n as input, and returns a list of all the powers of 2 with the exponent ranging 
from 0 to n (inclusive).

Examples
n = 0  ==> [1]        # [2^0]
n = 1  ==> [1, 2]     # [2^0, 2^1]
n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]
[9:26 am, 10/05/2021] REENA KUMARI: '''

def powers_of_two(n):
    list1=[]
    i=0
    while i<=n:
        a=2**i
        list1.append(a)
        i=i+1
    return list1
n=int(input("enter the number--> "))
print(powers_of_two(n))