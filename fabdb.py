# contacts class object layout
class Contact:

    def __init__(self, name, phone_number, email_address):

        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address

    def cprint(self):

        print("Name: " + self.name)
        print("Phone Number: " + str(self.phone_number))
        print("Email Address: " + self.email_address)

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

# serializing database objects into a string
def serialize_contacts(database_contacts):

    s_contacts = ""
    for contact in database_contacts:
        s_contacts = s_contacts + contact.name + "," + contact.phone_number + "," + contact.email_address + "\n"
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
                    name = cleaned_contact[0]
                    phone_number = cleaned_contact[1]
                    email_address = cleaned_contact[2]
                    contact = Contact(name, phone_number, email_address)
                    database.append(contact)

    except:
        pass

    return database

# add new contacts functionality
def add_new_contact(database):

    name = input("\nEnter the contact's name: ")
    phone_number = input("Enter the contact's phone number: ")
    email_address = input("Enter the contact's email address: ")

    new_contact = Contact(name, phone_number, email_address)
    database.append(new_contact)

    contact_added_message = name + " was added to contacts!"
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

# control flow of the program
def main():

    welcome_message = "Welcome to Fab Database!"
    unbuilt_feature = "This feature is not built yet."
    exit_database_message = "Thank you for using Fab Database! Program Closed."
    invalid_input_message = "Error! Please enter numbers only."

    database = load_database()
    welcome(welcome_message)

    while True:

        user_ui()
        task = input("Enter the task number and press enter: ")

        if task == "1":
            print("")
            for item in database:
                item.cprint()
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
