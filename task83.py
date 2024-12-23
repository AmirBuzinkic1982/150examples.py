word=input("Enter word,word in a upper case:   ")
tryagain=False

while tryagain==False:
    if word.isupper():
        print("Thank you")
        tryagain=True
    else:
        print("Try again")
        word=input("Enter word,word in a upper case: ")