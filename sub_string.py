# find sub string

def sub_string(user):
    i=0
    while i<len(user):
        j=i+1
        while j<=len(user):
            string=user[i:j]
            sub_string=string[::-1]
            if string==sub_string and len(string)>1:
                print(string)
            j+=1
        i+=1
user=input("enter string: ")
sub_string(user)
