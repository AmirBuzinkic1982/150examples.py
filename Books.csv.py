import csv

file=open("Books.csv","w")
newRecord="To kill a Mockinbird,Harper Lee,1960\n"
file.write(str(newRecord))
newRecord="A brief history of time,Stephen Hawking,1988\n"
file.write(str(newRecord))
newRecord="The great Gatsby,F.Scott Fitzerald,1922\n"
file.write(str(newRecord))
newRecord="The man who misstook his wife for a hat,Oliver Sacks,1985\n"
file.write(str(newRecord))
newRecord=("Pride and prejudice,James Austen.1813\n")
file.write(str(newRecord))
file.close()



