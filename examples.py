num1=93
num2=97

answer=num1+num2
answer=num1-num2
answer=num1*num2
answer=num1/num2
answer=num1//num2

print(answer)

print("This is a message")

print("First line\nSecond line")           #\n is used as a line break

print("The answer is",answer)

textValue=input("Enter a text value: ")     #Displays the question “Enter a text value: ”
                                            # and stores the value the user enters in a 
                                             #variable called textValue. The space after the colon allows a space
                                             #  to be added before 
                                             #the user enters their answer, otherwise they appear squashed unattractively together. 

numValue=int(input("Enter a number: "))    #Displays the question “Enter a number: ” and stores the value as an 
                                            #integer (a whole number) in a variable called numValue Integers can be 
                                            #used in calculations but variables stored as text cannot.


firstname=input("Please eneter your first name: ")
print("Hello",firstname)

firstname=input("Please enter your first name: ")
surname=input("Please enter your surname: ")
print("Hello",firstname,surname)

print("What do you call a bear with no teeth?\nA gummy bear!")


num1=int(input("Please enter your first number: "))
num2=int(input("Please eneter your second number: "))
answer=(num1+num2)
print("The answer is",answer)

num1=int(input("Please enter how many slices of oizza did you have: "))
num2=int(input("Please enter how many slices of pizza there was: "))
answer=(num2-num1)
print("The answer is",answer)

name=(input("Please enter your first name: "))
age=int(input("Please enter your age: ") )
newAge=age+1
print(name,"Next birthday will be",newAge)

TotalPrice=int(input("What was the total price of the bill: "))
NumberOfDinners=int(input("How many dinners did you have: "))
EachPersonBill=TotalPrice/NumberOfDinners
print(EachPersonBill)

days=int(input("Enter the number of days: "))
hours=days*24
minutes=hours*60
seconds=minutes*60
print("In",days,"days there are ...")
print(hours,"hours")
print(minutes,"minutes")
print(seconds,"seconds")



                                               