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
    print("You have",len(party),"people coming to your party")
    print(party)
    one_of_the_names=input("Enter one of the names from the list: ")
    print(one_of_the_names,"is in position",party.index(one_of_the_names),"on the list")
    answer=input("Do you still want that person to come y/n: ")

    if answer=="n":
        party.remove(one_of_the_names)
        print(party)


