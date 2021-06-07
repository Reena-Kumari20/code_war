def between(a,b):
    i=a
    c=[]
    while i<=b:
        c.append(i)
        i=i+1
    return(c)
a=int(input("enter a: "))
b=int(input("enter b: "))
print(between(a,b))
    