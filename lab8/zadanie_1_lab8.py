import json
import math


def pole_kola(r):
    return math.pi * r ** 2


def obwod_kola(a):
    return 2 * math.pi * a


def pole_pr(a, b):
    return a * b


def obowd_pr(a, b):
    return 2 * a + 2 * b


def obowod_t(e, r, t):
    return e + r + t


def pole_t(a, b, c):
    p = (a + b + c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))


def main():
    with open("data.json", "r") as file:
        data = json.load(file)
        while True:
            query = str(input("Prosze podac co ma zostać obliczone (o - obowd, p -pole): "))
            if query == "o" or query == "p":
                break
        while True:
            figura = str(input(f"Prosze podac dla jakiej figury ma zostac policzony {'obwod' if query == 'o' else 'pole'} (t - trojkat, pr -prostakat, k - kolo): "))
            if figura == "pr" or figura == "t" or figura == "k":
                break
        if query == "o" and figura == "k":
            x = data["promien_kola"]
            print(f"Odczytane długości {x}")
            print(f"Obliczony obwod wynosi {obwod_kola(x)}")
        if query == "p" and figura == "k":
            x = data["promien_kola"]
            print (f"Odczytane długości {x}")
            print(f"Obliczone pole wynosi {pole_kola(x)}")
        if query == "o" and figura == "t":
            x1 = data["1bok_trojkata"]
            x2 = data["2bok_trojkata"]
            x3 = data["3bok_trojkata"]
            print(f"Odczytane długości {x1, x2, x3}")
            print(f"Obliczony obwod wynosi {obowod_t(x1, x2, x3)}")
        if query == "p" and figura == "t":
            x1 = data["1bok_trojkata"]
            x2 = data["2bok_trojkata"]
            x3 = data["3bok_trojkata"]
            print(f"Odczytane długości {x1, x2, x3}")
            print(f"Obliczone pole wynosi {pole_t(x1, x2, x3)}")
        if query == "o" and figura == "pr":
            x1 = data["1bok_prostokata"]
            x2 = data["1bok_prostokata"]
            print(f"Odczytane długości {x1, x2}")
            print(f"Obliczone pole wynosi {obowd_pr(x1, x2)}")
        if query == "p" and figura == "pr":
            x1 = data["1bok_prostokata"]
            x2 = data["2bok_prostokata"]
            print(f"Odczytane długości {x1, x2}")
            print(f"Obliczone pole wynosi {pole_pr(x1, x2)}")


main()
