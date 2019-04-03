from ui_functions import *
from sanitizers import *
from serializers import *
from file_io import *
from pretty_print import *

# contacts class objects layout
class Contact:

    def __init__(self, first_name, last_name, phone_number, email_address, contact_type, contact_owner):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.contact_type = contact_type
        self.contact_owner = contact_owner

    def cprint(self):

        print("Name: " + self.first_name + " " + self.last_name)
        print("Phone Number: " + str(self.phone_number))
        print("Email Address: " + self.email_address)
        print("Contact Type: " + self.contact_type)
        print("Ownership: " + self.contact_owner.name)

# user class objects
class User:

    def __init__(self, name):

        self.name = name

    def uprint(self):

        print("User: " + self.name)

# add new contacts functionality
def add_new_contact(database, user_list):

    first_name = input("\nEnter the contact's first name: ")
    while sanitize_name_fields(first_name) is False:
        invalid_input = "ERROR: Invalid Input. No numbers, spaces, or special characters. Try again."
        pretty_print(invalid_input)
        first_name = input("\nEnter the contact's first name: ")

    last_name = input("Enter the contact's last name: ")
    while sanitize_name_fields(last_name) is False:
        invalid_input = "ERROR: Invalid Input. No numbers, spaces, or special characters. Try again."
        pretty_print(invalid_input)
        last_name = input("\nEnter the contact's last name: ")

    phone_number = input("Enter the contact's phone number: ")
    while sanitize_phone_number(phone_number) is False:
        invalid_input = "ERROR: Invalid Input. Input format must be as follows: ###-###-#### Try again."
        pretty_print(invalid_input)
        phone_number = input("\nEnter the contact's phone number: ")

    email_address = input("Enter the contact's email address: ")
    while sanitize_email(email_address) is False:
        invalid_input = "ERROR: Invalid Input. Input format must be as follows: email_name@domain"
        pretty_print(invalid_input)
        email_address = input("\nEnter the contact's email address: ")

    contact_type_ui()
    contact_type = int(input("Enter the contact type number: "))
    while contact_type_control(contact_type) is False:
        pretty_print("ERROR: Please enter a valid contact type number. Try again.")
        contact_type_ui()
        contact_type = input("Enter the contact type number: ")

    if contact_type == 1:
        contact_type = "Unassigned"
    elif contact_type == 2:
        contact_type = "Prospect"
    elif contact_type == 3:
        contact_type = "Customer"

    user_list_ui(user_list)
    ownership = int(input("Enter the contact owner number: "))
    while ownership_control(ownership, user_list) is False:
        pretty_print("ERROR: Please enter a valid owner number. Try again.")
        user_list_ui(user_list)
        ownership = int(input("Enter the contact owner number: "))
    contact_owner = user_list[ownership - 1]

    new_contact = Contact(first_name, last_name, phone_number, email_address, contact_type, contact_owner)
    database.append(new_contact)

    contact_added_message = first_name + " " + last_name + " was added to contacts!"
    pretty_print(contact_added_message)

# add users functionality
def add_user(user_list):

    user_management_ui()

    ownership = int(input("\nEnter the task number and press enter: "))
    while user_control(ownership) is False:
        pretty_print("Error! Please enter task numbers only.")
        user_management_ui()
        ownership = input("\nEnter the task number and press enter: ")

    if ownership == 1:
        name = input("\nEnter the user's name: ")
        new_user = User(name)
        user_list.append(new_user)
        pretty_print(name + " was added to the users!")
    elif ownership == 2:
        pretty_print("This feature is not built yet.")

# control flow of the program
def main():

    welcome_message = "Welcome to Fab Database!"
    unbuilt_feature = "This feature is not built yet."
    exit_database_message = "Thank you for using Fab Database! Program Closed."
    invalid_input_message = "Error! Please enter task numbers only."

    user_list = load_users()
    database = load_database()
    pretty_print(welcome_message)

    while True:

        user_ui()
        task = int(input("Enter the task number and press enter: "))

        if task == 1:
            print("")
            for item in database:
                item.cprint()
                print("")
        elif task == 2:
            print("")
            for item in user_list:
                item.uprint()
        elif task == 3:
            add_new_contact(database, user_list)
        elif task == 4:
            pretty_print(unbuilt_feature)
        elif task == 5:
            add_user(user_list)
        elif task == 6:
            pretty_print(exit_database_message)
            print("")
            break
        else:
            pretty_print(invalid_input_message)

    save_users(user_list)
    save_database(database)

main()
