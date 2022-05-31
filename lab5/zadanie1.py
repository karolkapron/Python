def main():
    with open("data.txt", "r", encoding="utf-8") as file:
        content = file.readlines()
        arr = []
        encode_arr = []
        for el in content:
            arr.append(el.strip())
        # print(arr)
        for i in arr:
            x = int(i)
            encode_arr.append((chr(x)))
        # print(encode_arr)
        f = open("answer.txt", "w", encoding="utf-8")
        f.writelines(encode_arr)
        f.close()
main()