word=input("Enter a word:  ")
lenght=len(word)
num=1

for x in word:
    position=lenght-num
    letter=word[position]
    print(letter)
    num=num+1