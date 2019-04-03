def user_ui():

    print("\nWhat would you like to do?\n")
    print("1. List all contacts")
    print("2. List all users")
    print("3. Add a new contact")
    print("4. Search for a contact")
    print("5. Manage users")
    print("6. Exit\n")

# contact type ui for options
def contact_type_ui():

    print("\nContact Types:\n")
    print("1. Unassigned")
    print("2. Prospect")
    print("3. Customer\n")

# user management ui options
def user_management_ui():

    print("\nWhat would you like to do?\n")
    print("1. Add a new user")
    print("2. Delete a user")

def user_list_ui(user_list):

    print("")
    count = 0
    for user in user_list:
        count += 1
        print(str(count) + ". " + str(user.name))
    print("")
