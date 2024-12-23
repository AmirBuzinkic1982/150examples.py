from array import*
import math




nums=array('f',[10.55,12.67,14.53,15.77,17.53])


tryagain=True
while tryagain==True:
    num=int(input("Enter a number between 2 and 5: "))
    
    if num<=2 or num>=5:
        print("Incorrect answer,please try again")

    else:
        tryagain=False

for f in range(0,5):

    answer=nums[f]/num

    print(round(answer,2))







