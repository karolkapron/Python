import os


def file_sizes(test):
    assert os.path.isdir(test)
    data = {}
    content = os.listdir(test)
    for el in content:
        test1 = os.path.join(test, el)
        if os.path.isdir(test1):
            next_data = file_sizes(test1)
            for key, value in next_data.items():
                if key in data:
                    data[key] += next_data[key]
                else:
                    data[key] = value
        else:
            whole_path = test+"/"+el
            extension = os.path.splitext(whole_path)
            size = os.path.getsize(whole_path)
            if extension[1] in data:
                data[extension[1]] += size
            else:
                data[extension[1]] = size
    return data



if __name__ == "__main__":
    try:
        print(file_sizes("boo1ks/"))
    except AssertionError:
        print("Błąd katalogu")

