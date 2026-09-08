import csv
import json


def load_employees():
    try:
        with open('employees.csv', 'r', newline='', encoding='utf-8') as file:
            employees = list(csv.DictReader(file))
            return employees
    except FileNotFoundError:
        print("Файл не найден")
        return []


def show_employees(employees):
    print('-' * 20)
    print("Список сотрудников:")
    print('-' * 20)
    if not employees:
        print("Список пуст.")
    for row in employees:
        name = row['name']
        department = row['department']
        salary = int(row['salary'])
        experience = row['experience']
        print(f"Имя: {name}")
        print(f"Отдел: {department}")
        print(f"Зарплата: {salary}")
        print(f"Стаж работы: {experience}")
        print('-' * 20)


def add_employee(employees):
    name = input("Введите имя: ").capitalize()
    department = input("Введите отдел: ").capitalize()
    for emp in employees:
        if emp['name'] == name and emp['department'] == department:
            print("❌ Сотрудник с таким именем в этом отделе уже существует.")
            return  # выходим из функции
    salary = int(input("Введите зарплату: "))
    experience = int(input("Введите стаж работы: "))
    new_employee = {'name': name, 'department': department, 'salary': salary, 'experience': experience}
    employees.append(new_employee)
    try:
        with open('employees.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'department', 'salary', 'experience'])
            writer.writerow(new_employee)
            print(f"Сотрудник {name} успешно добавлен в отдел {department}.")
            print("✅Файл успешно обновлён.")
    except FileNotFoundError:
        print("❌Ошибка-Файл не найден.")


def find_by_department(employees, department):
    found = False
    find_name = []
    for row in employees:
        if row['department'].lower() == department.lower():
            find_name.append(row['name'])
            found = True
    if found:
        return f"🔍Сотрудники отдела {department}: {find_name}"
    else:
        return "❌Такой отдел не существует."


def find_by_salary_above(employees, min_salary):
    emp_name = []
    for row in employees:
        name = row['name']
        salary = int(row['salary'])
        if salary >= min_salary:
            emp_name.append(name)
    return emp_name


def avg_salary_by_department(employees):
    department_salaries = {}
    result = {}
    for row in employees:
        department = row['department']
        salary = row['salary']
        if department not in department_salaries:
            department_salaries[department] = [int(salary)]
        else:
            department_salaries[department].append(int(salary))
    for key, value in department_salaries.items():
        result[key] = sum(value) / len(value)
    return result


def save_stats_to_json(stats, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(stats, file, indent=2, ensure_ascii=False)
            print(f"✅Файл {filename} успешно сохранён!")
    except Exception as e:
        print(f"⚠️ Ошибка сохранения: {e}")


def main():
    employees = load_employees()
    while True:
        print("""
1. Показать всех сотрудников
2. Добавить нового сотрудника
3. Найти сотрудников по отделу
4.Найти сотрудников с зарплатой выше указанной
5. Посчитать среднюю зарплату по отделам
6. Сохранить (среднюю зарплату по отделам) в JSON
0. Выход""")
        choice = int(input("Выберите пункт меню: "))
        if choice == 1:
            show_employees(employees)
        elif choice == 2:
            add_employee(employees)
        elif choice == 3:
            department = input("Введите название отдела: ")
            print(find_by_department(employees, department))
        elif choice == 4:
            try:
                min_salary = int(input("Введите минимальную зарплату:"))
                print('-' * 20)
                print(f"Сотрудники с зарплатой выше {min_salary}руб.")
                print('-' * 20)
                print(find_by_salary_above(employees, min_salary))
            except ValueError:
                print("Ошибка ввода: Введите число.")
        elif choice == 5:
            print('-' * 20)
            print("Средняя зарплата по отделам:")
            print('-' * 20)
            result = avg_salary_by_department(employees)
            for key, value in result.items():
                print(f"Отдел: {key} - средняя зарплата {value} руб.")
        elif choice == 6:
            stats = avg_salary_by_department(employees)
            filename = 'avg_department.json'
            save_stats_to_json(stats, filename)

        elif choice == 0:
            print("❤️До свидания!")
            break


main()
