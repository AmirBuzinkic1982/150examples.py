
count=0
again="y"

while again=="y":
    name=input("Enter the name of the person you want to invite: ")
    print(name,"has been invited")
    
    count=count+1
    again=input("Do you want to invite somebody else y/n: ")
    print("You have",count,"People coming to party")


