answer=input("Is it raining?: ")

answer=str.lower(answer)


if answer=="yes":
    windy=(input("Is it windy: "))
    windy=str.lower(windy)
    if windy=="yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")