import csv


file=open("Books.csv","w")
newRecord="To kill a mockingbird,Harper Lee,1960\n"
file.write(str(newRecord))

newRecord="A brief history of Time,Stephen Hawking,1988\n"
file.write(str(newRecord))

newRecord="The great Gatsby,F Scott Fitzgerald,1922\n"
file.write(str(newRecord))

newRecord="The man who misstook his wife for a Hat,Oliver Sacks,1985\n"
file.write(str(newRecord))

newRecord="Pride and Prejudice,Jane Austen,1813\n"
file.write(str(newRecord))

file.close()