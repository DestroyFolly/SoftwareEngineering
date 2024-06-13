from __future__ import annotations

import logging

import requests


def menu() -> int:
    print("""
\nMenu:
0) Exit;
1) Users;
2) Trainers;
3) Trains;
4) Gym;
          """)
    action = input("Select an action: ")
    return int(action) if action.isdigit() else 0

def user_menu() -> int:
    print("""
\nMenu:
1) Log in;
2) Register;
3) Get the user by id;
4) Get the user by email;
5) Delete the user;
    """)
    action = input("Select an action: ")
    return int(action) if action.isdigit() else 0


def trainer_menu() -> int:
    print("""
\nMenu:
1) Add new trainer;
2) Delete trainer;
3) Get all trainers.
    """)
    action = input("Select an action: ")
    return int(action) if action.isdigit() else 0

def train_menu() -> int:
    print("""
\nMenu:
1) Add new train;
2) Delete train;
3) Get all trains.
    """)
    action = input("Select an action: ")
    return int(action) if action.isdigit() else 0

def gym_menu() -> int:
    print("""
\nMenu:
1) Add new gym;
2) Delete gym;
3) Get all gym.
    """)
    action = input("Select an action: ")
    return int(action) if action.isdigit() else 0




action = menu()
user_id = 0
role = ""
url = 'http://127.0.0.1:5000'

while action:
    logging.basicConfig(level=logging.DEBUG, filename=log_file, format = '%(levelname)s (%(asctime)s): %(message)s'
                                                                            '(Line: %(lineno)d) [%(filename)s]', datefmt='%d/%m/%Y %I:%M:%S',filemode="w")
    if action == 1:
        action = user_menu()
        if action == 1:
            data = {"email": input("Enter email: "), "password": input("Enter password: ")}
            response = requests.get(url + "/login", json=data)
            print(response.text)
        elif action == 2:
            data = {"phone": int(input("Enter your phone number: ")), "email": input("Enter email: "),
                    "name": input("Enter your name: "),
                    "surname": input("Enter your surname: "),
                    "password": input("Enter password: "), "gender": input("Enter your gender (M/F): ")}
            response = requests.post(url + "/register", json=data)
            user_id = response.json().get("user_id")
            role = response.json().get("role")
            print(f"Information: {response.json()}\nStatus code: {response.status_code}")
            print(f"Information: {response.json()}\nStatus code: {response.status_code}")
        elif action == 3:
            response = requests.get('http://127.0.0.1:5000/getuserbyid/1')
            print(response.text)
        elif action == 4 and role == "admin":
            response = requests.get(url + f"/getuserbyemail/{input('Enter the user email: ')}", timeout=10)
            print(f"Information: {response.json()}\nStatus code: {response.status_code}")
        elif action == 5 and role == "admin":
            response = requests.delete(url + f"/deleteuserbyid/{input('Enter the user ID: ')}")
        else:
            print("Not enough rights!")
    elif action == 2:
        action = trainer_menu()
        if action == 1 and role == "admin":
            data = {"name": input("Enter name: "),"surname": input("Enter surname: "),"gender": input("Enter gender (M/F): "),
                    "phone": int(input("Enter phone number: "))}
            response = requests.post(url + "/addtrainer", json=data)
            print(f"Information: {response.json()}\nStatus code: {response.status_code}")
        elif action == 2 and role == "admin":
            response = requests.delete(url + f"/deletetrainerbyid/{input('Enter ID: ')}")
            print(f"Information: {response.json()}\nStatus code: {response.status_code}")
        elif action == 3 and role == "admin":
            data = {"name": input("Enter name: "), "surname": input("Enter surname: "),
                    "gender": input("Enter gender (M/F): "),
                    "phone": int(input("Enter phone number: "))}
            response = requests.post(url + "/getlistoftrainers", json=data)
            print(f"Information: {response.json()}\nStatus code: {response.status_code}")
        else:
            print("Not enough rights!")
    elif action == 3:
        action = train_menu()
        if action == 1:
            data = {"title": input("Enter your name: "), "time": input("Enter time of the train: "),
                    "date": input("Enter train date: ")}
            response= requests.post(url+f"/create_payment/{user_id}", json=data)
            print(f"Information: {response.json()}\nStatus code: {response.status_code}")
        elif action == 2 and role == "admin":
            response = requests.delete(url + f"/delete_payment/{input('Enter the payment id: ')}")
            print(f"Information: {response.json()}\nStatus code: {response.status_code}")
        elif action == 3 and role == "admin":
            data = {"title": input("Enter your name: "), "time": input("Enter time of the train: "),
                    "date": input("Enter train date: ")}
            print(f"Information: {response.json()}\nStatus code: {response.status_code}")
        else:
            print("Not enough rights!")
    elif action == 4:
        action = gym_menu()
        if action == 1:
            data = {"adress": input("Enter gym`s address: "), "time": input("Enter gyms`s worktime: "),
                    "phone": int(input("Enter phone number: "))}
            print(f"Information: {response.json()}\nStatus code: {response.status_code}")
        elif action == 2 and role == "admin":
            response = requests.get(url + f"/get_gym_by_id/{input('Enter the order ID: ')}")
            print(f"Information: {response.json()}\nStatus code: {response.status_code}")
        elif action == 3:
            response = requests.get(url + "/get_all_gyms")
            print(f"Information: {response.json()}\nStatus code: {response.status_code}")
        else:
            print("Not enough rights!")
    else:
        print("Incorrect input!")
    action = menu()

