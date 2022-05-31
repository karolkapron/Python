def palindroms(array):
    palindrom = []
    for el in array:
        el = el.lower()
        el_ = el.replace(" ", "")
        reversed_el = el_[::-1].lower()
        #print(el_, " ", reversed_el)
        if reversed_el == el_:
            if reversed_el in palindrom:
                continue
            else:
                palindrom.append(reversed_el)
    sort_answ = sorted(palindrom)
    return sort_answ

print(palindroms(["kajak", "radar", "anakonda","radar", "jan", "kajak", "A to idiota"]))
