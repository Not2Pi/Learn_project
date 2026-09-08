users = [
    {"name": "Анна", "age": 25, "city": "Москва", "friends": ["Иван", "Петр", "Ольга"]},
    {"name": "Иван", "age": 30, "city": "Москва", "friends": ["Анна", "Сергей"]},
    {"name": "Петр", "age": 28, "city": "Киев", "friends": ["Анна", "Сергей", "Мария"]},
    {"name": "Сергей", "age": 35, "city": "Москва", "friends": ["Иван", "Петр"]},
    {"name": "Ольга", "age": 22, "city": "Киев", "friends": ["Анна", "Мария"]},
    {"name": "Мария", "age": 27, "city": "Киев", "friends": ["Петр", "Ольга"]}
]

def common_friends(name1, name2, users):
    friends1=set()
    friends2 =set()
    for user in users:
        if user["name"] == name1.title():
            friends1 = set(user["friends"])
        if user['name']==name2.title():
            friends2 = set(user["friends"])
    if not friends1:
        print(f"Пользователь {name1} не найден")
    if not friends2:
        print(f"Пользователь {name2} не найден")
    common = friends1 & friends2
    return common

def friends_of_friends(name, users):
    friends_name=set()
    result = set()
    target = None
    for user in users:
        if user["name"] == name.title():
            target = user
            friends_name=set(target["friends"])
    for new_name in friends_name:
        for user in users:
            if user['name'] == new_name:
                friends_of_friend = user["friends"]
                for friend in friends_of_friend:
                    result.add(friend)
    result.discard(name)
    for friend in friends_name:
        result.discard(friend)
    return result

def sort_by_age(users):
    sorted_users = sorted(users, key=lambda x:x['age'])
    return sorted_users

def sort_by_name_length(users):
    sorted_users_name = sorted(users,key=lambda x:len(x['name']))
    return sorted_users_name

def most_popular(users):
    popular_user = max(users,key=lambda x: len(x['friends']))
    return f"Самый популярный: {popular_user['name']} - друзей: {len(popular_user['friends'])}"

def sort_by_city(users):
    sorted_city = {}
    for user in users:
        city=user['city']
        if city not in sorted_city:
            sorted_city[city]=[]
        sorted_city[city].append(user["name"])
    return sorted_city


