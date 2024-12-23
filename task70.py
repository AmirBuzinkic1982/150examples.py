countries=("US","Serbia","Italy","Spain","Portugal")

print(countries)
print()

name=input("Enter the name of the county from the list: ")
print(countries.index(name))
print()


number=int(input("Enter the number between 0 and 4: "))
print(countries[number])
