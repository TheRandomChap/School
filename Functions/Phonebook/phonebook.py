import json
import os

FILE = os.path.join(os.path.dirname(__file__), "phonebook.json")


def save_phonebook():
    with open(FILE, "w") as f:
        json.dump(phonebook, f, indent=4)


def retrive_phonebook():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "93890028": "Mathias Andersen",
            "51220202": "Thomas Nielsen",
            "22434244": "Liselotte",
        }


phonebook = retrive_phonebook()


def add_contact():
    number = input("Insert phone number: ").strip()
    name = input("Insert name: ").strip()

    if not number or not name:
        print("Number and name can't be empty.")
    elif number in phonebook:
        print(f"{number} already belongs to {phonebook[number]}.")
    else:
        phonebook[number] = name
        print(f"Added {name}.")
        save_phonebook()
    input("Press Enter to continue...")


def find_contact():
    print("1. Name\n2. Phone number")
    choice = input("Choose an option: ")

    if choice == "1":
        search = input("Insert name: ").strip().lower()
        matches = [
            (number, name)
            for number, name in phonebook.items()
            if search in name.lower()
        ]
        if matches:
            for number, name in matches:
                print(f"{name}: {number}")
        else:
            print("Not found!")

    elif choice == "2":
        number = input("Insert phone number: ").strip()
        print(phonebook.get(number, "Not found!"))

    else:
        print("Invalid option.")

    input("Press Enter to continue...")


def show_all():
    if not phonebook:
        print("The phonebook is empty.")
    for number, name in phonebook.items():
        print(f"{name} has '{number}' as phone number")
    input("Press Enter to continue...")


while True:
    print("\n1. Add contact")
    print("2. Find contact")
    print("3. Show all contacts")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        find_contact()
    elif choice == "3":
        show_all()
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid option.")