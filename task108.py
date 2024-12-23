
file=open("Names.txt","a")
name=input("Enter a name:")
file.write(name + "\n")
file.close
file=open("Names.txt","r")
print(file.read())
file.close