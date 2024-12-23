from array import*


'''nums=array('i',[])
new_nums=array('i',[])

for i in range(0,5):
    num=int(input("Enter a number: "))
    nums.append(num)

    nums=sorted(nums)
    print(nums)

getRid=int(input("Enter index number: "))
nums.remove(getRid)

new_nums.append(getRid)
print(new_nums)'''

nums=array('i',[])

for i in range(0,5):
    num=int(input("Enter a number: "))
    nums.append(num)

nums=sorted(nums)

for i in nums:
    print(i)

num=int(input("Select a number from array: "))
if num in nums:
    nums.remove(num)
    num2=array('i',[])
    num2.append(num)
    print(nums)
    print(num2)
else:
    print("That number is not in the array: ")




