import requests, json
import prettytable as pt

# session = requests.session()
# url = "http://127.0.0.1:8000/login/"
# data = {"username": "lxy", "password": "lxy"}
# r = session.post(url=url, json=data)
# data = json.loads(r.text)
# print(data.get("msg"))
#
# url = "http://127.0.0.1:8000/logout/"
# r = session.get(url=url)
# data = json.loads(r.text)
# print(data.get("msg"))

def register(username, email, password):
    global session
    url = "http://127.0.0.1:8000/register/"
    data = {"username": username, "email": email, "password": password}
    r = session.post(url=url, json=data)
    data = json.loads(r.text)
    print(data.get("msg"))

def login(username, password, url):
    global session
    # url = "http://127.0.0.1:8000/login/"
    try:
        data = {"username": username, "password": password}
        r = session.post(url=url, json=data)
        cookies = r.cookies.get_dict()
        data = json.loads(r.text)
        print(data.get("msg"))
    except Exception as e:
        print("Your input url is not correct!")

    # print(r)
    # print(r.text)
    # print(r.content)

def logout():
    global session
    url = "http://127.0.0.1:8000/logout/"
    r = session.get(url=url)
    data = json.loads(r.text)
    print(data.get("msg"))
    session = requests.session()

def list():
    global session
    url = "http://127.0.0.1:8000/module/"
    r = session.get(url=url)
    data = json.loads(r.text)
    tb = pt.PrettyTable()
    title_list = []
    for i in data[0]:
        title_list.append(i)
    tb.field_names = title_list
    for i in data:
        row = []
        for j in i:
            if j == "taught_by":
                taught_by = []
                for t in i[j]:
                    taught_by.append(dict(t)["teacher_name"])
                row.append(str(taught_by)[1:-1])
            else:
                row.append(i[j])
        tb.add_row(row)
    print(tb)

def view():
    global session
    url = "http://127.0.0.1:8000/view/"
    r = session.get(url=url)
    data = json.loads(r.text)
    # print(data)
    if data['code'] == 100:
        print(data.get('msg'))
    elif data['code'] == 200:
        for i in data:
            if i == 'code':
                pass
            else:
                print("The rating of " + i + " is " + str(data[i]))

def average(professor_id, module_code):
    global session
    url = "http://127.0.0.1:8000/average/"
    data = {"professor_id": professor_id, "module_code": module_code}
    r = session.post(url=url, json=data)
    data = json.loads(r.text)
    # print(data)
    if data['code'] == 200:
        for i in data:
            if i == 'code':
                pass
            elif i == 'module_name':
                pass
            else:
                print("The rating of " + i + " (" + professor_id + ")" + " in module " + data['module_name'] + " (" + module_code + ")" + " is " + str(data[i]))
    else:
        print(data.get('msg'))

def rate(professor_id, module_code, year, semester, rating):
    global session
    url = "http://127.0.0.1:8000/rate/"
    data = {"professor_id": professor_id, "module_code": module_code, "year": year, "semester": semester, "rating": rating}
    r = session.post(url=url, json=data)
    data = json.loads(r.text)
    print(data.get("msg"))

if __name__ == '__main__':
    session = requests.session()
    # login("lxy", "lxy", "http://127.0.0.1:8000/login/")
    # view()
    # average("VS1", "CD1")
    # rate("VS1", "CD1", "2017", "1", "4")
    while True:
        print("-------------------------------------------------")
        print("Please input your commands! (type 'quit' to exit)")
        user_input = input()
        try:
            command = user_input.split()[0]
        except Exception as e:
            print("Invalid format, please input correct command!")
            continue
        if command == "register":
            username = input("username:")
            email = input("email:")
            password = input("password:")
            register(username, email, password)
        elif command == "login":
            try:
                url = user_input.split()[1]
            except Exception as e:
                print("Invalid format, please input as 'login url'!")
                continue
            username = input("username:")
            password = input("password:")
            login(username, password, url)
        elif command == "logout":
            logout()
        elif command == "list":
            list()
        elif command == "view":
            view()
        elif command == "average":
            try:
                professor_id = user_input.split()[1]
                module_code = user_input.split()[2]
            except Exception as e:
                print("Invalid format, please input as 'average professor_id module_code'")
                continue
            average(professor_id, module_code)
        elif command == "rate":
            try:
                professor_id = user_input.split()[1]
                module_code = user_input.split()[2]
                year = user_input.split()[3]
                semester = user_input.split()[4]
                rating = user_input.split()[5]
            except Exception as e:
                print("Invalid format, please input as 'rate professor_id module_code year semester rating'")
                continue
            rate(professor_id, module_code, year, semester, rating)
        elif command == 'quit':
            break
        else:
            print("Please input correct command!")