import csv


file=open("Books.csv","a")

title=input("Enter title:  ")
author=input("Enter author: ")
year=input("Enter the year it was released: ")
newRecord=title+ "," +author+ "," +year+ "\n"
file.write(str(newRecord))
file.close()

file=open("Books.csv","r")
for row in file:
    print(row)

file.close()

