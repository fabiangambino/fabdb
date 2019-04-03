# main menu options
main_menu = ["List all contacts", "List all users", "Add a new contact", "Search for a contact", "Manage users", "Exit"]
contact_type_menu = ["Unassigned", "Prospect", "Customer"]
user_management_menu = ["Add a new user", "Delete a user"]

# menu headings
contact_type_heading = "Contact Types:"
default_menu_heading = "What would you like to do?"

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
