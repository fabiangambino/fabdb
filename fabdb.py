from ui_functions import user_ui, contact_type_ui, user_management_ui, user_list_ui
from sanitizers import sanitize_phone_number, sanitize_name_fields, sanitize_email, contact_type_control, ownership_control, user_control
from serializers import serialize_contacts, serialize_users
from file_io import save_database, save_users, load_database, load_users
from add_new_contacts import add_new_contact
from add_user import add_user
from pretty_print import pretty_print

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
