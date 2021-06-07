# Is there a vowel in there?
# Given an array of numbers, check if any of the numbers are the character codes for lowercase vowels (a, e, i, o, u).
# If they are, change the array value to a string of that vowel.
# Return the resulting array.


def is_vow(inp):
    i=0
    list1=[]
    while i<len(inp):
        if str(inp[i]).isalpha():
            a=ord(inp[i])
            list1.append(a)
        else:
            list1.append(inp[i])
        i=i+1
    return list1
list1=[1,34,112,116,117,"e",56,"a"]
print(is_vow(list1))

