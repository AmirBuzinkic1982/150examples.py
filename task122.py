import csv


def addtofile():
    file=open("Salaries.csv","a")
    name=input("Enter  name: ")
    salary=int(input("Enter your salary: "))
    newRecord=name+","+str(salary)+ "\n"
    file.write(str(newRecord))
    file.close()

def viewrecord():
    file=open("Salaries.csv","r")

    for row in file:
        print(row)
    file.close()




tryagain=True

while tryagain==True:
      print("1)Add to a file")
      print("2)Display a file")
      print("3)Quit program")
      print()

        
      selection=int(input("Enter the number of your selection: "))

      if selection==1:
          addtofile()

      elif selection==2:
            viewrecord()

      elif selection==3:
            tryagain=False

      else:
            print("Incorrect option")




        

            

