class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_cover(self):
        return "Обложка"

    def __str__(self):
        title = self.title
        author = self.author
        year = self.year
        return f"Название: {title}, Автор: {author}, {year} г."
class Novel(Book):
    def get_cover(self):
        return "Твёрдая обложка"

class Fantasy(Book):
    def get_cover(self):
        return "Мягкая обложка с драконом"

class Detective(Book):
    def get_cover(self):
        return "Мягкая обложка с лупой"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        return True

    def show_all(self):
        for book in self.books:
            print(book)

    def show_by_genre(self, genre):
        for book in self.books:
            if isinstance(book, genre):
                print(book)
    def show_covers(self):
        for book in self.books:
            title = book.title
            cover = book.get_cover()
            print(f"{title} - {cover}")


    def remove_book(self, title):
        for book  in self.books:
            if book.title == title:
                self.books.remove(book)
                return True

        return False

    def count_by_genre(self, genre):
        return sum(1 for book in self.books if isinstance(book, genre))

    def find_by_author(self, author):
        flags = False
        for book in self.books:
            if book.author == author:
                flags = True
                print(book)
        if not flags:
            print(f"Книг автора {author} не найдено")

    def save_to_file(self, filename):
        with open(filename, 'w',encoding='utf-8')as file:
            for book in self.books:
                    if isinstance(book, Novel):
                        genre = "Роман"
                    elif isinstance(book, Fantasy):
                        genre = "Фантастика"
                    elif isinstance(book, Detective):
                        genre = "Детектив"
                    else:
                        genre = "Неизвестный жанр"
                    file.write(f"{book.title}, {book.author}, {book.year}, {genre}\n")
            return True

library = Library()
book1 = Novel('Love', 'Pushkin', 1850)
book2 = Novel("Golubi", 'Stepanov',1980)
book3 = Fantasy("My Piace", 'Glushkov', 1985)
book4 = Detective("Find mi", "Holms", 1839)
library.add_book( book1)
library.add_book( book2)
library.add_book( book3)
library.add_book( book4)
print('-'*30)
library.save_to_file('test.txt')

