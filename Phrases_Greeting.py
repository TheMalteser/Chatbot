import random
#Reading the student records txt file

phrases_greeting = ["hello there", "how are you doing?", "ASK ME SOMETHING ELSE"]
phrases = ["Please type in the unit you are interested in", "I only understand unit codes", "I am the unit master"]

user_input = ''
print(random.choice(phrases_greeting))
while user_input != "END":
    flag = 0
    student_records = open("StudentRecords.txt","r")
    user_input = input("(Type END to stop playing) Enter a study unit: ")
    for line in student_records:
        if user_input in line:
            values = line.split()
            print(user_input+",",  values[4]+",","is a "+ values[1]+" study unit.")
            flag = 1
    if flag == 0:
        print(random.choice(phrases))        
            
         

    student_records.close()
