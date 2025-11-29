print("Hello world!")

def filter_students(students, average):
    filtered = []
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg > average:
            filtered.append(student)
    return filtered

avg = float(input("Введите средний балл для фильтрации: "))
filtered = filter_students(groupmates, avg)
print_students(filtered)  

def filter_students(students, average):
    filtered = []
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg > average:
            filtered.append(student)
    return filtered

avg = float(input("Введите средний балл для фильтрации: "))
filtered = filter_students(groupmates, avg)
print_students(filtered) 

