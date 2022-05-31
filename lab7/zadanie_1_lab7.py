import os


def counter(q):
    file = open("rozprawa.txt", "r", encoding="utf-8")
    content = file.readlines()
    array = []
    words = []
    words_ = []
    string = 0
    for i in content:
        # print(i)
        array.append(i.strip())
    for x in array:
        if x != "":
            words.append(x.strip())
    for k in words:
        words_.append(k.split())
    for el in words_:
        for do in el:
            if len(q) > 1:
                do = do.lower()
                string += do.count(q)
            else:
                string += do.count(q)
    return string



def palindroms():
    file = open("rozprawa.txt", "r", encoding="utf-8")
    content = file.readlines()
    array = []
    words = []
    words_ = []
    pali = {}
    for i in content:
        # print(i)
        array.append(i.strip())
    for x in array:
        if x != "":
            words.append(x.strip())
    for k in words:
        words_.append(k.split())
    for el in words_:
        for u in el:
            u = u.lower()
            u_ = u[::-1]
            if len(u) > 1 and u == u_ and u.isdigit() == False and u[0] != "-":
                if u in pali:
                    continue
                else:
                    pali[u] = 0

    for key, item in pali.items():
        for k in words_:
            for y in k:
                if key == y:
                    pali[key] +=1
    return pali
    file.close()

def exist_file():
    while True:
        name_file = str(input("Podaj nazwę pliku: "))
        if os.path.isfile(name_file):
            break
        else:
            print("Nie znaleziono pliku!")
            continue



def main():
    exist_file()
    while True:
        query = str(input("Wpisz polecenie: "))
        if query == "palindromy":
            answ = palindroms()
            print(answ)
        elif query == "koniec":
            print("Przerywam działanie programu")
            break
        else:
            answer = counter(query)
            print(f"Znak {query} pojawia się w pliku 'rozprawa.txt' {answer}")


main()
