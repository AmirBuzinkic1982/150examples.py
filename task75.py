list=[111,222,333]
for i in list:
    print(i)
num=int(input("Enter a three digit number: "))

if num in list:
    print(num,"is in the position",list.index(num))
else:
    print("That is not on the lsit")
