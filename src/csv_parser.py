from csv import DictReader
from csv import DictWriter


class CSVParser:

    def get_from_file(self, file_path):
        with open(file_path, newline='') as f:
            reader = DictReader(f)
            data = [row for row in reader]
        return data

    def load_to_file(self, data, fieldnames, file_path):
        with open(file_path, "w", newline='') as f:
            writer = DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for d in data:
                writer.writerow(d)
