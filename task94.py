from array import*

nums=array('i',[3,5,7,51,2])

for i in nums:
    print(i)

num=int(input("Select one of the numbers from the array: "))

tryagain=True

while tryagain==True:
    if num in nums:
       print("This is in  position",nums.index(num))
       tryagain=False


    else:
        print("Not in the array")
        num=int(input("Select a number from the array: "))