import os


def file_sizes(test):
    assert os.path.isdir(test), "Podany plik nie jest katalogiem"
    data = {}
    content = os.listdir(test)
    for el in content:
        whole_path =os.path.join(test, el)
        extension = os.path.splitext(whole_path)
        size = os.path.getsize(whole_path)
        if extension[1] in data:
            data[extension[1]] += size
        else:
            data[extension[1]] = size
    return data


if __name__ == "__main__":
    print(file_sizes("books/poe"))
