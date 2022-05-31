def main():
    file = open("splot.txt", "r")
    content = file.readlines()
    arr = []
    letter_dict = {}
    counter = 0
    for line in content:
        arr.append(line.replace("\n", ""))
    for k in arr:
        for string in k:
            if string.isupper():
                letter_dict[string] = 0
                counter += 1
    print(counter, letter_dict)
    for el in arr:
        for line in el:
            if line.isupper():
                letter_dict[line] += 1
    for key, value in letter_dict.items():
        letter_dict[key] = round(value / counter, 2)
    print(counter, letter_dict)
    file.close()

main()
