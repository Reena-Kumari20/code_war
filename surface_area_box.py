# Surface Area and Volume of a Box: 
# Write a function that returns the surface area and volume of a box as an array: [area,volume]

def get_size(w,h,d):
    area=2*d*w+2*d*h+2*w*h
    volume=w*h*d
    list1=[area,volume]
    return list1
w=int(input("enter: "))
h=int(input("enter: "))
d=int(input("enter: "))
print(get_size(w,h,d))


