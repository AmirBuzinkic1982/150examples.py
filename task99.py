from array import*



simple_2D=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

for i in simple_2D:
    print(i)

row=int(input("Which row would you like to have: "))

print(simple_2D[row])

col=int(input("Which column would you like to have in that row: "))

print(simple_2D[row][col])

ans=input("Do you want to change that value y/n: ")

if ans=="y":
    newvalue=int(input("Enter the newvalue: "))
    simple_2D[row][col]=newvalue
print(simple_2D[row])


