from array import*

list={}

for i in range(0,4):
    name=input("Enter name:")
    age=int(input("Enter age:"))
    shoe=int(input("Enter a shoes size:"))
    list[name]={ "Age":age,"Shoes Size":shoe }



list[name]={ "Age":age,"Shoes Size":shoe }


getrid=input("Enter the name of the person you want to take out: ")

del list[getrid]

for name in list:

    print((name),list[name]["Age"],list[name]["Shoes Size"])



    
        
