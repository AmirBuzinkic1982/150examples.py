import math 

print("1)Square")
print("2)Triangle")
print()

number=int(input("Enter the number:  "))

if number==1:
    side=int(input("enter the lenght of one side:  "))
    area=side*side
    print("Area of your chosen shape is",area)

elif number==2:
    base=int(input("Enter the lenght of the triangle: "))
    height=int(input("Enter the height of the triangle: "))
    area=(base*height)/2
    print("The area of your chosen shape is",area)
else:
    print("Incorrect option selected")

