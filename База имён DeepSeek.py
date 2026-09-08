def add_first_name():
    with open('проект база имён.txt','w',encoding='utf-8') as names:
        names.write("Анна"+'\n')
        print("Файл создан и имя Анна добавлено!")

def show_all_names():
    try:
        with open('проект база имён.txt','r',encoding='utf-8') as names:
            name = names.readlines()
            if name:
                for i, children in enumerate(name, 1):
                    print(f"{i}. {children.strip()}")
    except FileNotFoundError:
        print('Список имен пуст')


def add_one_name():
    try:
        name = input("Введите имя: ").title()
        with open('проект база имён.txt','r', encoding='utf-8') as names:
            names_new = names.readlines()
            if name in [item.strip() for item in names_new]:
                print("Такое имя уже существует")
            else:
                with open('проект база имён.txt', 'a', encoding='utf-8') as names:
                    names.write(name + '\n')
                    print("Имя успешно добавлено")
    except FileNotFoundError:
        print("Файл не найден")



def delete_one_name():
    with open('проект база имён.txt','r',encoding='utf-8') as names:
        names_new = names.readlines()
        show_all_names()
        choice = int(input("Введите номер: "))
        choice = choice - 1
        if 0<=choice<len(names_new):
            names_new.pop(choice)
            print("Имя удалено")
        else:
            print("Некорректный номер")
    with open('проект база имён.txt', 'w', encoding='utf-8') as names:
        for name in names_new:
            names.write(name)
        print("Файл успешно обновлён")

def find_name():
    search_name = input("Введите имя для поиска: ").title()
    try:
        with open('проект база имён.txt', 'r', encoding='utf-8') as names:
            names_new = names.readlines()
            found = False
            for items in names_new:
                clean_name = items.strip()
                if search_name.lower() in clean_name.lower():
                    found = True
                    print(f"Имя {search_name} найдено!")
            if not found:
                print(f"Имя {search_name} не найдено")
    except FileNotFoundError:
        print("Файл не найден")

def edit_name():
    try:
        with open('проект база имён.txt','r',encoding='utf-8')as name:
            read_name = name.readlines()
            if read_name:
                show_all_names()
                choice = int(input("Введите номер имени для редактирования: "))
                name_count = choice-1
                if 0<= name_count <len(read_name):
                    new_name = input("Введите новое имя: ")
                    read_name[name_count] = new_name+'\n'
                    print(f"Имя успешно изменено на {new_name}")
                    with open('проект база имён.txt', 'w', encoding='utf-8') as name:
                        for i in read_name:
                            name.write(i)
                    print("Файл успешно обновлён")
                else:
                    print("Некорректный номер")
            else:
                print("Список имен пуст")
    except FileNotFoundError:
        print("Такой файл не найден")

def clear_names():
    try:
        with open('проект база имён.txt','r',encoding='utf-8') as name:
            open_file = name.read()
            if open_file:
                choice = input("Вы уверены, что хотите удалить все имена? (да/нет): ").lower()
                while choice not in ['д', 'да', 'н', 'нет']:
                    choice = input("Введите да/нет").lower()
                if choice in['д', 'да']:
                    with open('проект база имён.txt', 'w', encoding='utf-8') as name:
                        name.write('')
                        print("Файл успешно очищен")
                elif choice in['н', 'нет']:
                    print("Операция отменена")
            else:
                print("Список имен пуст")
    except FileNotFoundError:
        print("Файл не найден")


while True:
    print("=" * 30)
    print("МЕНЮ")
    print("=" * 30)
    print("""
    1. Показать все имена
    2. Добавить имя
    3. Удалить имя
    4. Найти имя
    5. Редактировать имя
    6. Очистить все имена
    7. Выход
    """)
    choice = input("Выберите пункт меню").strip()
    if not choice:
        print("Вы ничего не ввели. Попробуйте снова.")
        continue
    if choice == '1':
        show_all_names()
    elif choice == '2':
        add_one_name()
    elif choice == '3':
        delete_one_name()
    elif choice == '4':
        find_name()
    elif choice == '5':
        edit_name()
    elif choice == '6':
        clear_names()
    elif choice == '7':
        print("До свидания")
        break
    else:
        print("Не корректный ввод")