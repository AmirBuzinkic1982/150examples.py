import random

def addition():
    num1=random.randint(5,20)
    num2=random.randint(5,20)
    print(num1,"+",num2,"= ")
    user_answer=int(input("Your answer: "))
    actual_answer=num1+num2
    answers=(user_answer,actual_answer)
    return answers
    

def subtraction():
    num3=random.randint(25,50)
    num4=random.randint(1,25)
    print(num3,"-",num4,"= ")
    user_answer=int(input("Your answer: "))
    actual_answer=num3-num4
    answers=(user_answer,actual_answer)
    return answers
    

def correct_answer(user_answer,actual_answer):

    if user_answer==actual_answer:
        print("Correct")
    else:
        print("Incorect,the correct answer is",actual_answer)
def main():
    print("1)Addition")
    print("2)Subtraction")
    selection=int(input("Enter 1 or 2:"))
    if selection==1:
        user_answer,actual_answer=addition()
        correct_answer(user_answer,actual_answer)
    elif selection==2:
        user_answer,actual_answer=subtraction()
        correct_answer(user_answer,actual_answer)

    else:
        print("Incorrect selection")

main()




