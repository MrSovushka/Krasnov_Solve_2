from models import Book
from storage import load, save


class Library:

    def __init__(self):
        self.books = load()
        # print("загружено книг:", len(self.books))

    def add(self, title, author, genre, year, desc):
        new_book = Book(title, author, genre, year, desc)
        self.books.append(new_book)
        save(self.books)
        return new_book

    def delete(self, book_id):
        for i in range(len(self.books)):
            if self.books[i].id == book_id:
                self.books.pop(i)
                save(self.books)
                return True
        return False

    def get_list(self, sort="title", genre=None, status=None):
        result = list(self.books)

        if genre:
            filtered = []
            for b in result:
                if b.genre.lower() == genre.lower():
                    filtered.append(b)
            result = filtered

        if status == "read":
            filtered = []
            for b in result:
                if b.read:
                    filtered.append(b)
            result = filtered
        elif status == "unread":
            filtered = []
            for b in result:
                if not b.read:
                    filtered.append(b)
            result = filtered

        if sort == "author":
            result.sort(key=lambda b: b.author)
        elif sort == "year":
            result.sort(key=lambda b: b.year)
        else:
            result.sort(key=lambda b: b.title)

        return result

    def search(self, query):
        q      = query.lower()
        result = []
        for b in self.books:
            in_title  = q in b.title.lower()
            in_author = q in b.author.lower()
            in_desc   = q in b.desc.lower()
            if in_title or in_author or in_desc:
                result.append(b)
        return result

    def get_favs(self):
        result = []
        for b in self.books:
            if b.fav:
                result.append(b)
        return result

    def find_by_id(self, book_id):
        for b in self.books:
            if b.id == book_id:
                return b
        return None

    def toggle_fav(self, book_id):
        b = self.find_by_id(book_id)
        if b is None:
            return None
        b.fav = not b.fav
        save(self.books)
        return b

    def set_read(self, book_id, val):
        b = self.find_by_id(book_id)
        if b is None:
            return None
        b.read = val
        save(self.books)
        return b
