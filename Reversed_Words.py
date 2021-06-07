# Complete the solution so that it reverses all of the words within the string passed 
def reverse_words(s):
    a=(' '.join(s.split(" ")[-1::-1]))
    return a
string=["hell0 world!"]
print(reverse_words(string))