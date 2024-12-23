



name=input("Enter your name: ")
count=0

name=name.lower()

for x in name:
    if x=="a" or x=="e" or x=="i" or x=="u"or x=="o":
        count=count+1
        print("Vowels=",count)
