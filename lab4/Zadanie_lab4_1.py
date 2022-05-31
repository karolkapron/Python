def dicto():
    dict_men ={
        "Igor": 24,
        "Rafał": 21,
        "Karol": 35,
        "Adam": 32,
        "Marek": 18,
        "Piotr": 42
    }
    print(dict_men)
    dict_men["Tomek"] = 57
    print(dict_men)

    dict_kobieta = {
        "Anna": 56,
        "Katarzyna": 28,
        "Dorota": 17,
        "Marta": 16
    }
    dict_men.update(dict_kobieta)
    print(dict_men)
    print(len(dict_men))
    items_dict = dict_men.items()
    values_dict = dict_men.values()
    keys_dict = dict_men.keys()
    print(f"Zawartość {items_dict}, wartości {values_dict}, klucze {keys_dict}")
    dict_men["Piotr"] = 48
    print(dict_men)
    dict_men["Dorota"] = dict_men["Dorota"] - 2
    print(dict_men)
    dict_men.pop("Marta")
    print(dict_men)
    for key, values in dict_men.items():
        if values >=20 and values <=55:
            dict_men[key] = True
        else:
            dict_men[key] = False
        # print(key, values)
    print(dict_men)
dicto()