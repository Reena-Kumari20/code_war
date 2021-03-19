def func(list):
    x=[]
    i=0
    while i<len(list):
        if list[i]%2!=0:
            x.append(list[i])
        i=i+1
    return x
list=[2,7,8,6,9,4,3]
print(func(list))