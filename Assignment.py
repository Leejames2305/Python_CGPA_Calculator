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
    print("\nCore Course")
    print("Code        Course Name")
    print("--------------------------------------------------------")
    for i in range(1, len(Core_Course_List) + 1, 1):
        print(*Core_Course_Code[i - 1:i], "  ", *Core_Course_List[i - 1:i])  # the * is to prevent it printing []
    print("\nElective Course")
    print("Code        Course Name")
    print("--------------------------------------------------------")
    for i in range(1, len(Student_Stream_Course) + 1, 1):
        print(*Student_Stream_Code[i - 1:i], "  ", *Student_Stream_Course[i - 1:i])
    input('\nPress Enter to continue')
    student()


def Grade():
    print("\nCore Course")
    print("Code        Course Name")
    print("--------------------------------------------------------")
    for i in range(1, len(Core_Course_List) + 1, 1):
        print(*Core_Course_Code[i - 1:i], "  ", *Core_Course_List[i - 1:i])  # the * is to prevent it printing '[]'
    print("\nElective Course")
    print("Code        Course Name")
    print("--------------------------------------------------------")
    for i in range(1, len(Student_Stream_Course) + 1, 1):
        print(*Student_Stream_Code[i - 1:i], "  ", *Student_Stream_Course[i - 1:i])
    Grade_Course_Code = []
    Grade_Grades = []
    Input_Grade_Course_Code = input("\nEnter the course code (Enter '0' to Exit) : ")
    Input_Grade_Grades = input('Enter grade : ')
    if Input_Grade_Course_Code in Core_Course_Code + Student_Stream_Code:  # Combine Core and Elective Course
        if Input_Grade_Course_Code not in Grade_Course_Code:
            Grade_Course_Code.append(Input_Grade_Course_Code)
            Grade_Grades.append(Input_Grade_Grades)
        else:
            print('This course Grade is already recorded in the system . ')
    else:
        print('\nYou do not have this course in your stream ! ')
        Grade()


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


print("----------------------------------------------------------")
print("              WELCOME TO THE CGPA CALCULATOR              ")
print("----------------------------------------------------------")

ID = int(input("Please key in your Student ID : "))
while len(str(ID)) != 7:
    print("Invalid Student ID (Exp of correct Student ID: 2100111)")
    ID = int(input("Please key in your Student ID : "))

Core_Course_List = ['Effective Communication Skills', 'English for Academic Study', 'Mathematics I', 'Mathematics II',
               'Mathematics III', 'Organic Chemistry', 'Physical Chemistry']
Core_Course_Code = ['FHHM1022', 'FHEL1012', 'FHMM1014', 'FHMM1024', 'FHMM1034', 'FHSC1124', 'FHSC1114']

Stream_1_Course_List = ['Fundamentals of Cell Biology', 'Inorganic Chemistry', 'Introduction to Physiological Systems',
                        'Modern Biology', 'Physics I', 'Physics II', 'Programming Concept']
Stream_1_Code_List = ['FHSC1214', 'FHSC1134', 'FHSC1224', 'FHSC1234', 'FHSP1014', 'FHSP1024', 'FHCT1022']

Stream_2_Course_List = ['Mechanics', ' Thermodynamics and Electromagnetism', 'Waves and Modern Physics',
                        'Inorganic Chemistry', 'Programming Concepts', 'Biology I', 'Biology II']
Stream_2_Code_List = ['FHSC1014', 'FHSC1024', 'FHSC1034', 'FHSC1134', 'FHCT1022', 'FHSB1214', 'FHSB1224']

Stream_3_Course_List = ['Computing Technology', 'Introduction to Data Analytics', 'Programming Concepts and Design',
                        'Management', 'Mechanics', 'Thermodynamics and Electromagnetism', 'Biology I']
Stream_3_Code_List = ['FHSC1214', 'FHSC1134', 'FHSC1224', 'FHSC1234', 'FHSP1014', 'FHSP1024', 'FHCT1022']

ID_list = ['2103301', '2103302', '2103303']  # 1st student ID = 2103301
Name_list = ["Josh", "Jack", "Jason"]  # 1st student name = Josh
Stream_list = ['1', '2', '3']  # 1st student stream = Stream 1

List_Position = ID_list.index(str(ID))  # Finding ID in the list and the index(position) of it in all list
Name = Name_list[List_Position]
Stream = Stream_list[List_Position]

if Stream == '1':  # Determine which List should the data read from according to the correct Stream
    Student_Stream_Code = Stream_1_Code_List
    Student_Stream_Course = Stream_1_Course_List
elif Stream == '2':
    Student_Stream_Code = Stream_2_Code_List
    Student_Stream_Course = Stream_2_Course_List
elif Stream == '3':
    Student_Stream_Code = Stream_3_Code_List
    Student_Stream_Course = Stream_3_Course_List

if ID == 1234567:  # Staff ID login is 1234567
    staff()
else:
    student()
