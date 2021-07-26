print("----------------------------------------------------------")
print("              WELCOME TO THE CGPA CALCULATOR              ")
print("----------------------------------------------------------")

ID = int(input("Please key in your Student ID : "))
while len(str(ID)) != 7:
    print("Invalid Student ID (Exp of correct Student ID > 2100111)")
    ID = int(input("Please key in your Student ID : "))

print("Student's ID = ", ID)
print("Name = ")
print("Stream")
