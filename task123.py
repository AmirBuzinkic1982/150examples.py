import csv

def addtofile():
    file=open("Salaries.csv","a")
    name=input("Enter name: ")
    salary=int(input("Enter your salary: "))
    newrecord=name+ "," +str(salary)+"\n"
    file.write(str(newrecord))
    file.close()

def viewrecords():
    file=open("Salaries.csv","r")

    for row in file:
        print(row)
    file.close()

def deleterecord():
    file=open("Salaries.csv","r")
    x=0
    tmplist=[]
    for row in file:
        tmplist.append(row)
    file.close()
    for row in tmplist:
        print(x,row)
        x=x+1
    rowtodelete=int(input("Enter the row you want to delete:"))
    del tmplist[rowtodelete]
    file=open("Salaries.csv","w")
    for row in tmplist:
        file.write(row)
    file.close()
tryagain=True
while tryagain==True:
    print("1)Add file")
    print("2)View records")
    print("3)Delete record")
    print("4)Quit program")
    print()
    selection=(input("Enter the number of your selection: "))
    if selection=="1":
        addtofile()
    elif selection=="2":
        viewrecords()
    elif selection=="3":
        deleterecord()
    elif selection=="4":
        tryagain=False

    else:
        print("Incorrect option")






    
        
