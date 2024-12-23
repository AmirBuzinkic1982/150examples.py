import sqlite3
import os

# Specify the file name
db_file = "Bookinfo.db"

# Check if the file exists
if os.path.exists(db_file):
    os.remove(db_file)
    print(f"{db_file} has been deleted.")
else:
    print(f"{db_file} does not exist.")



with sqlite3.connect("PhoneBook.db")as db:
    cursor=db.cursor()

cursor.execute("DELETE FROM Names")
db.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS Names(

id integer PRIMARY KEY,
 firstname text,
 surname text,
 phonenumber text);""")

cursor.execute("""INSERT INTO Names(id,firstname,surname,phonenumber)
            VALUES(1,"Simon","Howels","01223 349752")""")
db.commit()

cursor.execute("""INSERT INTO Names(id,firstname,surname,phonenumber)
              VALUES(2,"Karen","Philips","01954 295773")""")
db.commit()

cursor.execute("""INSERT INTO Names(id,firstname,surname,phonenumber)
              VALUES(3,"Darren","Smith","01583 749012")""")
db.commit()

cursor.execute("""INSERT INTO Names(id,firstname,surname,phonenumber)
              VALUES(4,"Anne","Jones","01323 567322")""")

cursor.execute("""INSERT INTO Names(id,firstname,surname,phonenumber)
             VALUES(5,"Mark","Smith","01223 85534")""")
db.commit()

db.close()

'''cursor.execute("SELECT * FROM Names")
records = cursor.fetchall()

print("ID | Firstname | Surname | Phone Number")
print("-" * 40)
for row in records:
    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

db.close()'''
