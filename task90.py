from array import*


newArray=array('i',[])




while len(newArray)<5:
    num=int(input("Enter a number: "))
    if num>=10 or num<=20:
        newArray.append(num)
    
    
    else:
        print("Outside range")

for i in newArray:
    

    print("Thank you",i)
    




