# Pre-FizzBuzz Workout 
# This is the first step to understanding FizzBuzz.
# Your inputs: a positive integer, n, greater than or equal to one. n is provided, you have NO CONTROL over its value.
# Your expected output is an array of positive integers from 1 to n (inclusive).
# Your job is to write an algorithm that gets you from the input to the output.
def pre_fizz(n):
    a=[ ]
    i=1
    while i<=n:
        a.append(i)
        i=i+1
    return(a)
n=int(input("Enter the number: "))
print(pre_fizz(n))
