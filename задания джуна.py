from collections import Counter


def is_palindrome(r):
    # Убираем всё кроме букв и цифр, приводим к нижнему регистру
    result = ''.join(char.lower() for char in r if char.isalnum())  ###  СТРОКА ПАЛИНРДРОМ
    return result == result[::-1]  # Возвращает True   False


def sum_list(numbers):
    return sum(i for i in numbers if i > 0)  ###   СУММА ПОЛОЖИТЕЛЬНЫХ ЧИСЕЛ


def find_max(numbers):
    if not numbers:
        raise ValueError("⚠️Список пуст.")
    result = numbers[0]
    for i in numbers:
        if i > result:
            result = i
    return result


def count_vowels(s):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"  ###   КОЛИЧЕТСТВО ВХОЖДЕНИЙ
    return sum(1 for char in s if char in vowels)


def first_unique(s):
    counts = Counter(s)  # ← один проход: O(n)
    for i in s:  # ← второй проход: O(n)
        if counts[i] == 1:  # ← O(1) доступ к словарю
            return i
    return None


def is_anagram(s1, s2):
    res1 = Counter(s1)
    res2 = Counter(s2)
    if res1 == res2:
        return True
    return False


### или можно коротко
# def is_anagram(s1, s2):
#     return Counter(s1) == Counter(s2)

def find_duplicates(s):
    a = set()
    b = set()
    for i in s:
        lower = i.lower()
        if lower in a:
            b.add(lower)
        a.add(lower)
    return sorted(b)


# print(find_duplicates(["Apple", "banana", "apple", "Cherry", "banana", "DATE"]))

def group_by_age(users):
    result = {}
    for row in users:
        if 'name' not in row or 'age' not in row:
            continue
        age = row["age"]
        name = row["name"]
        if age not in result:
            result[age] = []
        if name not in result[age]:
            result[age].append(name)
    for age in result:
        result[age].sort()
    return result


# print(group_by_age([
#         {"name": "Alice", "age": 25},
#         {"name": "Bob", "age": 30},
#         {"name": "Charlie", "age": 25},
#     ]))

def count_lines_in_file(filepath):
    if not filepath:  # пустая строка
        return 0
    total = 0
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    total += 1
    except FileNotFoundError:
        return 0
    return total


def merge_dicts(*dicts):
    res = {}
    for d in dicts:
        for key, value in d.items():
            if key not in res:
                res[key] = value
            else:
                res[key] += value
    return res


# print(merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}, {"a": 5}))


def find_word_in_file(filepath, word):
    result = []
    for i, line in enumerate(filepath, start=1):
        if 'l'.lower() in line.lower():
            result.append(i)
    return result


def factorial(n):
    result = 1  ###    ФАКТОРИАЛ ЧИСЛА
    for i in range(1, n + 1):
        result *= i
    return result


def count_vowel(text):
    char = 'aeiou'
    return sum(1 for i in text.lower() if i in char)  ### СУММА ГЛАСНЫХ БУКВ В СТРОКЕ


def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])  ###  ПЕРЕВОРОТ СПИСКА


def find_max(numbers):
    if not numbers:
        return None
    max_number = numbers[0]  # ← берём первый элемент, не 0!
    for i in numbers[1:]:  # ← начинаем со второго  (не обязательно но лишняя итерация)
        if i > max_number:
            max_number = i
    return max_number


def is_prime(n):
    if n < 2:  # ← 0, 1, отрицательные — не простые
        return False  ###  ПРОВЕРКА ПРОСТОГО ЧИСЛА
    for i in range(2, n):  # ← проверяем делители от 2 до n
        if n % i == 0:
            return False  # ← нашли делитель, не простое
    return True  # ← делителей не нашли, простое


def has_duplicates(items):
    return len(set(items)) == len(items)  # ПОИСК ДУБЛИКАТОВ


def lists_to_dict(keys, values):
    res = {}
    for i, key in enumerate(keys):
        if i < len(values):
            res[key] = values[i]  # СЛОВАРЬ ИЗ 2 СПИСКОВ
        else:
            res[key] = None
    return res  ### или  return {key: values[i] if i < len(values) else None  for i, key in enumerate(keys)}


