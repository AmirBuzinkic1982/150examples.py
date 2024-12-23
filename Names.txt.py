

file=open("Names.txt","w")

file.write("Amir\n")
file.write("Igor\n")
file.write("Dusan\n")
file.write("Robert\n")
file.write("Marko\n")

file.close()

file=open("Names.txt","r")
print(file.read())
file.close()




