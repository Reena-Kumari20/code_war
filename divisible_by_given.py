# Find numbers which are divisible by given number
# Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. First argument is an array of numbers and the second is the divisor.
# divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]


def divisible_by(numbers, divisor):
    i=0
    list1=[]
    while i<len(numbers):
        if numbers[i]%divisor==0:
            list1.append(numbers[i])
        i=i+1
    return list1
list1=[1,2,4,2,6,4,8,5,42,7,8]
divisor=int(input("enter the divisor: "))
print(divisible_by(list1, divisor))
