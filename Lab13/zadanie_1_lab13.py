import requests
import sys



#staff.elka.pw.edu.pl/~jwagner/tablica

def api():
    if sys.argv[1] == "post":
        sender = sys.argv[2]
        content = sys.argv[3]
        cont = {"sender": sender,
                "message": content
                }
        x = requests.post("http://staff.elka.pw.edu.pl/~jwagner/tablica/new_message.php", json = cont)
        if x.status_code == 200:
            print("udało się")
        else:
            print("Nie udało się połączyc z bazą")
    elif sys.argv[1] == "get":
        x = requests.get("http://staff.elka.pw.edu.pl/~jwagner/tablica/read_messages.php")
        data = x.text
        print(data)


api()
