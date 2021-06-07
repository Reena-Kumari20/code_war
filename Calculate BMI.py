def bmi(weight, height):
    #your code here
    bmi=weight/(height*height)
    #print(bmi)
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal"
    elif bmi < 30.0:
        return "Overweight"
    elif bmi > 30:
        return "Obese"

weight=int(input("Enter the weight--> "))
height=int(input("Enter the height--> "))
print(bmi(weight,height))