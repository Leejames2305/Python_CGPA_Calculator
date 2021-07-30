import time


# -------------------------------------------------STAFF----------------------------------------------------------
def Course_Name():
    Code_Or_Name = input("Would you like update the Course name based on Course Name(NAME)"
                         " or Course Code(CODE) ? ").upper()
    if Code_Or_Name == 'NAME':
        Selected_Course_Name = input("Please enter the Course Name you want to update : ")
        Replaced_Course_Name = input("Please enter the new name : ")
        if Selected_Course_Name in Core_Course_List:
            Core_Course_List[Core_Course_List.index(Selected_Course_Name)] = Replaced_Course_Name
            print("\nDone")
            time.sleep(0.5)
        if Selected_Course_Name in Stream_1_Course_List:
            Stream_1_Course_List[Stream_1_Course_List.index(Selected_Course_Name)] = Replaced_Course_Name
            print("\nDone")
            time.sleep(0.5)
        if Selected_Course_Name in Stream_2_Course_List:
            Stream_2_Course_List[Stream_2_Course_List.index(Selected_Course_Name)] = Replaced_Course_Name
            print("\nDone")
            time.sleep(0.5)
        if Selected_Course_Name in Stream_3_Course_List:
            Stream_3_Course_List[Stream_3_Course_List.index(Selected_Course_Name)] = Replaced_Course_Name
            print("\nDone")
            time.sleep(0.5)
        else:
            print('Invalid Course Name ! Please check again the name you key in (CAPS is important)')
            Course_Name()
        staff()
    elif Code_Or_Name == 'CODE':
        Selected_Course_Code = input("Please enter the Course Code of the course you want to update its name : ")
        Replaced_Course_Name = input("Please enter the new name : ")
        if Selected_Course_Code in Core_Course_Code:
            Core_Course_List[Core_Course_Code.index(Selected_Course_Code)] = Replaced_Course_Name
            print("\nDone")
            time.sleep(0.5)
            staff()
        if Selected_Course_Code in Stream_1_Code_List:
            Stream_1_Course_List[Stream_1_Code_List.index(Selected_Course_Code)] = Replaced_Course_Name
            print("\nDone")
            time.sleep(0.5)
        if Selected_Course_Code in Stream_2_Code_List:
            Stream_2_Course_List[Stream_2_Code_List.index(Selected_Course_Code)] = Replaced_Course_Name
            print("\nDone")
            time.sleep(0.5)
        if Selected_Course_Code in Stream_3_Code_List:
            Stream_3_Course_List[Stream_3_Code_List.index(Selected_Course_Code)] = Replaced_Course_Name
            print("\nDone")
            time.sleep(0.5)
        else:
            print('Invalid Code ! Please check again the name you key in (CAPS is important)')
            Course_Name()
        staff()

    else:
        print("Invalid selection. ")
        Course_Name()


def Credit_Hour():
    Selected_Course_Code = input("Please enter the Course Code of the course you want to update its credit hour : ")
    try:
        Replaced_Credit_Hour = int(input("Please enter the new credit hour : "))
        if 0 < Replaced_Credit_Hour < 10:
            if Selected_Course_Code in Core_Course_Code:
                Core_Course_Code[Core_Course_Code.index(Selected_Course_Code)] = \
                    (Core_Course_Code[Core_Course_Code.index(Selected_Course_Code)][0:7]) + str(Replaced_Credit_Hour)
                print("\nDone")
                time.sleep(0.5)
                staff()
            if Selected_Course_Code in Stream_1_Code_List:
                Stream_1_Code_List[Stream_1_Code_List.index(Selected_Course_Code)] = \
                    (Stream_1_Code_List[Stream_1_Code_List.index(Selected_Course_Code)][0:7]) + str(
                        Replaced_Credit_Hour)
                print("\nDone")
                time.sleep(0.5)
            if Selected_Course_Code in Stream_2_Code_List:
                Stream_2_Code_List[Stream_2_Code_List.index(Selected_Course_Code)] = \
                    (Stream_2_Code_List[Stream_2_Code_List.index(Selected_Course_Code)][0:7]) + str(
                        Replaced_Credit_Hour)
                print("\nDone")
                time.sleep(0.5)
            if Selected_Course_Code in Stream_3_Code_List:
                Stream_3_Code_List[Stream_3_Code_List.index(Selected_Course_Code)] = \
                    (Stream_3_Code_List[Stream_3_Code_List.index(Selected_Course_Code)][0:7]) + str(
                        Replaced_Credit_Hour)
                print("\nDone")
                time.sleep(0.5)
            else:
                print('Invalid Code ! Please check again the name you key in (CAPS is important)')
                Credit_Hour()
            staff()
        else:
            print("Value should be between 1 ~ 9 only ! ")
    except ValueError:
        print("That isn't a integer")


