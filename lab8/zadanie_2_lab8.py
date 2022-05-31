def anagramy(x, y):
    array_string1 = list(x)
    array_string2 = list(y)
    array_string1_sort = sorted(array_string1)
    array_string2_sort = sorted(array_string2)
    if array_string1_sort == array_string2_sort:
        answ = True
    else:
        answ = False
    if answ == True:
        print(f"Słowa {x} i {y}, to anagramy ({answ}) ")
    else:
        print(f"Słowa {x} i {y}, to nie anagramy ({answ}) ")


def main():
    string1 = str(input("Podaj pierwszy ciag: "))
    string2 = str(input("Podaj drugi ciag: "))
    anagramy(string1, string2)


main()