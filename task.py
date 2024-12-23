import random
import csv



'''def get_name():
    user_name=input("Enter your name:")
    return user_name

def print_Msg(user_name):
    print("Hello",user_name)

def main():
    user_name=get_name()
    print_Msg(user_name)

main()'''

'''def get_data():
    user_name=input("Enter your name:")
    user_age=int(input("Enter your age:"))
    data_tuple=(user_name,user_age)
    return data_tuple

def message(user_name,user_age):
    if user_age<=10:
        print("Hi",user_name)
    else:
        print("Hello",user_name)

def main():
    user_name,user_age=get_data()
    message(user_name,user_age)

main()'''


def add_to_file():
    file=open("Salaries.csv","a")
    name=input("Enter your name:")
    salary=int(input("Enter your salary:"))
    newrecord=name+ "," +str(salary)+"\n"
    file.write(str(newrecord))
    file.close()

def display_records():
    file=open("Salaries.csv","r")
    for row in file:
        print(row)
    file.close()

def del_file():
    file=open("Salaries.csv","r")
    x=0
    tmplist=[]
    for row in file:
        tmplist.append(row)
    file.close()

    for row in tmplist:
        print(x,row)
        x=x+1
    rowdelete=int(input("Enter a row you want to delete:"))
    del tmplist[rowdelete]
    file=open("Salaries.csv","w")
    for row in tmplist:
        file.write(row)
    file.close()

tryagain=True

while tryagain==True:
    print("1)Add to file")
    print("2)View all records")
    print("3)Delete file")
    print("4)End program")
    print()

    selection=int(input("Enter your selection 1,2 or 3:"))

    if selection==1:
        add_to_file()
    elif selection==2:
        display_records()
    elif selection==3:
        del_file()
    elif selection==4:
        tryagain=False
    else:
        print("You have selected a wrong option")