def Students_Details():
    print("\nKeep Student details is currently not available")
    staff()


def Students_Results():
    print("\nUpdate Students' results is currently not available")
    staff()


def List_All_Course():
    print("\nCore Course")
    print("Code        Course Name")
    print("--------------------------------------------------------")
    for i in range(1, len(Core_Course_List) + 1, 1):
        print(*Core_Course_Code[i - 1:i], "  ", *Core_Course_List[i - 1:i])  # the * is to prevent it printing []
    print("\nElective Course")
    print("Code        Course Name")
    print("--------------------------------------------------------")
    print("\n Stream 1")
    for i in range(1, len(Stream_1_Code_List) + 1, 1):
        print(*Stream_1_Code_List[i - 1:i], "  ", *Stream_1_Course_List[i - 1:i])
    print("\n Stream 2")
    for i in range(1, len(Stream_2_Code_List) + 1, 1):
        print(*Stream_2_Code_List[i - 1:i], "  ", *Stream_2_Course_List[i - 1:i])
    print("\n Stream 3")
    for i in range(1, len(Stream_3_Code_List) + 1, 1):
        print(*Stream_3_Code_List[i - 1:i], "  ", *Stream_3_Course_List[i - 1:i])
    time.sleep(0.5)
    staff()


def staff():
    print("\n1. Update Course Name")
    print("2. Update Credit Hours")
    print("3. Keep Students Details")
    print("4. Update Students' Result")
    print("5. List down all the course")
    print("0. Log Out")
    select_2 = input("\nSelect the service you required from the list above : ")
    if select_2 == '0':
        print('\nLogging Out ... ')
        login()
    elif select_2 == '1':
        Course_Name()
    elif select_2 == '2':
        Credit_Hour()
    elif select_2 == '3':
        Students_Details()
    elif select_2 == '4':
        Students_Results()
    elif select_2 == '5':
        List_All_Course()
    else:
        print('Please enter the options from 1 ~ 5 only')
        staff()


# ------------------------------------------------STUDENT-----------------------------------------------------
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
    Input_Grade_Course_Code = input("\nEnter the course code (Enter '0' to Exit) : ")
    while Input_Grade_Course_Code != '0':
        if Input_Grade_Course_Code in Core_Course_Code + Student_Stream_Code:  # Combine Core and Elective Course
            if Input_Grade_Course_Code not in Grade_Course_Code:
                Input_Grade_Grades = input('Enter grade : ').upper()
                Grade_Course_Code.append(Input_Grade_Course_Code)
                Grade_Grades.append(Input_Grade_Grades)
                Grade_Course_Stream_Position = (Core_Course_Code + Student_Stream_Code).index(Input_Grade_Course_Code)
                Grade_Course_Stream.append((Core_Course_List + Student_Stream_Course)[Grade_Course_Stream_Position])
            else:
                print('This course Grade is already recorded in the system . ')
                Update_Grade = input('Do you want to update the grade ? (Y/N) : ').upper()
                if Update_Grade == 'Y':
                    Overwrite_Course_List_Position = Grade_Course_Code.index(Input_Grade_Course_Code)
                    Overwrite_Grade = input('Enter grade : ')
                    Grade_Grades[Overwrite_Course_List_Position] = Overwrite_Grade
            Input_Grade_Course_Code = input("\nEnter the course code (Enter '0' to Exit) : ")
        else:
            print('\nYou do not have this course in your stream ! ')
            time.sleep(1)
            Grade()
    print('\nQuiting to main menu ... ')
    time.sleep(1)
    student()


