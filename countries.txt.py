


file=open("Countries.txt","w")
file.write("Italy\n")
file.write("Germany\n")
file.write("Spain\n")
file.close()

file=open("Countries.text","r")
print(file.read())


file=open("Countries.text","a")
file.write("France\n")
file.close()

