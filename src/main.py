from src.csv_parser import CSVParser
from src.json_parser import JsonParser


def create_user(user):
    """приводит данные о пользователе к требуемому формату"""

    d = dict({"name": "", "gender": "", "address": "", "age": int})
    d["name"] = user["name"]
    d["gender"] = user["gender"]
    d["address"] = user["address"]
    d["age"] = user["age"]
    return d


def create_users_list(file_path):
    jp = JsonParser()
    users = []

    for user in jp.get_from_file(file_path):
        users.append(create_user(user))

    return users


def create_book(book):
    """приводит данные о книге к требуемому формату"""

    d = dict({"title": "", "author": "", "pages": int, "genre": ""})
    d["title"] = book["Title"]
    d["author"] = book["Author"]
    d["pages"] = book["Pages"]
    d["genre"] = book["Genre"]
    return d


def create_books_list(file_path):
    cp = CSVParser()
    books = []

    for book in cp.get_from_file(file_path):
        books.append(create_book(book))

    return books


def hand_out_books(books, users):
    """распределяет книги среди юзеров максимально поровну"""

    res = []
    n = len(books)
    m = len(users)
    for i in range(m):
        res.append(dict(users[i]))
        res[i]["books"] = []
    for i in range(n):
        res[i % m]["books"].append(books[i])

    return res


def create_result_json(data, file_path):
    """создает джейсон файл с результатами"""

    jp = JsonParser()
    jp.load_to_file(data, file_path)


if __name__ == "__main__":
    res = hand_out_books(create_books_list("..\\data\\books.csv"), create_users_list("..\\data\\users.json"))
    create_result_json(res, "..\\data\\result.json")