def filter_even(numbers):
    return [i for i in numbers if i % 2 == 0]  # принято так выше скорость лучше читаемость ### СПИСОК ЧЁТНЫХ ЧИСЕЛ
    # return list(filter(lambda x:x % 2 == 0, numbers))


def flatten(nested_list):
    res = []
    for i in nested_list:
        if isinstance(i, list):
            res.extend(flatten(i))  ### ВЛОЖЕННЫЙ СПИСОК В ПЛОСКИЙ СПИСОК
        else:
            res.append(i)
        ### или def flatten(nested_list):
        # res = []
        # for i in nested_list:
        #     res.extend(flatten(i) if isinstance(i, list) else [i])
        # return res
    return res


def count_words(text):
    res = {}
    for word in text.strip().split():
        clean_word = word.strip("!?.,;:").lower()
        if clean_word in res:
            res[clean_word] += 1  ###  ПОДСЧЁТ КОЛИЧЕСТВА СЛОВ В СТРОКЕ
        else:
            res[clean_word] = 1
    return res


def is_anagram(a, b):
    a = (char.lower() for char in a if char.isalpha())
    b = (char.lower() for char in b if char.isalpha())  ### аннаграмма
    return sorted(a) == sorted(b)


def fizzbuzz(n):
    res = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")  ### ПРОВЕРКА "FizzBuzz"
        elif i % 5 == 0:
            res.append("Buzz")
        elif i % 3 == 0:
            res.append("Fizz")
        else:
            res.append(str(i))
    return res


def find_missing(numbers):
    total = 0
    n = len(numbers) + 1
    for i in range(1, len(numbers) + 2):
        total += i  ### или по формуле    total = n * (n + 1) // 2
    return total - sum(numbers)


def flatten_dict(d):
    res = {}
    for key, value in d.items():
        if isinstance(value, dict):
            unpak_dict = flatten_dict(value)  ###  РАСПАКОВКА ВЛОЖЕННЫХ СЛОВАРЕЙ
            for unpak_key, unpak_value in unpak_dict.items():
                res[f"{key}.{unpak_key}"] = unpak_value
        else:
            res[key] = value
    return res


def get_unique(items):
    count = {}
    for i in items:
        if i not in count:  ### встречаются ровно один раз. Порядок сохранить.
            count[i] = 1
        else:  ###  или в 1 строку count[i] = count.get(i, 0) + 1
            count[i] += 1

    return [i for i in items if count[i] == 1]


def intersection(a, b):
    b = set(b)
    seen = set()
    res = []
    for i in a:
        if i in b and i not in seen:
            seen.add(i)
            res.append(i)
    return res


def is_balanced(text):
    total = 0
    for i in text:
        if i == '(':
            total += 1
        if i == ')':  ### ПРОВЕРКА  СКОБОК
            total -= 1
        if total < 0:
            return False
    return True if total == 0 else False


def remove_duplicates(items):
    result = []
    seen = set()
    for i in items:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result


def union(a, b):
    seen = set()
    result = []
    for i in a:
        if i not in seen:
            seen.add(i)
            result.append(i)  ###     СЛОЖЕНИЕ СПИСКОВ
    for i in b:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result


def difference(a, b):
    res_b = set(b)
    seen = set()
    result = []
    for i in a:
        if i not in seen and i not in res_b:  ###  ВЫЧИТАНИЕ СПИСКОВ
            seen.add(i)
            result.append(i)
    return result


def symmetric_difference(a, b):
    res_a = set(a)
    res_b = set(b)
    seen = set()
    result = []
    for i in a:
        if i not in seen and i not in res_b:
            seen.add(i)
            result.append(i)  ### Симметрическая разность
    for i in b:
        if i not in seen and i not in res_a:
            seen.add(i)
            result.append(i)
    return result


def is_power_of_two(n):
    if n <= 0:
        return False  ###  Проверка на степень двойки
    while n > 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True  ### return n > 0 and (n & (n - 1))==0  или return (n & (n - 1)) == 0


def sot_number():
    number = input('number').strip()
    if not number:
        print("Номер не введён")
        return None
    sort_number = ''.join(char for char in number if char.isdigit())  ### или ''.join(filter(str.isdigit, number)
    if sort_number[0] == '8' and len(sort_number) == 11:
        return '+7' + sort_number[1:]
    if sort_number[0] == '7' and len(sort_number) == 11:  ### ПРОВЕРКА СОТОВОГО НОМЕРА
        return '+7' + sort_number[1:]
    if sort_number[0] == '9' and len(sort_number) == 10:
        return '+7' + sort_number
    else:
        print('Не верный формат номера')
        return None


