# Evens times last
# Given a sequence of integers, return the sum of all the integers that have an even index,
#  multiplied by the integer at the last index.
# Indices in sequence start from 0.
# If the sequence is empty, you should return 0.

def even_last(numbers): 
    if numbers==[]:
        return 0
    else:
        i=0
        sum=0
        while i<len(numbers):
            if numbers[i]%2==0:
                sum=sum+numbers[i]
            i=i+1
        a=sum*numbers[-1]
        return a
numbers=[1,2,3,45,6,8,12,5,9,32,20,14,6,8]
print(even_last(numbers))
