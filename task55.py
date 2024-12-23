import random

num=random.randint(1,5)

user_choice=int(input("Choose a number:  "))

if user_choice==num:
    print("Well done")

elif user_choice<1:
    print("Too low")
    user_choice=int(input("Pick a second number: "))
    if user_choice==num:
        print("Correct")
    else:
          print("You loose")
elif user_choice>5:
    print("Too high")
    user_choice=int(input("Pick a second number: "))
    if user_choice==num:
        print("Correct")
    else:
        print("You loose")