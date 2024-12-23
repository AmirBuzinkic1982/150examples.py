from array import*

'''nums=array('i',[2,3,7,8,7,])
print(nums)

pick=int(input("Enter on of the numbers from the array: "))

print("Number apears",nums.count(pick),"times")'''



nums=array('i',[3,4,5,7,7])

for i in nums:
    print(i)

num=int(input("Enter number from the list: "))

if nums.count(num)==1:
    print(num,"is in the list once")
else:
    print(num,"is in the list",nums.count(num),"times")
