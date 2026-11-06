import json
import os
from functions import *



FILE = os.path.join(os.path.dirname(__file__), "phonebook.json")
phonebook = retrive_phonebook()



while True:
    print("\n1. Add contact")
    print("2. Find contact")
    print("3. Show all contacts")
    print("4. Edit Contacts")
    print("5. Explin Functions")
    print("6. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        number = input("Insert phone number: ")
        name = input("Insert name: ").strip()
        if validate_phone_number(number):
            add_contact(normalize_phone_number(number), name)
        else:
            print("Error: Expected a 8 digit number.")
            input("Press Enter to continue.")
            
    elif choice == "2":
        find_contact()

    elif choice == "3":
        show_all()

    elif choice == "4":
        number = input("Which phonenumber to change?")
        name = input("Insert new name: ").strip()
        if validate_phone_number(number):
            edit(normalize_phone_number(number), name)
            input("Press Enter to continue.")
        else:
            print("Error: Expected a 8 digit number.")
            input("Press Enter to continue.")

    elif choice == "5":
        functions_to_explain = [
            save_phonebook,
            retrive_phonebook,
            normalize_phone_number,
            validate_phone_number,
            add_contact,
            find_contact,
            show_all,
            edit,
        ]

        for function in functions_to_explain:
            print(f"\n{function.__name__}:")
            print(function.__doc__ or "No docstring available.")

    elif choice == "6":
        print("Goodbye")
        break

    else:
        print("Invalid option.")
