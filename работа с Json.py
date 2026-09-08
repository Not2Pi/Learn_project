import json
try:
    with open ('students.json', 'r', encoding='utf-8') as file:
        students = json.load(file)
        min_grade = float('inf')
        max_average_grade = 0
        min_student = []
        max_student = []
        courses = {}
        for row in students:
            name = row['name']
            age = row['age']
            course = row['course']
            average_grade = row['average_grade']
            print(f"{name} — {age} лет, курс {course}, средний балл {average_grade}")
            if average_grade > max_average_grade:
                max_average_grade = average_grade
                max_student = [name, average_grade]
            if average_grade < min_grade:
                min_grade = average_grade
                min_student =[name, average_grade]
            if course not in courses:
                courses[course] = [name]
            else:
                courses[course].append(name)
        for course, name in courses.items():
            print(f"Студенты {', '.join(name)} - курс {course}")
        print(f"Студент с самым высоким средним баллом: {max_student[0]} - балл - {max_average_grade}")
        print(f"Студент с самым низким средним баллом: {min_student[0]} - балл - {min_grade}")
        print(f"Общее количество студентов: {len(students)} человек.")
        # После всех расчётов создаём словарь result
        result = {"best_student":{'name':max_student[0],'grade':max_average_grade},
                 "worst_student": {"name": min_student[0], "grade": min_grade},
                "total_students": len(students),
                "students_by_course": courses}
except FileNotFoundError:
    print("❌Ошибка. Файл не найден")
    # Сохраняем в JSON
try:
    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, indent=2, ensure_ascii=False)
        print(f"✅Файл result успешно сохранён.")
except Exception as e:
    print(f"❌ Ошибка сохранения: {e}")





