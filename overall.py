my_dict = {
  "s1": {"hw1": 80, "hw2": 90, "hw3": 100},
  "s2": {"hw1": 70, "hw2": 75, "hw3": 85},
  "s3": {"hw1": 95, "hw2": 85, "hw3": 90}
}
def student_averages(my_dict):
    r= {}
    for students, asignaturas in my_dict.items():
        total = 0
        cuantas= 0
        for nota in asignaturas.values():
            total += nota
            cuantas += 1
        if cuantas > 0:
            r[students] = round(total / cuantas)
        else:
            r[students] = 0
    return r
def assignment_averages(my_dict):
    t= {}
    c= {}
    for students, asignaturas in my_dict.items():
        for tarea, nota in asignaturas.items():
            t[tarea] = t.get(tarea, 0) + nota
            c[tarea] = c.get(tarea, 0) + 1
    p= {}
    for tarea in t:
        p[tarea] = round(t[tarea] / c[tarea], 2 )

