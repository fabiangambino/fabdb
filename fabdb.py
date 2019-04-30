from ui_utils import *
from sanitizers import *
from serializers import *
from file_io import *
from printers import *
from models import *

# add new contacts functionality
def add_new_contact(database, user_list):

    name_error = "ERROR: Invalid Input. No numbers, spaces, or special characters. Try again."
    phone_error = "ERROR: Invalid Input. Input format must be as follows: ###-###-#### Try again."
    email_error = "ERROR: Invalid Input. Input format must be as follows: email_name@domain"

    first_name = input_sanitized("\nEnter the contact's first name: ", sanitize_name_fields, name_error)
    last_name = input_sanitized("\nEnter the contact's last name: ", sanitize_name_fields, name_error)
    phone_number = input_sanitized("\nEnter the contact's phone number: ", sanitize_phone_number, phone_error)
    phone_number = "".join([x for x in phone_number if x != "-"])
    email_address = input_sanitized("\nEnter the contact's email address: ", sanitize_email, email_error)


    contact_type = menu_display(contact_type_menu, contact_type_heading)
    if contact_type == 1:
        contact_type = "Unassigned"
    elif contact_type == 2:
        contact_type = "Prospect"
    elif contact_type == 3:
        contact_type = "Customer"

    user_names = [user.name for user in user_list]
    contact_owner = menu_display(user_names, contact_owner_heading)
    contact_owner = user_list[contact_owner -1]

    new_contact = Contact(first_name, last_name, phone_number, email_address, contact_type, contact_owner)
    database.append(new_contact)

    contact_added_message = first_name + " " + last_name + " was added to contacts!"
    pretty_print(contact_added_message)

# add users functionality
def add_user(user_list):

    username_error = "ERROR: Please enter username in this format: 'firstname lastname'."

    choice = menu_display(user_management_menu, default_menu_heading)

    if choice == 1:
        name = input_sanitized("\nEnter the user's name: ", sanitize_username, username_error)
        new_user = User(name)
        user_list.append(new_user)
        pretty_print(name + " was added to the users!")
    elif choice == 2:
        pretty_print("This feature is not built yet.")

def convert_users_to_names(user_list):

    user_names = []
    for item in user_list:
        user_names.append(item.name)
    return user_names

def search_contacts(database):

    choice = menu_display(search_contacts_menu, search_menu_heading)

    if choice == 1:

        name = input("\nEnter the full name you are searching for: ")
        print("")
        ns = name.split(" ")
        cleaned = [x for x in ns if x != ""]
        first_name = cleaned[0].lower()
        last_name = cleaned[1].lower()

        count = 0
        for item in database:
            if item.first_name.lower().startswith(first_name) and item.last_name.lower().startswith(last_name):
                item.cprint()
                count += 1

        if count == 0:
            pretty_print("Contact does not exist in database.")
        else:
            pretty_print("Found %d contacts" % count)

    elif choice == 2:

        phone_number = input("\nEnter the phone number you are searching for: ")
        print("")

        for item in database:
            if item.phone_number.startswith(phone_number):
                item.cprint()

    elif choice == 3:
        email_address = input("\nEnter the email address: ")
    elif choice == 4:
        contact_type = input("\nEnter the contact type: ")
    elif choice == 5:
        contact_owner = input("\nEnter the contact owner: ")


# control flow of the program
def main():

    welcome_message = "Welcome to Fab Database!"
    unbuilt_feature = "This feature is not built yet."
    exit_database_message = "Thank you for using Fab Database! Program Closed."

    user_list = load_users()
    database = load_database()
    convert_users_to_names(user_list)
    pretty_print(welcome_message)

    while True:

        task = menu_display(main_menu, default_menu_heading)

        if task == 1:
            print("")
            for item in database:
                item.cprint()
        elif task == 2:
            print("")
            for item in user_list:
                item.uprint()
        elif task == 3:
            add_new_contact(database, user_list)
        elif task == 4:
            search_contacts(database)
        elif task == 5:
            add_user(user_list)
        elif task == 6:
            pretty_print(exit_database_message)
            print("")
            break

    save_users(user_list)
    save_database(database)

main()
