import sys
from library import Library


lib = Library()
LINE = "-" * 45


def show_book(book, num):
    status = "прочитана" if book.read else "не прочитана"
    star   = "★" if book.fav else "☆"
    print(str(num) + ". " + star + "  " + book.title)
    print("   автор : " + book.author)
    print("   жанр  : " + book.genre + "  |  год: " + str(book.year))
    print("   статус: " + status + "  |  id: " + book.id)
    if book.desc:
        txt = book.desc if len(book.desc) <= 55 else book.desc[:55] + "..."
        print("   " + txt)
    print(LINE)


def show_list(books):
    if not books:
        print("пусто")
        return
    print(LINE)
    num = 1
    for b in books:
        show_book(b, num)
        num += 1


def pick(books):
    raw = input("номер книги: ").strip()
    if not raw.isdigit():
        print("нужно число")
        return None
    n = int(raw) - 1
    if n < 0 or n >= len(books):
        print("нет такой книги")
        return None
    return books[n].id


def cmd_add():
    print("\n-- добавить книгу --")
    title  = input("название  : ").strip()
    author = input("автор     : ").strip()
    genre  = input("жанр      : ").strip()
    year   = input("год       : ").strip()
    desc   = input("описание  : ").strip()

    if not year.isdigit():
        print("год должен быть числом!")
        return

    b = lib.add(title, author, genre, int(year), desc)
    print("добавлено: " + b.title + "  (id: " + b.id + ")")


def cmd_list():
    print("\n-- список книг --")

    print("сортировка?  1-название  2-автор  3-год")
    s = input("→ ").strip()
    if s == "2":
        sort = "author"
    elif s == "3":
        sort = "year"
    else:
        sort = "title"

    print("статус?  1-все  2-прочитанные  3-непрочитанные")
    f = input("→ ").strip()
    if f == "2":
        status = "read"
    elif f == "3":
        status = "unread"
    else:
        status = None

    genre = input("жанр (или enter): ").strip()
    if genre == "":
        genre = None

    books = lib.get_list(sort=sort, genre=genre, status=status)
    print("книг найдено: " + str(len(books)))
    show_list(books)


def cmd_search():
    print("\n-- поиск --")
    q     = input("запрос: ").strip()
    books = lib.search(q)
    print("найдено: " + str(len(books)))
    show_list(books)


def cmd_fav():
    print("\n-- избранное --")
    books = lib.get_list()
    show_list(books)
    uid = pick(books)
    if uid is None:
        return
    b = lib.toggle_fav(uid)
    if b.fav:
        print("добавлено в избранное ★")
    else:
        print("убрано из избранного")


def cmd_favlist():
    print("\n-- избранные книги --")
    show_list(lib.get_favs())


def cmd_status():
    print("\n-- изменить статус --")
    books = lib.get_list()
    show_list(books)
    uid = pick(books)
    if uid is None:
        return
    print("1-прочитана   2-не прочитана")
    ch  = input("→ ").strip()
    val = (ch == "1")
    b   = lib.set_read(uid, val)
    print(b.title + " → " + ("прочитана ✓" if val else "не прочитана"))


def cmd_delete():
    print("\n-- удалить --")
    books = lib.get_list()
    show_list(books)
    uid = pick(books)
    if uid is None:
        return
    sure = input("точно удалить? (y/n): ").strip()
    if sure == "y":
        lib.delete(uid)
        print("удалено.")
    else:
        print("отмена")


def menu():
    print("\n" + "=" * 45)
    print("          Т-Библиотека 📚")
    print("=" * 45)
    print("  1. добавить книгу")
    print("  2. все книги")
    print("  3. поиск")
    print("  4. избранное вкл/выкл")
    print("  5. список избранных")
    print("  6. отметить прочитанной")
    print("  7. удалить книгу")
    print("  0. выход")
    print(LINE)


def run():
    print("добро пожаловать!")
    while True:
        menu()
        ch = input("выбери: ").strip()

        if ch == "1":
            cmd_add()
        elif ch == "2":
            cmd_list()
        elif ch == "3":
            cmd_search()
        elif ch == "4":
            cmd_fav()
        elif ch == "5":
            cmd_favlist()
        elif ch == "6":
            cmd_status()
        elif ch == "7":
            cmd_delete()
        elif ch == "0":
            print("пока!")
            sys.exit(0)
        else:
            print("не понял, попробуй ещё раз")
