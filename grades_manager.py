
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
def get_students(student_grades, keys):
    result= {}
    lresult = {}
    for name in student_grades:
        lname = name.lower()
        lresult[lname] = name
    for key in keys:
        lkey= key.lower()
        if lkey in lresult:
            nombreo = lresult[lkey]
            result[nombreo.title()] = student_grades[nombreo]
        else:
            print(f"{key.title()} not found!")
    return result
def avg_by_student(student_grades, keys=None):
    if keys is None:
        sele= student_grades
    else:
        sele = get_students(student_grades, keys)
    for student, materia in sele.items():    
        if materia:
            promedio = sum(materia.values()) / len(materia)
        else:
            promedio = 0
        print(f"{student}: {round(promedio,1)}")
