import random
dlugosc = int(input("Podaj długość: "))

def bubble(length):
    print(length)
    array = []
    for i in range(0,length):
        array.append(random.randint(0,101))
    print(array)
    for i in range(0,length-1):
        for j in range(i+1,length):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    print(array)
    even = []
    odd =[]
    checked = 0
    for i in array:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
        checked +=1
    print(f"Parzyste {even}, nieparzyste {odd}, sprawdzonych {checked}")
bubble(dlugosc)