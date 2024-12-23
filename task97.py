from array import*



simple_2D=[[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

for i in simple_2D:
    print(i)

select_row=int(input("Enter a row: "))
slect_column=int(input("Enter a column: "))

print(simple_2D[select_row][slect_column])