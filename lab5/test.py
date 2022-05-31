import os.path

def main():
    # file = open("example.txt", "r")
    with open("example.txt", "w", encoding="utf-8") as file:
        # c = file.read(5)
        # x = file.read(2)
        # line = file.readline()
        # next_line = file.readline()
        file.write("ąśćę")
    print(os.path.isfile("example.txt"))
    s = "     enenen     \n"
    string = "text, test"
    el = string.split(",")
    print(el)
    print(s)
    x = s.strip()
    print(x)
main()