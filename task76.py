

name1=input("Enter a name of the person you would like to invite: ")
name2=input("Enter another name of the person you would like to invite: ")
name3=input("Enter one more name of the person you would like to invite: ")

party=[name1,name2,name3]


print(party)

add_another=input("Do you want to add another person y/n: ")
print(add_another)

while add_another=="y":
    newname=party.append(input("Enter another name: "))
    add_another=input("Do you want to add another person y/n: ")
else:
    print(len(party),"are invited to the party")








