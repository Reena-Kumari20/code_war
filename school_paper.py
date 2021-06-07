# Beginner Series #1 School Paper
# Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.
# Your task is to calculate how many blank pages you need. If n < 0 or m < 0 return 0.
 
# ex-
# input,n= 5 
#       m=5 
#       output=25
# input,n=-5, 
#       m=5:  
#       output=0



def paperwork(n, m):
    if n<0:
        return 0
    elif m<0:
        return 0
    else:
        a=n*m
        return a
n=int(input("enter: "))
m=int(input("enter: "))
print(paperwork(n, m))
