print("-----> Student Management System <-----")

# Kayıtlı öğrenci adı ve soyadı
name = "Burak"
surname = "Şentürk"

# Girilecek hak
enteredNumber = 3

# Döngü başlangıcı
while True:
    enteredName = str(input("Enter your name : "))
    enteredSurname = str(input("Enter your surname : "))
    if name == enteredName and surname == enteredSurname:
        print(f"Welcome {name} {surname}")
        lessons=["MATHS","TURKISH","GEOGRAPHY","HISTORY","PHYSICS"]
        chosenCourse=[]
        lessonNumber=int(input("How many lessons do you take (You can take a minimum of 3 and a maximum of 5 courses!) :"))
        if 3<=lessonNumber<=5:
            print(f'Lessons you took -> {lessons}')
            while lessonNumber>0:
                courseName=str(input("Enter the name of the lesson :")).upper()
                if courseName not in lessons:
                    print("There is no such course! Type again")
                    lessonNumber += 1
                else:
                    if courseName in chosenCourse:
                        print("I remember this letter before. Please guess another letter.")
                        continue
                    chosenCourse.append(courseName)
                    print("Registration has been successfully added to your courses...")
                lessonNumber -= 1
            print(f"List of courses you have selected -> {chosenCourse}")
            examLesson=str(input("Which course will you take the exam from? :")).upper()
            examGrade={}
            midtermGrade=int(input(f"{examLesson} enter the grade you got from the midterm exam : "))
            finalGrade=int(input(f"{examLesson} enter the grade you got from the final exam : "))
            projectGrade=int(input(f"{examLesson} enter the grade you got from the project exam : "))
            examGrade["Midterm"] = midtermGrade
            examGrade["Final"] = finalGrade
            examGrade["Project"] = projectGrade

            # Exam grade calculation
            passingAverage = ((midtermGrade*30)/100) + ((finalGrade*50)/100) + ((projectGrade*20)/100)
            if passingAverage>90:
                print(f"{examLesson} your grade is AA. Congratulations")
                break
            elif 70<passingAverage<90:
                print(f"{examLesson} your grade is BB. Congratulations")
                break
            elif 50<passingAverage<70:
                print(f"{examLesson} your grade is CC. Congratulations")
                break
            elif 30<passingAverage<50:
                print(f"{examLesson} your grade is DD.")
                break
            else:
                print(f"{examLesson} your grade is FF. You stayed in class.")
                break

        # Feedback to be given if he/she wants to take less than 3 or more than 5 courses
        else:
            print("If your course number is less than 3, it cannot be more than 5.")
            break
        
    # If the entered name and surname is incorrect, the feedback to be given
    elif (name != enteredName or surname != enteredSurname) and enteredNumber != 0:
        enteredNumber -= 1
        if enteredNumber>0:
            print("You wrote wrong, please try again.")
            again=input(f"{name} {surname} do you want to login again? (y/n): ")
            if again == "y":
                continue
            else:
                break
        else:
            print("Please try again later..")
            break