def sum_digits(n):
    return sum(int(i) for i in
               str(n).strip('-'))  # return sum(int(i) for i in str(abs(n))) abs(n) — модуль числа, вместо strip('-')


def reverse_number(n):
    result = []
    if n < 0:
        n = abs(n)  ###  переворачивает цифры числа
        for i in str(n)[::-1]:
            result.append(i)
        return int('-' + ''.join(result))  ### sign = -1 if n < 0 else 1
        # reversed_n = int(str(abs(n))[::-1])
        # return sign * reversed_n
    else:
        for i in str(n)[::-1]:
            result.append(i)
        return int(''.join(result))


def is_lucky_ticket(number):
    n = len(str(number)) // 2
    res_1 = sum(int(i) for i in str(number)[:n])  ###  СУММА ПОЛОВИНА ЧИСЛА
    res_2 = sum(int(i) for i in str(number)[n:])
    return res_1 == res_2


def count_divisors(n):
    return sum(1 for i in range(1, n + 1) if n % i == 0)  ###  Количество делителей


def reverse_number(n):
    sign = -1 if n < 0 else 1  ###  переворачивает цифры числа
    revers_n = int(str(abs(n))[::-1])
    return revers_n * sign


def two_sum(nums, target):
    res = {}
    for i, num in enumerate(nums):
        rest = target - num  ###  индексы двух чисел
        if rest in res:
            return [res.get(rest), i]  # ← можно просто return res[rest], i
        else:
            res[num] = i


def is_subsequence(s, t):
    s_index = 0
    for char in t:
        if s_index < len(s) and char == s[s_index]:
            s_index += 1  ### Проверка на подпоследовательность
            if s_index == len(s):
                return True
    return False


def is_number_palindrome(n):
    str_n = str(n)  ### палиндром числа
    if n < 0:
        return False
    return str_n == str_n[::-1]  ### или  return n >= 0 and str(n) == str(n)[::-1]


def find_missing_number(nums):
    res_total = sum(int(i) for i in range(len(nums) + 1))
    total = sum(int(i) for i in nums)  ### full_sum = n * (n + 1) // 2  метод гаусса
    return res_total - total


def intersect(nums1, nums2):
    num_1 = {}
    res = []  ### Пересечение двух массивов II
    for i in nums1:
        num_1[i] = num_1.get(i, 0) + 1
    for i in nums2:
        if i in num_1 and num_1[i] > 0:
            res.append(i)
            num_1[i] -= 1
    return res


def gcd(a, b):
    while b != 0:
        a, b = b, a % b  ### НОД УРАВНЕНИЕ ЕВКЛИДА
    return a


def is_leap_year(year):
    if year % 400 == 0:
        return True  ### ВИСОКОСНЫЙ ГОД
    if year % 100 == 0:
        return False
    else:
        return year % 4 == 0


def lcm(a, b):
    orig_a, orig_b = a, b
    while b != 0:
        a, b = b, a % b  # нашли НОД                                               ###  НОК
    return orig_a * orig_b // a  # нашли НОК


def is_perfect_square(n):
    sqrt_n = n ** 0.5
    return sqrt_n == int(sqrt_n)  ###   ПОЛНЫЙ КВАДРАТ ЧИСЛА


def is_subsequence(a, b):
    total = 0  # длина a
    j = 0  # ограничение списка b                                            ### ПОДСТРОКА
    while j < len(b) and total < len(a):
        if b[j] == a[total]:
            total += 1
        j += 1
    return total == len(a)


def sort_by_value(d):
    return sorted(d, key=lambda x: d[x])  ###      сортирует ключи по значению


def first_uniq_char(s):
    res = {}
    res_s = list(s)
    for i, num in enumerate(res_s):
        res[num] = res.get(num, 0) + 1
    for i in res_s:
        if res[i] == 1:
            return i
    return -1


