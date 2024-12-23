from array import*



simple_2D=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

for i in simple_2D:
    print(i)

row=int(input("Which row would you like to have: "))

print(simple_2D[row])

num=int(input("Add number to that row: "))

simple_2D[row].append(num)

print(simple_2D[row])
