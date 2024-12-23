compnum=50
guess=int(input("Can you guess the number: "))
count=1
while guess != compnum:
    if guess < compnum:
        print("Too low")
    else:
        print("too high")
    count=count+1
    guess=int(input("Have another guess: "))
print("Well done,you took",count,"attemps")








