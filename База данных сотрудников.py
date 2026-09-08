company={
    'IT': {
        'руководитель': 'Иванов Иван',
        'сотрудники': {
            'Петров Петр': {'телефон': '+79990001122', 'должность': 'Разработчик', 'зарплата': 100000},
            'Сидоров Сидор': {'телефон': '+79990003344', 'должность': 'Тестировщик', 'зарплата': 80000}
        }
    },
    'Бухгалтерия': {
        'руководитель': 'Петрова Анна',
        'сотрудники': {
            'Смирнова Ольга': {'телефон': '+79990005566', 'должность': 'Бухгалтер', 'зарплата': 70000}
        }
    }
}

def show_info_department():
    try:
        search_department = input("Введите название отдела: ").strip().lower()
        found_dept = False
        director = "не назначен"
        employees = []
        with open('учёт сотрудников.txt', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                line_split = line.split("|")
                if len(line_split) == 3 and line_split[0].lower()==search_department:
                    director = line_split[2]
                    found_dept = True
                elif len(line_split) == 5 and line_split[0].lower() == search_department:
                    department, name, phone, position, salary = line_split
                    employees.append({
                        'имя': name,
                        'телефон': phone,
                        'должность': position,
                        'зарплата': salary})
                    found_dept = True
        if found_dept:
            print(f"{search_department}: Руководитель: {director}")
            print('-'*30)
            for i, emp in enumerate(employees, 1):
                print(f"{i}. Сотрудник: {emp['имя']}")
                print(f"   Телефон: {emp['телефон']}")
                print(f"   Должность: {emp['должность']}")
                print(f"   Зарплата: {emp['зарплата']}")
                print()
        else:
            print("Такой отдел не найден")

    except FileNotFoundError:
        print("Файл не найден")

def find_name():
    try:
        search_name = input("Введите имя сотрудника для поиска: ").strip().lower()
        spisok = []
        with open('учёт сотрудников.txt', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                search_name_info = line.split('|')
                if len(search_name_info) != 5:
                    continue
                department, name, phone, position, salary = search_name_info
                if search_name in search_name_info[1].lower():
                    spisok.append({
                        'отдел': department,
                        'имя': name,
                        'телефон': phone,
                        'должность': position,
                        'зарплата': salary})
        if not spisok:
            print(f"Имя {search_name} не найдено.")
            return
        print(f"Результат для {search_name}: ")
        print(f"Найдено {len(spisok)} имён:")
        print("="*30)
        for i, emp in enumerate(spisok, 1):
            print(f"{i}. Отдел{emp['отдел']}")
            print(f"   Сотрудник: {emp['имя']}")
            print(f"   Телефон: {emp['телефон']}")
            print(f"   Должность: {emp['должность']}")
            print(f"   Зарплата: {emp['зарплата']}")
            print()
    except FileNotFoundError:
        print("Файл не найден. Проверьте правильность имени файла")




def read_file():
    try:
        with open('учёт сотрудников.txt','r',encoding='utf-8')as file:
            company_read = file.readlines()
            for line in company_read:
                print(line.strip())
    except FileNotFoundError:
        print("Такого файла нет")


def save_company_to_file():
    global company
    if not company:
        print("Нет данных для сохранения")
        return False
    try:
        with open('учёт сотрудников.txt','w',encoding='utf-8')as file:
            for department_name, department_info in company.items():
                manager_name = department_info["руководитель"]
                manager_line = f"{department_name}|руководитель|{manager_name}\n"
                file.write(manager_line)
                employees = department_info["сотрудники"]
                for employee_name, employee_info in employees.items():
                    line = (f"{department_name}|{employee_name}|"
                            f"{employee_info['телефон']}|"
                            f"{employee_info['должность']}|{employee_info['зарплата']}\n")
                    file.write(line)
            print("Файл сохранен успешно")
            return True
    except (PermissionError,OSError)as e:
        print(f"Ошибка записи: {e}")


def abb_department():
    global company
    dept_name = "Отдел маркетинга"
    # Проверка на дубликат
    if dept_name in company:
        print(f"Отдел '{dept_name}' уже существует!")
        return
    # Добавляем отдел и сотрудников
    company[dept_name] = {
        'руководитель': 'Петрова М.С.',
        'сотрудники': {
            "Иван": {
                'телефон': "666-66-66",
                'должность': "Маркетолог",
                'зарплата': 60000
            }
        }
    }

    print("Данные добавлены")
    save_company_to_file()


def load_company_from_file():
    global company
    try:
        with open('учёт сотрудников.txt','r',encoding='utf-8') as file:
            global company
            company = {}
            for line in file:
                line = line.strip().split('|')
                if len(line) == 3 and line[1]=="руководитель":
                    department, _,name  = line
                    company[department]={'руководитель':name,'сотрудники':{}}
                elif len(line) == 5:
                    department, name, phone, position, salary = line
                    if department not in company:
                        company[department] = {'руководитель': 'не назначен', 'сотрудники': {}}
                    try:
                        company[department]['сотрудники'][name]={
                            'телефон':phone,
                            'должность':position,
                            'зарплата':int(salary)}
                    except ValueError:
                        print("Ошибка зарплаты. Зарплата не число")
                        continue
            return  company
    except FileNotFoundError:
        print("Файл не найден")
        company={}
        return {}

while True:
    try:
        print("=" * 30)
        print("МЕНЮ")
        print("=" * 30)
        print("""
            1. Просмотр данных отдела
            2. Данные сотрудника
            3. Загрузить файл
            4. Сохранить в файл
            5. Добавить отдел
            6. Выход
            """)
        choice = int(input("Выберите пункт меню:"))
        if choice == 1:
            show_info_department()
        elif choice == 2:
            find_name()
        elif choice == 3:
            company = load_company_from_file()
        elif choice == 4:
            save_company_to_file()
        elif choice == 5:
            abb_department()
        elif choice == 6:
            print("До свидания!")
            break
        else:
            print("Такого пункта нет.")
    except ValueError:
        print("Введите пункт меню цифрой")

