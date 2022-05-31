def main():
    file = open("splot.txt", "r")
    content = file.readlines()
    arr = []
    j = 1
    counter = 0
    one_zdanie = 0
    zero_zdan = 0
    for line in content:
        arr.append(line.replace("\n", ""))
    ile_zdan = len(arr)
    print(f"Tyle mamy zdań {ile_zdan}")
    for el in arr:
        for string in el:
            if string == "*":
                counter += 1
    for f in arr:
        print(f"Liczba gwiazdek w zdaniu {j}: {f.count('*')}")
        if f.count("*") >= 1:
            one_zdanie += 1
        else:
            zero_zdan += 1
        j += 1
    print(f"Tyle mamy gwiazdek {counter}")
    print(f"Minimum 1 gwiazdka {one_zdanie}")
    print(f"Zero gwiazdek {zero_zdan}")
    file.close()
    f = open("answer3.txt", "w", encoding="utf-8")
    for sentence in arr:
        xd = sentence.replace("*", "")
        sentence = xd + '\n'
        f.write(sentence)


main()
