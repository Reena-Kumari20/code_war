'''Create a function that takes 2 positive integers in form of a string as an input, and outputs 
the sum (also as a string):

Example: (Input1, Input2 -->Output)

"4",  "5" --> "9"
"34", "5" --> "39"
Notes:

If either input is an empty string, consider it as zero.'''
def sum_str(a, b):
    if a=="" and b=="":
        return str(0)
    elif a!="" and b=="":
        return a
    elif a=="" and b!="":
        return b
    else:
        sum=int(a)+int(b)
        x=str(sum)
        y=type(x)
        return x,y
a=input("string_first:- ")
b=input("string_second:- ")
print(sum_str(a,b))