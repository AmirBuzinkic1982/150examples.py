

word=input("Enter any word: ")

first=word[0]
lenght=len(word)
rest=word[1:lenght] 
if first !="a" and first !="e"and first !="i" and first !="o" and first !="u":
    newword=rest+first+"ay"
else:
    newword=word+"way"
print(newword.lower())

