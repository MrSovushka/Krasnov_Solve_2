import uuid

class Book:
    def __init__(self, title, author, genre, year, desc):
        self.id     = uuid.uuid4().hex[:8]
        self.title  = title
        self.author = author
        self.genre  = genre
        self.year   = year
        self.desc   = desc
        self.read   = False
        self.fav    = False

    def to_dict(self):
        return {
            "id":     self.id,
            "title":  self.title,
            "author": self.author,
            "genre":  self.genre,
            "year":   self.year,
            "desc":   self.desc,
            "read":   self.read,
            "fav":    self.fav,
        }

    # TODO: потом сделать нормальную валидацию полей
    def from_dict(data):
        b        = Book(data["title"], data["author"], data["genre"], data["year"], data.get("desc", ""))
        b.id     = data["id"]
        b.read   = data.get("read", False)
        b.fav    = data.get("fav",  False)
        return b
