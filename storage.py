import json
import os
from models import Book

FILE = "library.json"

def load():
    if not os.path.exists(FILE):
        return []

    f    = open(FILE, "r", encoding="utf-8")
    text = f.read()
    f.close()

    if not text.strip():
        return []

    # иногда падало с ошибкой если файл кривой, добавил try
    try:
        data = json.loads(text)
    except:
        print("файл с книгами повреждён, начинаем заново")
        return []

    result = []
    for item in data:
        result.append(Book.from_dict(item))
    return result


def save(books):
    data = []
    for b in books:
        data.append(b.to_dict())

    # пишем сначала во временный файл на всякий случай
    tmp = FILE + ".tmp"
    f   = open(tmp, "w", encoding="utf-8")
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.close()

    os.replace(tmp, FILE)
