def reverse_range(n):
    return list(range(n, -1, -1))

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

def clean_words(text):
    text_clean = text.split()
    return [char.strip("!?.,;:") for char in text_clean]

def get_unique(lst):
    res = set(lst)
    result = []
    for i in lst:
        if i not in result and i in res:
            result.append(i)
    return result

def read_file_safe(filename):
    try:
        with open(filename,'r',encoding='utf-8')as file:
            read_file =  file.readlines()
            return read_file
    except FileNotFoundError:
        return 'Файл не найден'
    except Exception as d:
        return f"Ошибка: {d}"

def sum_all(*args):
    return sum(args)

def print_book_info(title, author, **kwargs):
    print(f"Название: {title}, Автор: {author}")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def collect_data(first, *args, **kwargs):
    result = {}
    result['first']=first
    result ["args"] = (args)
    result["kwargs"]=kwargs
    return result   ###  return {"first": first, "args": args, "kwargs": kwargs}

def is_even(n):
    return n%2==0

def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    print("Тесты прошли успешно")


def merge_dicts(d1, d2):
    res = d1.copy()
    res.update(d2)
    return res          ### или return {**d1, **d2}            ### ОБЪЕДИНЕНИЕ СЛОВАРЕЙ

