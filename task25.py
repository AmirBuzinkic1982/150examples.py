name=input("Enter your first name: ")
lenght=len(name)
if len(name)<5:
    surname=input("Enter your surname: ")
    name=name+surname
    print(name.upper())
else:
    print(name.lower())
   
