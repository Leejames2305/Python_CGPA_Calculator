print("----------------------------------------------------------")
print("              WELCOME TO THE CGPA CALCULATOR              ")
print("----------------------------------------------------------")

ID = int(input("Please key in your Student ID : "))
while len(str(ID)) != 7:
    print("Invalid Student ID (Exp of correct Student ID: 2100111)")
    ID = int(input("Please key in your Student ID : "))


def staff():
    print("\n1. Update Course Name")
    print("2. Update Credit Hours")
    print("3. Keep Students Details")
    print("4. Update results of students")
    print("0. Quit")
    select_2 = int(input("\nSelect the service you required from the list above : "))
    if select_2 == 0:
        print("Thanks for using")
    elif select_2 == 1:
        Course_Name()
    elif select_2 == 2:
        Credit_Hour()
    elif select_2 == 3:
        Students_Details()
    elif select_2 == 4:
        Students_Results()


def Course_Name():
    print("Course name")


def Credit_Hour():
    print("Credit hour")


def Students_Details():
    print("Student details")


def Students_Results():
    print("Student results")


def Course():
    print("Code        Course Name")
    print("--------------------------------------------------------")
    for i in range(1, 8, 1):
        print(*course_Code[i-1:i], "  ", *course_List[i-1:i])


def Grade():
    print("Grade")


def Results():
    print("Results")


def Other():
    print("Other")


def student():
    print("\nStudent's ID = ", ID)
    print("Name = ", Name)
    print("Stream", Stream)
    print("\n1. View Course List")
    print("2. Enter or Update Grade")
    print("3. View Results")
    print("4. Other functions")
    print("0. Quit")
    select_1 = int(input("\nSelect the service you required from the list above : "))
    if select_1 == 0:
        print("Thanks for using")
    elif select_1 == 1:
        Course()
    elif select_1 == 2:
        Grade()
    elif select_1 == 3:
        Results()
    elif select_1 == 4:
        Other()


course_List = [' Effective Communication Skills', 'English for Academic Study', 'Mathematics I', 'Mathematics II', 'Mathematics III', 'Organic Chemistry', 'Physical Chemistry']
course_Code = ['FHHM1022', 'FHEL1012', 'FHMM1014', 'FHMM1024', 'FHMM1034', 'FHSC1124', 'FHSC1114']

Name = "Unknown"
Stream = "Unknown"

if ID == 1234567:
    staff()
else:
    student()
