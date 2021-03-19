def descending_order(num):
    a=str(num)
    b=" "
    i=1
    while i<=len(a):
        b=b+a[-i]
        i=i+1
    return (int(b))
num=input("enter the number: ")
print(descending_order(num))