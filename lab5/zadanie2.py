def main():
    database = {}
    while True:
        name = str(input("Podaj imie: "))
        if name == "":
            break
        else:
            passwd = str(input("Podaj hasło: "))
            database[name] = passwd
    print(database)
    with open("database.txt", "w") as file:
        for key, item in database.items():
            key_ = str(key)
            item_ = str(item)
            line = key_+" "+item_+"\n"
            # print(line)
            file.write(line)

main()