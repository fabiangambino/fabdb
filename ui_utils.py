from printers import *

# main menu options
main_menu = ["List all contacts", "List all users", "Add a new contact", "Search for a contact", "Manage users", "Exit"]
contact_type_menu = ["Unassigned", "Prospect", "Customer"]
user_management_menu = ["Add a new user", "Delete a user"]
search_contacts_menu = ["Search by name", "Search by phone number", "Search by email address", "Search by contact type", "Search by contact owner"]

# menu headings
contact_type_heading = "Contact Types:"
contact_owner_heading = "Contact Owners:"
search_menu_heading = "How would you like to search?"
default_menu_heading = "What would you like to do?"

# error messages
invalid_input_message = "Error! Please enter task numbers only."

def user_list_ui(user_list):

    print("")
    count = 0
    for user in user_list:
        count += 1
        print(str(count) + ". " + str(user.name))
    print("")


# generic menu display function
def menu_display(menu, heading):

    print("")
    print(heading)
    print("")
    count = 0
    for item in menu:
        count += 1
        print(str(count) + ". " + item)
    print("")

    while True:

        invalid_input_message = "Error! Please enter task numbers only."

        choice = input("Enter menu selection number and press enter: ")

        if choice.isdigit() is False:
            pretty_print(invalid_input_message)
            print("")
            continue
        elif int(choice) < 1 or int(choice) > count:
            pretty_print(invalid_input_message)
            print("")
            continue
        else:
            return int(choice)
