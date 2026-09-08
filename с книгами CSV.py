import csv

book_prices = {}
results = []
total = 0
with open('books.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row['title']
        price = int(row['price'])
        book_prices[title] = price
    for title, price in book_prices.items():
        print(f"Цена на книгу: {title} - {price} руб.")
with open('sales.csv', 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        title = row['title']
        sold = int(row['sold'])
        if title in book_prices:
            revenue = book_prices[title] * sold
            total += revenue
            results.append({'title': title, 'sold': sold, 'revenue': revenue})
            print(f"Выручка по книге: {title}: {revenue} руб.")
        else:
            print(f"🚫  Предупреждение: книга '{title}' не найдена в прайсе")
    print(f"✅Общая выручка: {total} руб.")
with open('result.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'sold', 'revenue'])
    writer.writeheader()
    writer.writerows(results)
print("💾Файл result.csv создан.")

with open('books.csv', 'r', newline='', encoding='utf-8') as file:
    books = list(csv.DictReader(file))


def get_books_by_author(books, author):
    books_autor = []
    for row in books:
        title = row['title']
        authors = row['author']
        if authors == author:
            books_autor.append(title)
    return books_autor




def get_books_by_genre(books, genre):
    books_genre = []
    for row in books:
        genre_find = row['genre']
        title = row['title']
        if genre == genre_find:
            books_genre.append(title)
    return books_genre


def get_books_after_year(books, year_find):
    books_result = []
    for row in books:
        year =int(row['year'])
        title = row['title']
        if year > year_find:
            books_result.append(title)
    return books_result


def main():
    while True:
        print("1. Поиск по автору")
        print("2. Поиск после года")
        print("3. Поиск по жанру")
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            author = input("Введите автора: ")
            result = get_books_by_author(books, author)
            print(result)
        elif choice == '2':
            year_find = int(input("Введите год: "))
            result = get_books_after_year(books, year_find)
            if result:
                print(f"✅ Найденные книги после {year_find}: {result}")
            else:
                print("❌ Таких книг не найдено")
        elif choice == '3':
            genre = input("💡Введите жанр: ").title()
            result = get_books_by_genre(books, genre)
            if result:
                print(f"Книги в жанре {genre} - {result}")
            else:
                print(f"Книг в жанре '{genre}' не найдено.")
        else:
            print("Неверный пункт меню")

main()




