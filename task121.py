from array import*



def add_name():
    name=input("Add name to the list: ")
    names.append(name)
    return names


def change_name():
    num=0
    for x in names:
        print(num,x)
        num=num+1


    select_num=int(input("Enter the number of the name you want to change: "))
    name=input("Enter new name: ")
    names[select_num]=name
    return names

def delete_name():
    num=0
    for x in names:

        print(num,x)
        num=num+1
    select_num=int(input("Enter the number of the name you want to delete: "))
    del names[select_num]
    return names

def view_names():
    for x in names:
        print(x)
    #print()

def main():

    again="y"
    while again=="y":
        print("1)Add name")
        print("2)Change a name")
        print("3)Delete a name")
        print("4)View names")
        print("5)Quit")
        selection=int(input("Select one of the options: "))
        if selection==1:
            names=add_name()
        elif selection==2:
            names=change_name()
        elif selection==3:
            names=delete_name()
        elif selection==4:
            names=view_names()
        elif selection==5:
            again="n"
        else:
            print("Incorreect option:")
        data=(names,again)

names= []

main()
    




