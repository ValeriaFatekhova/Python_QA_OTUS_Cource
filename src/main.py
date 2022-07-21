from data.csv_parser import CSVParser
from data.json_parser import JsonParser


def create_user(user):
    d = dict({"name": "", "gender": "", "age": int, "books": []})
    d["name"] = user["name"]
    d["gender"] = user["gender"]
    d["age"] = user["age"]
    return d


def create_book(book):
    d = dict({"title": "", "author": "", "pages": int, "genre": ""})
    d["title"] = book["Title"]
    d["author"] = book["Author"]
    d["pages"] = book["Pages"]
    d["genre"] = book["Genre"]
    return d


# создание экземпляров парсеров
jp = JsonParser()
cp = CSVParser()

# создание списка пользователей в требуемом формате
users = []
for user in jp.get_from_file("..\\data\\users.json"):
    users.append(create_user(user))

# создание списка книг в требуемом формате
books = []
for book in cp.get_from_file("..\\data\\books.csv"):
    books.append(create_book(book))

print(users)
print(books)
