from array import*



list={}

for i in range(0,4):
    name=input("Enter name:")
    age=int(input("Enter age:"))
    shoe=int(input("Enter a shoes size:"))
    list[name]={"Age":age,"Shoe size":shoe}

for name in list:
    print((name),list[name]["Age"])
    
