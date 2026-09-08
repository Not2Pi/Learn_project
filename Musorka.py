
def filter_numbers(n):
    return list(i for i in n if i%2 == 0)


def count_words(n):
    result = {}
    text = n.strip().split()
    for word in text:
        result[word]= result.get(word, 0)+1
    return result

def get_most_frequent_word(text):
    result = {}
    text_clean = text.strip().split()
    for char in text_clean:
        result[char]=result.get(char,0)+1
    res = sorted(result, key=lambda p: result[p], reverse=True)
    return res[0]

def invert_dict(n):
    new_dict = {}
    for key, value in n.items():
        if value not in new_dict:
            new_dict[value]=[]
        new_dict[value].append(key)
    return new_dict

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


def gcd(a, b):
    while b!=0:
        a,b=b,a%b                                                   #нашли НОД
    return a

def lcm(a, b):
    orig_a, orig_b = a, b
    while b!=0:
        a,b=b,a%b    #нашли НОД                                        ###  НОК
    return orig_a * orig_b // a #нашли НОК

def is_perfect_square(n):
    sqrt_n = n ** 0.5
    return sqrt_n == int(sqrt_n)                         ###   ПОЛНЫЙ КВАДРАТ ЧИСЛА

def is_subsequence(a, b):
    total = 0    #длина a
    j = 0        #ограничение списка b                                            ### ПОДСТРОКА
    while j < len(b) and total < len(a):
        if b[j] == a[total]:
            total += 1
        j += 1
    return total == len(a)

def sort_by_value(d):
    return sorted(d, key=lambda x: d[x])                 ###      сортирует ключи по значению



from datetime import datetime
def get_weekday(date_str):
    date=datetime.strptime(date_str, "%d.%m.%Y")
    week=date.weekday()
    days = {
    0: "Понедельник",
    1: "Вторник",
    2: "Среда",
    3: "Четверг",
    4: "Пятница",
    5: "Суббота",                                  ### находим день недели
    6: "Воскресенье"
}
    return days[week]

def days_until_new_year():
    date_now = datetime.now()
    next_year = date_now.year + 1
    new_year = datetime(next_year,1,1)        ###  До нового года дней
    res = (new_year - date_now).days
    return res

def uppercase_decorator(funk):
    def upper():
        res = funk()
        return res.upper()                               ###   Декоратор
    return upper

@uppercase_decorator
def get_greeting():
    return "hello world"

def countdown(n):
    for i in range(n,-1,-1):
        yield i                                            ### range в обратном порядке

from datetime import datetime, date, time, timedelta
def date_difference(date1, date2):
    date1=datetime.strptime(date1,"%d.%m.%Y")       ###  разница даты
    date2=datetime.strptime(date2,"%d.%m.%Y")
    return abs((date2-date1).days)

def

print(days_until_new_year())
