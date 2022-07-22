from src.csv_parser import CSVParser
from src.json_parser import JsonParser


class Parser:

    def get_from_file(self, file_path):
        """выбирает нужный парсер в зависимости от расширения пришедшего файла и читает из файла"""
        p = None
        if file_path.split(".")[-1] == "json":
            p = JsonParser()
        elif file_path.split(".")[-1] == "csv":
            p = CSVParser()
        else:
            raise ValueError(f"Incorrect format of file. Function expects json or csv file")

        return p.get_from_file(file_path)

    def load_to_file(self, data, file_path):
        """выбирает нужный парсер в зависимости от расширения пришедшего файла и пишет данные в файл"""

        p = None
        if file_path.split(".")[-1] == "json":
            p = JsonParser()
        elif file_path.split(".")[-1] == "csv":
            p = CSVParser()
        else:
            raise ValueError(f"Incorrect format of file. Function expects json or csv file")

        p.load_to_file(data, file_path)
