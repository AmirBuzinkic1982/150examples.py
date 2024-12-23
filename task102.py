from array import*

list={}

for i in range(0,4):
    name=input("Enter name:")
    age=int(input("Enter age:"))
    shoe=int(input("Enter a shoes size:"))


print(i)

list[name]={ "Age":age,"Shoes Size":shoe }

ask=input("Enter persons name: ")

print(list[ask])






