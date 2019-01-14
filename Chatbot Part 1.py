
#Reading the student records txt file


user_input = input("(Type END to stop playing) Enter a study unit: ")

while user_input != "END":
    student_records = open("StudentRecords.txt","r")
    for line in student_records:
        if user_input in line:
            values = line.split()
            print(user_input+",",  values[4]+",","is a "+ values[1]+" study unit.")
            print(user_input)
    user_input = input("(Type END to stop playing) Enter a study unit: ")

    student_records.close()
