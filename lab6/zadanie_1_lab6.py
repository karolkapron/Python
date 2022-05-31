def main():
    file = open("splot.txt", 'r', encoding="utf-8")
    content = file.readlines()
    arr = []
    answ = []
    counter = 0
    for i in content:
        i = i.lower()
        x = i.replace("\n", "")
        arr.append(x)
    # print(arr)
    file.close()
    for j in arr:
        counter += j.count("splot")
        answ.append(j.replace("splot", "konwolucja"))
    # print(answ)
    f = open("answer.txt", "w", encoding="utf-8")
    for k in answ:
        string = k + '\n'
        f.write(string)
    f.close()
    print(counter)


main()
