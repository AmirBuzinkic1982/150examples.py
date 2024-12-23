new_password=input("Enter a new password in small letters: ")
confirm_password=input("Confirm a new password with small letters: ")


if new_password==confirm_password:
    print("Thank you")

elif new_password.lower()==confirm_password.lower():
    print("They must be in the same case")
else:
    print("Incorrect")
