a=("aaa","bbb","ccc")
k=0
i=0
b=" "
while k<len(a):
    i=0
    while i<len(a):
        j=0
        while j<1:
            b=b+a[i][j]
            j=j+1
        i=i+1
    k=k+1
print(b)
    
        