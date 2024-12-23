print("1) Create a new file")
print("2) Display a new file")
print("3) Add a new item to the file")


selection=int(input("Please select 1,2 or 3: "))

if selection==1:
    new_subject=input("Enter the subject: ")
    file=open("Subject.txt","w")
    file.write(new_subject  + "\n" )
    file.close()

elif selection==2:
    file=open("Subject.txt","r")
    print(file.read())

elif selection==3:
    file=open("Subject.txt","a")
    new_subject=input("Enter the subject: ")
    
    file.write(new_subject + "\n")
    file.close()
    file=open("Subject.txt","r")
    print(file.read())
else:
    print("Invalid option")

    








