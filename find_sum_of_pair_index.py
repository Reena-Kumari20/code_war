##############find pair of sum which target in input and append in new list their index###############

def sum_of_target(list1,target):
    index=[]
    for i in range(len(list1)-1):
        for j in range(i+1,len(list1)):
            if list1[i] + list1[j]==target:
                print("Sum of pair:",(list1[i],list1[j]))
                index.append(i)
                index.append(j)
    print(index)        
list1= [9,5,10,20]
target=int(input("enter the sum: "))
sum_of_target(list1,target)