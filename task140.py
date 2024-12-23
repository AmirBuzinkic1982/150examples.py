import sqlite3




def viewphonebook():
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)

def addtophonebook():
    newid=int(input("Enter ID:"))
    newfname=input("Enter first name:")
    newsname=input("Enter surname: ")
    newpnum=input("Enter phone number:")
    cursor.execute("""INSERT INTO Names(id,firstname,surname,phonenumber)
VALUES (?,?,?,?)""",(newid,newfname,newsname,newpnum))
    db.commit()
    print("Record added succesfully")

def selectname():
    selectsurname=input("Enter a surname: ")
    cursor.execute("SELECT * FROM Names WHERE surname =?",[selectsurname])
    for x in cursor.fetchall():
        print(x)

def deletedata():
    selectid=int(input("Enter ID:"))
    cursor.execute("SELECT * FROM Names WHERE id=?",[selectid])
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
    db.commit()

with sqlite3.connect("Phonebook.db")as db:
    cursor=db.cursor()

def main():
    again="y"
    while again =="y":
        #print()
        print("\nMain Menu\n")
        #print()
        print("1) View phonebook")
        print("2) Add to phonebook")
        print("3) Search for surname")
        print("4) Delete person from phonebook")
        print("5) Quit)")
        print()
        selection=int(input("Enter your selection:"))
        print()

        if selection==1:
            viewphonebook()
        elif selection==2:
            addtophonebook()
        elif selection==3:
            selectname()
        elif selection==4:
            deletedata()
        elif selection==5:
            again="n"
        else:
            print("Incorrect selection entered")

main()
db.close()