def Results():
    if Grade_Course_Code:
        Total_Credit_Hour = 0
        Total_Point = 0
        CGPA = 0
        print("Code        Grades     Course Name")
        print("--------------------------------------------------------")
        for i in range(1, len(Grade_Course_Code) + 1, 1):
            print(*Grade_Course_Code[i - 1:i], "  ", *Grade_Grades[i - 1:i], "        ", *Grade_Course_Stream[i - 1:i])
            Total_Credit_Hour += int(str(Grade_Course_Code[i - 1])[-1:])
            if 'A+' in Grade_Grades[i - 1:i] or 'A' in Grade_Grades[i - 1:i]:
                Total_Point += 4
            elif 'A-' in Grade_Grades[i - 1:i]:
                Total_Point += 3.67
            elif 'B+' in Grade_Grades[i - 1:i]:
                Total_Point += 3.33
            elif 'B' in Grade_Grades[i - 1:i]:
                Total_Point += 3.00
            elif 'B-' in Grade_Grades[i - 1:i]:
                Total_Point += 2.67
            elif 'C+' in Grade_Grades[i - 1:i]:
                Total_Point += 2.33
            elif 'C' in Grade_Grades[i - 1:i]:
                Total_Point += 2.00
            elif 'F' in Grade_Grades[i - 1:i]:
                Total_Point += 0.00
            else:
                print("\nInvalid Grades detected", "---->", Grade_Grades[i - 1:i])
                print("Please use the 'Update Grade Function to overwrite it' (Select 2 at main menu) ")
                time.sleep(1)
                student()
            CGPA = Total_Point / i
        print("\nTotal Credit Hour : ", Total_Credit_Hour)
        print("CGPA : ", round(CGPA, 2))
        input('\nPress Enter to go back to main menu')
        student()
    else:
        print('\nThere is no grades being recorded')
        input('Press "Enter" to go back to main menu')
        student()


def Other():
    print("Coming Soon")
    time.sleep(1)
    student()


def student():
    print("\nStudent's ID = ", ID)
    print("Name = ", Name)
    print("Stream", Stream)
    print("\n1. View Course List")
    print("2. Enter or Update Grade")
    print("3. View Results")
    print("4. Other Functions")
    print("0. Log Out")
    select_1 = input("\nSelect the service you required from the list above : ")
    if select_1 == '0':
        print('\nLogging Out .... ')
        login()
    elif select_1 == '1':
        Course()
    elif select_1 == '2':
        Grade()
    elif select_1 == '3':
        Results()
    elif select_1 == '4':
        Other()
    else:
        print('Please enter the options from 1 ~ 4 only')
        student()


def login():
    global ID
    ID = input("Please key in your Student ID (Exp: 2103301) : ")
    check()


def check():
    global ID
    global Name
    global Stream
    global List_Position
    global Student_Stream_Code
    global Student_Stream_Course
    while ID not in ID_list:  # Check whether this user's data is available or not
        if ID == '1234567':
            staff()
        else:
            print("User ID can't be found in the database, please try again")
            ID = input("Please key in your Student ID (Exp: 2103301) : ")
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
    student()
# -----------------------------------------------------Values--------------------------------------------------------


Core_Course_List = ['Effective Communication Skills', 'English for Academic Study', 'Mathematics I', 'Mathematics II',
                    'Mathematics III', 'Organic Chemistry', 'Physical Chemistry']
Core_Course_Code = ['FHHM1022', 'FHEL1012', 'FHMM1014', 'FHMM1024', 'FHMM1034', 'FHSC1124', 'FHSC1114']

Stream_1_Course_List = ['Fundamentals of Cell Biology', 'Inorganic Chemistry', 'Introduction to Physiological Systems',
                        'Modern Biology', 'Physics I', 'Physics II', 'Programming Concept']
Stream_1_Code_List = ['FHSC1214', 'FHSC1134', 'FHSC1224', 'FHSC1234', 'FHSP1014', 'FHSP1024', 'FHCT1022']

Stream_2_Course_List = ['Mechanics', 'Thermodynamics and Electromagnetism', 'Waves and Modern Physics',
                        'Inorganic Chemistry', 'Programming Concepts', 'Biology I', 'Biology II']
Stream_2_Code_List = ['FHSC1014', 'FHSC1024', 'FHSC1034', 'FHSC1134', 'FHCT1022', 'FHSB1214', 'FHSB1224']

Stream_3_Course_List = ['Computing Technology', 'Introduction to Data Analytics', 'Programming Concepts and Design',
                        'Management', 'Mechanics', 'Thermodynamics and Electromagnetism', 'Biology I']
Stream_3_Code_List = ['FHCT1012', 'FHCT1014', 'FHCT1024', 'FHBM1114', 'FHSC1014', 'FHSC1024', 'FHSB1214']

ID_list = ['2103301', '2103302', '2103303']  # 1st student ID = 2103301
Name_list = ["Josh", "Jack", "Jason"]  # 1st student name = Josh
Stream_list = ['1', '2', '3']  # 1st student stream = Stream 1

Grade_Course_Code = []
Grade_Grades = []
Grade_Course_Stream = []

ID = []
List_Position = []
Name = []
Stream = []
Student_Stream_Code = []
Student_Stream_Course = []

# -----------------------------------------------------------SYSTEM----------------------------------------------------
print("----------------------------------------------------------")
print("              WELCOME TO THE CGPA CALCULATOR              ")
print("----------------------------------------------------------")
login()
