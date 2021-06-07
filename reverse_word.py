'''[10:19 am, 10/05/2021] REENA KUMARI: Complete the solution so that it reverses all of the words within the string passed in.

Example:

"The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"
[10:19 am, 10/05/2021] REENA KUMARI:'''


def reverse_words(s):
    a=s.split(" ")
    l=len(a)
    b=[]
    i=1
    while i<=l:
        s=""
        b.append(a[-i])
        m=a[-i]
        s=s+m
        i=i+1
        print(s,end=" ")
string=input("Enter the string--> ")
reverse_words(string)