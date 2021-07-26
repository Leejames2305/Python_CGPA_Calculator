print("----------------------------------------------------------")
print("              WELCOME TO THE CGPA CALCULATOR              ")
print("----------------------------------------------------------")

ID = int(input("Please key in your Student ID : "))
while len(str(ID)) != 7:
    print("Invalid Student ID (Exp of correct Student ID: 2100111)")
    ID = int(input("Please key in your Student ID : "))


def staff():
    print(staff)


Name = "Unknown"
Stream = "Unknown"


def student():
    print("\nStudent's ID = ", ID)
    print("Name = ", Name)
    print("Stream", Stream)
    print("\n1. View Course List")
    print("2. Enter or Update Grade")
    print("3. View Results")
    print("4. Other functions")
    print("0. Quit")


if ID == 1234567:
    staff()
else:
    student()

Select_1 = int(input("\nSelect the service you required from the list above : "))

Course_List = ['adawd', 'dawdw']
Course_Code = ['12345678', '12345678']


def Course():
    print("Code        Course Name")
    print("--------------------------------------------------------")
    print(*Course_Code[0:1], "  ", *Course_List[0:1])


def Grade():
    print("Grade")


def Results():
    print("Results")


def Other():
    print("Other")


def main():
    if Select_1 == 1:
        Course()
    elif Select_1 == 2:
        Grade()
    elif Select_1 == 3:
        Results()
    elif Select_1 == 4:
        Other()


if Select_1 == 0:
    print("Thanks for using")
else:
    main()
