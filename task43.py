direction=input("Please select and enter up or down:  ")

if direction=="up":
    top_num=int(input("Enter the top number: "))
    for i in range(1,top_num+1):
        print(i)
elif direction=="down":
    below_twenty=int(input("Enter the number below 20: "))
    for i in range(20,below_twenty-1,-1):
        print(i)
else:
    print("I don't understand")


