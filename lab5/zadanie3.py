import os.path

def main():
    database = {}
    if os.path.isfile("database.txt"):
        file = open("database.txt", "r", encoding="utf-8")
        content = file.readlines()
        for el in content:
            el_ = el.strip()
            logowanie = el_.split(" ")
            database[logowanie[0]] = logowanie[1]
        # print(database)
        while True:
            name = str(input("Podaj imię: "))
            if name in database.keys():
                passwd = str(input("Podaj haslo: "))
                if passwd == database[name]:
                    print("Udało Ci się zalogować")
                    break
                else:
                    print("Nie udalo ci się zalogowac")
                    break
            else:
                print("Podaj login jeszcze raz ")
    else:
        print("Plik nie istnieje ")
main()