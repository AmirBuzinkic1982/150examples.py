from array import*
import random

nums=array('i',[])

for i in range(0,5):
    num=random.randint(0,100)
    nums.append(num)
    print(nums)

for i in nums:
    print(i)



