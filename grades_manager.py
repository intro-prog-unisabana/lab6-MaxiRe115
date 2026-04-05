
def initialize_dict(student_name, student_grades):
    return {student_name: student_grades}
def add_student(student_grades):
    nuevo ={}
    name = input("Enter student name: ").title()
    while True:
        mn= input("Enter subject and grade (or 'exit' to finish): ").lower()
        if mn == 'exit':
            break
        nombre, nota = mn.split(",")    
        nombre = nombre.title().strip()
        nota = float(nota.strip())
        nuevo[nombre] = nota
    student_grades[name]= nuevo
    print(f"Student {name} successfully added to the grades management system.")
    return student_grades
student_data = {}
updated_data = add_student(student_data)
        

