import json
import os
FILE = os.path.join(os.path.dirname(__file__), "phonebook.json")
def save_phonebook():
    """Opens the .JSON file, to write the changes to it"""
    with open(FILE, "w") as f:
        json.dump(phonebook, f, indent=4)


def retrive_phonebook():
    """Opens the .JSON file to get the phonbook"""
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "11111111": ".JSON notfound",
            "22222222": ".JSON notfound",
            "33333333": ".JSON notfound",
        }

phonebook = retrive_phonebook()

def normalize_phone_number(test):
    """Remove whitespace so numbers can be entered with spaces."""
    return "".join(test.split())


def validate_phone_number(number):
    """Return True if the number contains exactly eight digits."""
    number = normalize_phone_number(number)
    return len(number) == 8 and number.isdigit()

def add_contact(number, name):
    """Add contact if not already in phonebook"""
    if not number or not name:
        print("Number and name can't be empty.")
    elif number in phonebook:
            print(f"{number} already belongs to {phonebook[number]}.")
            print(f"Do you want to edit {phonebook[number]}")
            choice = input("[Y] [N]")
            if choice == "Y":
                edit()
    else:
        phonebook[number] = name
        print(f"Added {name}.")
        save_phonebook()
    input("Press Enter to continue...")


def find_contact():
    """This is a way to find Contacts either based on phonenumber or name."""
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
    """Shows all contacts"""
    if not phonebook:
        print("The phonebook is empty.")
    for number, name in phonebook.items():
        print(f"{name} has '{number}' as phone number")
    input("Press Enter to continue...")

def edit(number, name):
    """Edits numbers aready in phonebook"""
    phonebook[number] = name
    print(f"Changed {name}.")
    save_phonebook()
