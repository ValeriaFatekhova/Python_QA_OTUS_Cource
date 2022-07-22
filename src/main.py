from src.parser import Parser


def create_user(user):
    """приводит данные о пользователе к требуемому формату"""

    d = dict({"name": "", "gender": "", "address": "", "age": int})
    d["name"] = user["name"]
    d["gender"] = user["gender"]
    d["address"] = user["address"]
    d["age"] = user["age"]
    return d


def create_users_list(file_path):
    """создает список пользователей в нужном формате из джейсон файла"""

    p = Parser()
    users = (create_user(user) for user in p.get_from_file(file_path))

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
    """создает список книг в нужном формате из csv файла"""

    p = Parser()
    books = (create_book(book) for book in p.get_from_file(file_path))

    return books


def hand_out_books(books, users):
    """распределяет книги среди юзеров максимально поровну"""

    res = [dict(user) for user in users]
    m = len(res)
    i = 0
    for book in books:
        if "books" not in list(res[i % m].keys()):
            res[i % m]["books"] = []
        res[i % m]["books"].append(book)
        i += 1

    return res


def create_result_json(data, file_path):
    """создает джейсон файл с результатами"""

    p = Parser()
    p.load_to_file(data, file_path)


if __name__ == "__main__":
    res = hand_out_books(create_books_list("..\\data\\books.csv"), create_users_list("..\\data\\users.json"))
    create_result_json(res, "..\\data\\result.json")
