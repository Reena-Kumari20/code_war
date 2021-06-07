# Sort and Star
# You will be given a vector of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars)
#  and then return the first value.
# The returned value must be a string, and have "***" between each of its letters.
# You should not remove or add elements from/to the array.

def two_sort(array):
    a=sorted(array)
    b=a[0]
    c=' '
    i=0
    while i<len(b):
        c=c+b[i]+"***"
        i=i+1
    c = c.rstrip("*")
    return c

array=["bitcoin","star","string","letter"]
print(two_sort(array))
