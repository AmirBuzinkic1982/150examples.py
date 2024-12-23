
import csv

num=int(input("How many files do you want to add: "))

file=open("Books.csv","a")

for x in range(0,num):
    title=input("Enter title:  ")
    author=input("Enter author: ")
    year=input("Enter the year it was released: ")
    newRecord=title+ "," +author+ "," +year+ "\n"
    file.write(str(newRecord))
file.close()

file=open("Books.csv","r")
count=0
searchauthor=input("Enter the authors name: ")

for row in file:
    if searchauthor in str(row):
        print(row)
        count=count+1
if count==0:
        print("There is no books by that author in this list")
file.close()




