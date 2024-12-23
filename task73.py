dict={}

food1=input("Enter a food you like: ")
dict[1]=food1

food2=input("Enter a second food you like: ")
dict[2]=food2

food3=input("Enter third food you like: ")
dict[3]=food3

food4=input("Enter fourth food you like: ")
dict[4]=food4

print(dict)

getrid=int(input("Enter the food you do not like : "))

del dict[getrid]


print(sorted(dict.values()))



