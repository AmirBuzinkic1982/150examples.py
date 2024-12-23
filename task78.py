programmes=["sky news","bbc","discovery","sports"]

for i in programmes:
    print(i)

another_programm=input("Enter another programm: ")
position=int(input("Enter the position 0 to 4: "))
programmes.insert(position,another_programm)
print(programmes)