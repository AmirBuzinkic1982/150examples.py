import random
heads_tails=random.choice(["h","t"])


user_choice=input("Select h/t:  " )


if heads_tails==user_choice:
    print("You win")
else:
    print("Bad luck")
if heads_tails=="h":
    print("It was heads")
else:
    print("It was tails")
print("Computer has selected",heads_tails)