import csv



startyear=int(input("Enter a starting year:"))
endyear=int(input("Enter a end year:  "))

file=list(csv.reader(open("Books.csv")))

tmp=[]
for row in file:
    tmp.append(row)

x=0
for row in tmp:
   if int(tmp[x][2])>=startyear and int(tmp[x][2])<=endyear:
    print(tmp[x])
    x=x+1