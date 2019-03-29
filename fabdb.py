# contacts class object layout
class Contact:

    def __init__(self, first_name, last_name, phone_number, email_address, contact_type, ownership):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.contact_type = contact_type
        self.ownership = ownership

    def cprint(self):

        print("Name: " + self.first_name + " " + self.last_name)
        print("Phone Number: " + str(self.phone_number))
        print("Email Address: " + self.email_address)
        print("Contact Type: " + self.contact_type)
        print("Ownership: " + self.ownership)

#welcome_message = "Welcome to Fab Database!"

# welcome user interface
def welcome(welcome_message):

    pretty_print(welcome_message)

# user interface display
def user_ui():

    print("\nWhat would you like to do?\n")
    print("1. List all contacts")
    print("2. Add a new contact")
    print("3. Search for a contact")
    print("4. Exit\n")

# contact type ui for options
def contact_type_ui():

    print("\nContact Types:\n")
    print("1. Unassigned")
    print("2. Prospect")
    print("3. Customer\n")

# ownserhip ui for options
def ownership_ui():

    print("\nBrokers:\n")
    print("1. Unsassigned")
    print("2. Fabian Gambino")
    print("3. Matt Malleo")
    print("4. Jonathan Sosnay")
    print("5. Joel Bauman")
    print("6. River Allen\n")

# serializing database objects into a string
def serialize_contacts(database_contacts):

    s_contacts = ""
    for contact in database_contacts:
        s_contacts = s_contacts + contact.first_name + "," + contact.last_name + "," + contact.phone_number + "," + contact.email_address + "," + contact.contact_type + "," + contact.ownership + "\n"
    return s_contacts

# save function
def save_database(database):

    with open("database.txt", "w") as db:
        db.write(serialize_contacts(database))

# load contacts and reconstruct contact objects from text file
def load_database():

    database = []

    try:

        with open("database.txt", "r+") as db:
            file = db.read()

            for item in file.split("\n"):
                if item != "":
                    cleaned_contact = item.split(",")
                    first_name = cleaned_contact[0]
                    last_name = cleaned_contact[1]
                    phone_number = cleaned_contact[2]
                    email_address = cleaned_contact[3]
                    contact_type = cleaned_contact[4]
                    ownership = cleaned_contact[5]
                    contact = Contact(first_name, last_name, phone_number, email_address, contact_type, ownership)
                    database.append(contact)

    except:
        pass

    return database

# add new contacts functionality
def add_new_contact(database):

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
    contact_type = input("Enter the contact type number: ")
    while contact_type_control(contact_type) is False:
        pretty_print("ERROR: Please enter a valid contact type number. Try again.")
        contact_type_ui()
        contact_type = input("Enter the contact type number: ")

    if contact_type == "1":
        contact_type = "Unassigned"
    elif contact_type == "2":
        contact_type = "Prospect"
    elif contact_type == "3":
        contact_type = "Customer"

    ownership_ui()
    ownership = input("Enter the contact owner number: ")
    while ownership_control(ownership) is False:
        pretty_print("ERROR: Please enter a valid owner number. Try again.")
        ownership_ui()
        ownership = input("Enter the contact owner number: ")

    if ownership == "1":
        ownership = "Unsassigned"
    elif ownership == "2":
        ownership = "Fabian"
    elif ownership == "3":
        ownership = "Matt"
    elif ownership == "4":
        ownership = "Jonathan"
    elif ownership == "5":
        ownership = "Joel"
    elif ownership == "6":
        ownership = "River"

    new_contact = Contact(first_name, last_name, phone_number, email_address, contact_type, ownership)
    database.append(new_contact)

    contact_added_message = first_name + " " + last_name + " was added to contacts!"
    pretty_print(contact_added_message)

# pretty print function
def pretty_print(some_string, should_add_newline = True):

    stringify = ""

    for char in some_string:
        stringify += "~"

    if should_add_newline == True:
        print("")

    print(stringify)
    print(some_string)
    print(stringify)

# input control for phone number
def sanitize_phone_number(phone_number):

        if len(phone_number) != 12:
            return False

        if phone_number[3] != "-" or phone_number[7] != "-":
            return False

        for char in phone_number:
            if char != "-" and char.isdigit() is False:
                return False

        return True

# input control for first and last name fields
def sanitize_name_fields(name_field):

    if name_field == "":
        return False

    for char in name_field:
        if char == " " or char.isalpha() == False:
            return False

    return True

# input control for email_address field
def sanitize_email(email_address):

    if email_address.count("@") != 1:
        return False

    split_email = email_address.split("@")
    domain = split_email[1]
    domain_split = domain.split(".")

    if domain.count(".") != 1:
        return False

    for part in domain_split:
        if len(part) == 0:
            return False

    return True

# input control for contact type field
def contact_type_control(contact_type):

    if contact_type == "1":
        return True
    elif contact_type == "2":
        return True
    elif contact_type == "3":
        return True
    else:
        return False

# input control for ownership field
def ownership_control(ownership):

    if ownership == "1":
        return True
    elif ownership == "2":
        return True
    elif ownership == "3":
        return True
    elif ownership == "4":
        return True
    elif ownership == "5":
        return True
    elif ownership == "6":
        return True
    else:
        return False


# input control for email_address field


# control flow of the program

def main():

    welcome_message = "Welcome to Fab Database!"
    unbuilt_feature = "This feature is not built yet."
    exit_database_message = "Thank you for using Fab Database! Program Closed."
    invalid_input_message = "Error! Please enter task numbers only."

    database = load_database()
    welcome(welcome_message)

    while True:

        user_ui()
        task = input("Enter the task number and press enter: ")

        if task == "1":
            print("")
            for item in database:
                item.cprint()
                print("")
        elif task == "2":
            add_new_contact(database)
        elif task == "3":
            pretty_print(unbuilt_feature)
        elif task == "4":
            pretty_print(exit_database_message)
            print("")
            break
        else:
            pretty_print(invalid_input_message)

    save_database(database)

main()
