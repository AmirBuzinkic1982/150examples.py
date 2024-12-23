total=0

for i in range(0,5):
    num=int(input("Enter the number: "))
    answer=input("Do you want that number included?(y/n): ")
    if answer=="y":
        total=total+num
        print(total)