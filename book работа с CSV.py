books = [
    {"title": "Война и мир", "author": "Толстой", "year": 1869, "genre": "Роман", "pages": 1225,"price": 2345},
    {"title": "Преступление и наказание", "author": "Достоевский", "year": 1866, "genre": "Роман", "pages": 671,"price": 3455},
    {"title": "Мастер и Маргарита", "author": "Булгаков", "year": 1967, "genre": "Роман", "pages": 480,"price": 6445},
    {"title": "Евгений Онегин", "author": "Пушкин", "year": 1833, "genre": "Роман в стихах", "pages": 320,"price": 4345},
    {"title": "Мёртвые души", "author": "Гоголь", "year": 1842, "genre": "Поэма", "pages": 352,"price": 265},
    {"title": "Герой нашего времени", "author": "Лермонтов", "year": 1840, "genre": "Роман", "pages": 224,"price": 345},
    {"title": "Ревизор", "author": "Гоголь", "year": 1836, "genre": "Комедия", "pages": 112,"price": 2385},
    {"title": "Тихий Дон", "author": "Шолохов", "year": 1940, "genre": "Роман", "pages": 1408,"price": 2545},
    {"title": "Идиот", "author": "Достоевский", "year": 1869, "genre": "Роман", "pages": 672,"price": 7545},
    {"title": "Дубровский", "author": "Пушкин", "year": 1841, "genre": "Роман", "pages": 240,"price": 2395}
]
import csv
all_price = 0
book_big_price = []
max_price = 0
with open('books.csv', 'w',newline='',encoding='utf-8')as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'author', 'year', 'genre', 'pages', 'price'])
    writer.writeheader()
    writer.writerows(books)
with open('books.csv', 'r',newline='',encoding='utf-8')as file:
    reader=csv.DictReader(file)
    for row in reader:
        price = int(row['price'])
        all_price += price
        if price > max_price:
            max_price = price
            book_big_price = [row['title']]
        else:
            if max_price == price:
                book_big_price.append(row['title'])
    avg = all_price / len(books)


with open('books.csv','r',newline='',encoding='utf-8')as file:
    reader=csv.DictReader(file)
    max_avg_price = 0
    avg_price = 0
    target_book = {}
    best_genre = {}
    for row in reader:
        genre = row['genre']
        price = int(row['price'])
        target_book.setdefault(genre,[]).append(price)
    for key, values in target_book.items():
        avg_price = sum(values)/len(values)
        if avg_price > max_avg_price:
            max_avg_price = avg_price
            best_genre = {key: avg_price}
with open('books.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    total = 0
    author_count_book = {}
    avg_best_genre = {}
    avg_genre = {}
    result_avg_best_genre = {}
    result_avg_best = 0
    best_genre = {}
    best_author = {}
    avg = 0
    max_count_book = 0
    most_popular_author = []
    for row in reader:
        price = int(row['price'])
        title = row['title']
        author = row['author']
        genre = row['genre']
        best_genre.setdefault(genre, []).append(price)
        total += price
        if author not in author_count_book:
            author_count_book[author] = 1
        else:
            author_count_book[author] += 1
    for author, count in author_count_book.items():
        if count > max_count_book:
            max_count_book = count
            most_popular_author = [author]
        elif count == max_count_book:
            most_popular_author.append(author)
    for genre, count in best_genre.items():
        avg = int(round(sum(count) / len(count), 1))
        avg_best_genre[genre] = avg
        if avg > result_avg_best:
            result_avg_best = avg
            result_avg_best_genre = {genre: avg}

    sum_books = len(books)
    avg = total / len(books)
print(f"Общее количество книг: {sum_books}")
print(f"Средняя цена книги: {round(avg, 1)} руб.")
print(f"Самый популярный автор: {most_popular_author}")
print(f"Жанр с самой высокой средней ценой: {result_avg_best_genre}")




