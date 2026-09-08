import csv


class Employee:
    def __init__(self, name, department, salary, experience):
        self.name = name
        self.department = department
        self.salary = salary
        self.experience = experience

    def to_dict(self):
        return {
            'name': self.name,
            'department': self.department,
            'salary': self.salary,
            'experience': self.experience
        }

    def show_info(self):
        print(f"Имя: {self.name}")
        print(f"Отдел: {self.department}")
        print(f"Зарплата: {self.salary}")
        print(f"Стаж: {self.experience} лет")

    def __str__(self):  ### для printa в одну строку
        return f"{self.name} - {self.department} - {self.salary} руб., стаж {self.experience} лет"

    def to_csv_row(self):  ### для сохранения  (CSV, JSON, API)
        return f"{self.name},{self.department},{self.salary},{self.experience}"

    def raise_salary(self, percent):
        self.salary = self.salary * (1 + percent / 100)
        print(f"Имя: {self.name}")
        print(f"Отдел: {self.department}")
        print(f"✅ Зарплата {self.name} повышена на {percent}%. Теперь: {self.salary}")
        print(f"Стаж: {self.experience} лет")


class EmployeeManager:
    def __init__(self):
        self.employees = []  # ← здесь хранятся объекты Employee
        self.employees_by_name = {}  # ← словарь для быстрой проверки

    def load_from_csv(self, filename):
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.employees = []  # ← очищаем список перед загрузкой
                self.employees_by_name = {}  # ← очищаем словарь
                for row in reader:
                    emp = Employee(
                        name=row['name'],
                        department=row['department'],
                        salary=int(row['salary']),
                        experience=int(row['experience'])
                    )
                    self.employees.append(emp)  # ← добавляем объект Employee в список
                    self.employees_by_name[emp.name] = emp  # ← добавляем в словарь
            print(f"✅ Загружено {len(self.employees)} сотрудников из {filename}")
        except FileNotFoundError:
            print(f"❌ Файл {filename} не найден.")
        except KeyError as e:
            print(f"❌ Ошибка в данных: отсутствует колонка {e}")

    def show_all_employees(self):
        return self.employees  # ← возвращает список;

    def add_employee(self, employee):
        if employee.name in self.employees_by_name:
            print(f"⚠️ Сотрудник {employee.name} уже есть. Пропускаем.")
            return
        self.employees_by_name[employee.name] = employee
        self.employees.append(employee)
        try:
            with open('employees.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([employee.name, employee.department, employee.salary, employee.experience])
                print("✅Файл успешно сохранён")
        except Exception as e:
            print(f"⚠️ Ошибка сохранения: {e}")


def main():
    # 1. Создаём менеджера
    manager = EmployeeManager()

    # 2. Загружаем данные из CSV (вызываем метод)
    manager.load_from_csv('employees.csv')
    while True:

        print('-' * 20)
        print('МЕНЮ')
        print('-' * 20)
        print("""
1. Показать всех сотрудников
2. Перезагрузить данные из файла CSV
3. Добавить сотрудника
0. Выход""")
        try:
            choice = int(input('Выберите пункт меню.'))
            print(('-' * 20))
            if choice == 1:
                print("Список всех сотрудников:")
                print(('-' * 20))
                for emp in manager.show_all_employees():
                    print(emp)

            elif choice == 2:
                manager.load_from_csv('employees.csv')

            elif choice == 3:
                name = input("Введите имя сотрудника:").title()
                department = input("Введите название отдела:")
                salary = int(input("Введите зарплату сотрудника"))
                experience = int(input("Введите стаж работы:"))
                employee = Employee(name, department, salary, experience)
                manager.add_employee(employee)

            elif choice == 0:
                print('До свидания!')
                break

        except ValueError:
            print("❌Ошибка ввода. Введите номер пункта.")


if __name__ == "__main__":
    main()
