import csv

file=open("Books.csv","r")

x=0

for row in file:

    display="Row:"+str(x)+" - "+row     #"Row" acts as a row number(0,1,2,3etc),+ concatenates 2 strings into one
                                        #str(x)converts x as its a integer into string so it can further concatenate
                                        #for exmp Row:10 - Snowing outside,Amir Buzinkic,2025
                                        # and " - " stands for separation for row,and row itself is a content of that row number or line

    print(display)
    x=x+1


