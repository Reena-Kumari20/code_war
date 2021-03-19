#In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.

#For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.

#Your function will be tested with pre-made examples as well as random ones.

#If you can, try writing it in one line of code.

def defference(a,b):
    i=0
    vol1=1
    vol2=1
    while i<len(a):
        vol1=vol1*a[i]
        vol2=vol2*b[i]
        i=i+1
    if vol1>vol2:
        x=vol1-vol2
        return(x)
    elif vol2>vol1:
        y=vol2-vol1
        return(y)
a=[3,2,5]
b=[1,4,4]
c=defference(a,b)
print(c)