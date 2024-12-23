num_of_people=int(input("How many people do you want to invite?: "))

if num_of_people<10:
    
    for i in range(0,num_of_people):
        name=input("Enter their names: ")
        print(name,"Has been invited")
else:
    print("Too many people")
