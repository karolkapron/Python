def pochodnie(array1, array2):
    assert len(array1) == len(array2)
    answ = []
    data = 0
    for x in range(0, len(array1)-1):
        y = (array2[x+1] - array2[x])/(array1[x+1] - array1[x])
        answ.append(y)
    print(answ)
    for el in answ:
        data += el**2

    return round(data**0.5, 2)

if __name__=="__main__":
    try:
        print(pochodnie([1, 2, 3, 4], [0.5, 1, 2, 3.5]))
    except AssertionError:
        print("Błąd dłguości tablicy")