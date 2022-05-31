import os
import json

class SuperMarket(object):


    def __init__(self, name = None, data = None):
        self.name = name or "deafult"
        self.data = data or {}

    def add_data(self, path_to_file):
        if os.path.isfile(path_to_file):
            with open(path_to_file, "r") as file:
                self .data = json.load(file)
                print(self.data)
        else:
            print("Podana ścieżka jest błędna")

    def sale(self, name, discount):
        if name in self.data:
            if discount > 0 and discount < 1:
                self.data[name] -= self.data[name]*discount
                # print(self.data)
            else:
                print('Wysokość przeceny jest poza przedziałem')
        else:
            print("Podanego produktu nie ma w sklepie")


class ConvenienceStore(SuperMarket):

    def percent_sale(self, product, price):
        super().sale(product, price)
        print(f"Aktualna cena produktu {product} wynosi {self.data[product]} i został obnizony o {price*100}% ")


if __name__ == "__main__":
    sklep = SuperMarket()
    sklep.add_data('data.json')
    sklep.sale("piwo", 1/5)
    # print(sklep.data)
    sklep1 = ConvenienceStore()
    sklep1.add_data('data.json')
    sklep1.percent_sale("piwo", 1/2)
    x = isinstance(sklep1, SuperMarket)
    if x:
        print("Jest obiektem klasy")
    else:
        print("Nie jest obiektem klasy")