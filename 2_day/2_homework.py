# Information from the part
fName = input("First Name :")
lName = input("Last Name :")
age = int(input("Age :"))
dateOfBirth = int(input("Date of birth (just year)"))

# Listing user information
userList = [fName, lName, age, dateOfBirth]

# Print to the screen with a for loop
print("Print to the screen with a for loop")

# First Way
# for i in range(len(userList)):
#     indexNumber = userList[i]
#     print(indexNumber)

# Second Way
for i in range(len(userList)):
    if i == 0:
        print(f"First Name : {userList[i]}")
    elif i == 1:
        print(f"Last Name : {userList[i]}")
    elif i == 2:
        print(f"Age : {userList[i]}")
    else:
        print(f"Date of birth (just year) : {userList[i]}")

# If command part
if age < 18:
    print("You can't go out because it's too dangerous")
else:
    print("You can go to the street")
