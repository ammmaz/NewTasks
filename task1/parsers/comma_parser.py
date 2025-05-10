name = "comma"

class Parser:
    def parse(self, file_path):
        import csv
        with open(file_path, newline='') as csvfile:
            return list(csv.DictReader(csvfile, delimiter=','))
