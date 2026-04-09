from grades_manager import *
print("Welcome to the Student Grades Manager!")
my_grades = {}
while True:
    option= input("""Select an option:  
1. Add a student   
2. Print student grade averages
3. Exit\n  """)
    if option == '1':
        agregar =  add_student(my_grades)
    elif option == '2':
        pregunta = input("""Select an option:  
a. Display all students  
b. Display selected students\n  """).lower()
        if pregunta == 'a':
            promedio= avg_by_student(my_grades)
        elif pregunta == 'b':
            names = input("Enter student names (comma-separated):\n")
            namesl= names.split(",")
            keys= []
            for name in namesl:
                lnames = name.strip()
                keys.append(lnames)
            avg_by_student(my_grades, keys)
        else:
            print("Invalid option selected!")
    elif option == '3':
        print("Goodbye!")
        break
    else: 
        print("Invalid option selected!")
