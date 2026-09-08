books = [
    {"title": "Война и мир", "author": "Толстой", "year": 1869, "genre": "Роман", "pages": 1225},
    {"title": "Преступление и наказание", "author": "Достоевский", "year": 1866, "genre": "Роман", "pages": 671},
    {"title": "Мастер и Маргарита", "author": "Булгаков", "year": 1967, "genre": "Роман", "pages": 480},
    {"title": "Евгений Онегин", "author": "Пушкин", "year": 1833, "genre": "Роман в стихах", "pages": 320},
    {"title": "Мёртвые души", "author": "Гоголь", "year": 1842, "genre": "Поэма", "pages": 352},
    {"title": "Герой нашего времени", "author": "Лермонтов", "year": 1840, "genre": "Роман", "pages": 224},
    {"title": "Ревизор", "author": "Гоголь", "year": 1836, "genre": "Комедия", "pages": 112},
    {"title": "Тихий Дон", "author": "Шолохов", "year": 1940, "genre": "Роман", "pages": 1408},
    {"title": "Идиот", "author": "Достоевский", "year": 1869, "genre": "Роман", "pages": 672},
    {"title": "Дубровский", "author": "Пушкин", "year": 1841, "genre": "Роман", "pages": 240}
]

def books_by_author(author, books):
    result =[]
    for book in books:
        if book['author'] == author:
            result.append(book['title'])
    return result

def books_by_genre(genre, books):
    result = []
    for book in books:
        if book['genre'] == genre:
            result.append(book['title'])
    return result

def books_before_year(year, books):
    result = []
    for book in books:
        if book['year']<year:
            result.append(book['title'])
    return result

def total_pages(books):
    total = 0
    for book in books:
        total += book["pages"]
    return total

def average_pages(books):
    total = 0
    for book in books:
        total += book['pages']
    avg = total/len(books)
    return round(avg, 1)

def thickest_book(books):
    thickest = max(books, key=lambda x: x['pages'])
    print("Самая толстая книга:")
    return thickest['title']

def sort_by_year(books):
    sorted_year = sorted(books,key=lambda x:x['year'])
    return  sorted_year

def group_by_genre(books):
    target = {}
    for book in books:
        genre = book['genre']
        if genre not in target:
            target[genre]=[]
        target[genre].append(book['title'])
    return target

def authors_with_one_genre(books):
    author_genres = {}
    result = set()
    for book in books:
        author = book['author']
        if author not in author_genres:
            author_genres[author] = []
        author_genres[author].append(book['genre'])
    print(author_genres)
    for author in author_genres:
        if len(author_genres[author])==1:
            result.add(author)
    return result

def unique_authors(books):
    authors = set()
    for book in books:
        authors.add(book['author'])
    return authors


def unique_genres(books):
    genre = set()
    for book in books:
        genre.add(book['genre'])
    return genre


def authors_in_both_genres(genre1, genre2, books):
    genre_one = set()
    genre_two = set()
    for book in books:
        if genre1 == book['genre']:
            genre_one.add(book['author'])
            if genre2 == book['genre']:
                genre_two.add(book['author'])
        return genre_one & genre_two

def books_by_multiple_authors(books):
    result = set()
    for book in books:
        if ',' in book['author']:
            result.add(book['title'])
    return result

def common_books(author1, author2, books):
    author1_books = set()
    author2_book = set()
    for book in books:
        if author1 == book['author']:
            author1_books.add(book['title'])
        if author2 == book['author']:
            author2_book.add(book['title'])
    result = (author1_books & author2_book)
    return result







