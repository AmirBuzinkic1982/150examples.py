

file=open("Names.txt","r")
print(file.read())
file.close()

file=open("Names.txt","r")
slectedname=input("Enter a name from the list: ")
slectedname=slectedname + "\n"
for row in file:
    if row !=slectedname:
        file=open("Names2.txt","a")
        newrecord=row
        file.write(newrecord)
        file.close()
    file.close()

