import requests

running = True

def menu(commands):
    labels = list(commands.keys())
    for i, label in enumerate(labels):
        print(f"{i}. {label}")
    choice = int(input(f"you command 0..{len(labels)-1}: "))
    commands[labels[choice]]()

def create():
    title = input('Todo title: ')
    payload = dict(title=title)
    resp = requests.post("http://localhost:5000/todos", json=payload)
    if resp.status_code == 201:
        print(f"todo created with id: {resp.json()['id']}")
    else:
        print(f"error create todo with response status code: {resp.status_code}")
        print(f"response body: {resp.text}")

def list_all():
    resp = requests.get("http://localhost:5000/todos")
    if resp.status_code == 200:
        todos = resp.json()['todos']
        for todo in todos:
            print(f"id: {todo['id']}, title: {todo['title']}, {'finish' if todo['finish'] else 'not finish'}")
    else:
        print(f"error get todo with response status code: {resp.status_code}")
        print(f"response body: {resp.text}")

def list_one():
    pass

def quit():
    global running
    running = False

while running:
    commands = {"create": create, "list all": list_all, "list_one": list_one, "quit": quit}
    menu(commands)
