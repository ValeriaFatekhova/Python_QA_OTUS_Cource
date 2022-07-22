import json


class JsonParser:

    def get_from_file(self, file_path):
        with open(file_path, "r") as f:
            data = json.loads(f.read())
        return data

    def load_to_file(self, data, file_path):
        with open(file_path, "w") as f:
            f.write(json.dumps(data, indent=4))