def flatten_dict(d):
    result = {}
    for key, values in d.items():
        if isinstance(values, dict):
            unpack = flatten_dict(values)  ### РАСПАКОВКА  ВЛОЖЕННЫЕ СЛОВАРИ
            for un_key, un_value in unpack.items():
                result[f"{key}.{un_key}"] = un_value
        else:
            result[key] = values
    return result


def show_products(purchases):
    unik_products = set(purchases)
    products = {}
    for product in purchases:
        products[product] = products.get(product, 0) + 1
    for i in unik_products:
        print(i)
    for key, value in products.items():
        print(f"{key}- {value}")


def word_frequency(filepath):
    try:
        with open(filepath, 'r', encoding="utf-8") as file:
            text = file.read().lower().split()  ###  ЧТЕНИЕ ФАЙЛА
            c = Counter(text)
            ## или words = []
            # for line in file:
            #     words.extend(line.lower().split())
            return c.most_common(3)
    except FileNotFoundError:
        return {}


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a  # ← ОТДАЙ 0 и ЗАМРИ                      ЧИСЛА ФЕБОНАЧИ
        a, b = b, a + b  # ← когда разбудят, обнови числа


def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a  ### ЧИСЛА ФЕБОНАЧИ
        temp_a = a
        a = b
        b = temp_a + b


def add_frame(func):
    def wrapper():
        print('+------+')
        result = func()
        print("+------+")  ###       ДЕКОРАТОРЫ
        return result

    return wrapper


@add_frame
def get_name():
    print("Алиса")
    return "Алиса"


def even_numbers(n):
    if n < 2:
        return  ###  YIELD
    for i in range(2, n + 1, 2):
        yield i


def most_common_word(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read().lower().split()
            if not text:
                return None
            res = Counter(text)
            return res.most_common(1)[0]
    except FileNotFoundError:
        return None


def words_by_frequency(filepath):
    result = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read().lower().split()
            if not text:
                return None
            res = Counter(text)
            for key, value in res.items():
                if value not in result:
                    result[value] = [key]
                else:
                    result[value].append(key)
            for word in result.values():
                word.sort()
            return result
    except FileNotFoundError:
        return None


def group_by_length(filepath):
    result = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read().lower().split()
            if not text:
                return None
            res = set(text)
            for word in res:
                len_word = len(word)
                if len_word not in result:
                    result[len_word] = [word]
                else:
                    result[len_word].append(word)
            for words in result.values():
                words.sort()
            return result
    except FileNotFoundError:
        return None


from collections import defaultdict


def group_by_first_letter(filepath):
    result = defaultdict(list)
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read().lower().split()  ### defaultdict(list)
            if not text:
                return None
            words = set(text)
            for word in words:
                result[word[0]].append(word)
            for value in result.values():
                value.sort()
        return dict(result)

    except FileNotFoundError:
        return None


def get_most_frequent_word(text):
    result = {}
    text_clean = text.strip().split()  ### САМОЕ ЧАСТОЕ СЛОВО В СПИСКЕ
    for char in text_clean:
        result[char] = result.get(char, 0) + 1
    res = sorted(result, key=lambda p: result[p], reverse=True)
    return res[0]


from datetime import datetime


def get_weekday(date_str):
    date = datetime.strptime(date_str, "%d.%m.%Y")
    week = date.weekday()
    days = {
        0: "Понедельник",
        1: "Вторник",
        2: "Среда",
        3: "Четверг",
        4: "Пятница",
        5: "Суббота",                                        ### находим день недели
        6: "Воскресенье"
    }
    return days[week]


def countdown(n):
    for i in range(n, -1, -1):
        yield i  ### range в обратном порядке


from datetime import datetime, date, time, timedelta


def date_difference(date1, date2):
    date1 = datetime.strptime(date1, "%d.%m.%Y")  ###  разница даты
    date2 = datetime.strptime(date2, "%d.%m.%Y")
    return abs((date2 - date1).days)


def days_until_new_year():
    date_now = datetime.now()
    next_year = date_now.year + 1
    new_year = datetime(next_year, 1, 1)  ###  До нового года дней
    res = (new_year - date_now).days
    return res


def uppercase_decorator(funk):
    def upper():
        res = funk()
        return res.upper()  ###   Декоратор

    return upper


@uppercase_decorator
def get_greeting():
    return "hello world"


def countdown(n):
    for i in range(n, -1, -1):
        yield i


