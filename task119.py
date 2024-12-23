import random

def pick_num():

    low=int(input("Enter a low number: "))
    high=int(input("Enter a high number: "))
    comp_num=random.randint(low,high)
    return comp_num

def first_guess():
    print("I'm thinking of a number....? ")
    guess=int(input("Guess a number : "))
    return guess
def check_if_equal(comp_num,guess):
    try_again=True
    while try_again==True:
        if comp_num==guess:
           print("Correct you win")
           try_again=False
        elif comp_num>guess:
            guess=int(input("Too low,guess again: "))
        else:
            
            guess=int(input("Too high ,try again: "))

def main():
    comp_num=pick_num()
    guess=first_guess()
    check_if_equal(comp_num,guess)

main()

        
        
        
          
             
        
             
        


    

    
