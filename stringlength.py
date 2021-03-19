a=("navgurukul banglore campus hkdfcolidhfcpaeiwhfpwehfpwehfpwie reenakumari hkhkfsjfoiwuffhkieh")
b=a.split()
print(b)

i=0
length=0
c=0
while i<len(b):
    if len(b[i])>length:
        length=len(b[i])
        c=i
    i=i+1
print(b[c])
print(length)

#in function 

def find_longest(string):
    spl = string.split(" ")
    longest = 0
    i=0
    while i<len(spl):
        if len(spl[i])>longest: 
            longest=len(spl[i])
        i=i+1
    return longest
string=("my name is reena kumari")
a=find_longest(string)
print(a)


#IN FOR LOOP
def find_longest(string):
     
    longest_list = string.split(' ')
    longest = len(longest_list.pop(0))
    for n in longest_list:
        if len(n) > longest:
            longest = len(n)
    return longest
