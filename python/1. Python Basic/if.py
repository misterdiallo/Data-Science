bachelor = ["andrea", "yacine", "marcia"]
master = ["alpha", "fred", "connard"]
phd = []

student = input("Enter the student name : ")

if student in bachelor:
    print(student, " is a bachelor student")
elif student in master:
    print(student, " is a master student")
elif student in phd:
    print(student, " is a phD student")
else:
    print("This student is not in the database")