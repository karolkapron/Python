import json
import os

class Tele:
    def __init__(self):
        self.tele_book = "default"
        self.data = {}

    def __init__(self, tele_book, data):
        self.tele_book = tele_book
        self.data = data

    def add_record(self, name, telephone):
        if telephone.isdigit() == False:
            print("Podany numer jest niepoprawny, zawiera inne znaki niż cyfry")
        else:
            if name in self.data:
                print(f"Podane imie {name} zawiera się już w książce")
            else:
                self.data[name] = telephone

    def print_all(self):
        print(f"Tytuł ksiazki {self.tele_book}")
        for key in self.data.keys():
            print(f"Imie {key}, numer telefonu {self.data[key]}")

    def write_json(self, json_file_name):
        name_file = json_file_name+".json"
        file = open(name_file, "w")
        content = json.dumps(self.data, indent=4)
        file.writelines(content)
        file.close()

    def read_json(self, file_name):
        json_name = file_name+".json"
        if os.path.isfile(json_name):
            with open(json_name, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    self.add_record(key, value)
        else:
            print(f"Plik o podanej nazwie: {json_name} nie istnieje")

    def __add__(self, other):
        new_one = Tele("XD", {})
        for key, value in other.data.items():
            new_one.add_record(key, value)
        for key, value in self.data.items():
            new_one.add_record(key, value)
        return new_one


if __name__ == "__main__":
    ksiazka = Tele("nazwa", {"Jan": "543789121", "Franciszek": "654321789", "Mateusz": "876532098", "Adam": "535789146", "Natalia": "543789121"})
    ksiazka.add_record("Karol", "543987122")
    ksiazka.print_all()
    ksiazka.write_json("data")
    ksiazka.read_json("asd")
    ksiazka.print_all()

    adder = Tele("XD", {"Ula": "423423"})
    suma = adder + ksiazka
    suma.print_all()