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

# database of contacts
database = []

# welcome user interface
def welcome():
    print("\n------------------------")
    print("Welcome to Fab Database!")
    print("------------------------")

# user interface display
def user_ui():
    print("\nWhat would you like to do?\n")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Exit\n")

# serializing database objects into a string
def serialize_contacts(database):
    s_contacts = ""
    for contact in database:
        s_contacts = s_contacts + contact.name + "," + contact.phone_number + "," + contact.email_address + "\n"
    return s_contacts

# save function
def save_database(database):
    with open("database.txt", "w") as db:
        db.write(serialize_contacts(database))

# working progress on deserializing contacts function
def deserialize_contacts():
    with open("database.txt", "r") as db:
        file = db.read()

        contacts = []
        clean_new_line_split = []
        fully_cleaned_contacts = []

        new_line_split = file.split("\n")
        for item in new_line_split:
            if item != "":
                clean_new_line_split.append(item)

        for item in clean_new_line_split:
            fully_cleaned_contacts.append(item.split(","))

        for item in fully_cleaned_contacts:
            name = fully_cleaned_contacts[0][0]
            phone_number = fully_cleaned_contacts[0][1]
            email_address = fully_cleaned_contacts[0][2]
            contact = Contact(name, phone_number, email_address)
            contacts.append(contact)

        for item in contacts:
            database.append(item)

    return database


# add new contacts functionality
def add_new_contact():
    name = input("\nEnter the contact's name: ")
    phone_number = input("\nEnter the contact's phone number: ")
    email_address = input("\nEnter the contact's email address: ")
    new_contact = Contact(name, phone_number, email_address)
    database.append(new_contact)
    print("\n-------------------------------------------------")
    print(name + " was added to contacts!")
    print("-------------------------------------------------")

#Program Runs

welcome()
deserialize_contacts()

# options 2, 3, and 4 are not built out yet
while True:
    user_ui()
    task = input("Enter the task number and press enter: ")
    if task == "1":
        add_new_contact()
    elif task == "2":
        print("\n------------------------------")
        print("This feature is not built yet.")
        print("------------------------------")
    elif task == "3":
        print("\n------------------------------")
        print("This feature is not built yet.")
        print("------------------------------")
    elif task == "4":
        print("\n------------------------------")
        print("This feature is not built yet.")
        print("------------------------------")
    elif task == "5":
        print("\n-------------------")
        print("Exited Fab Database")
        print("-------------------\n")
        break
    else:
        print("\n---------------------------------")
        print("Error! Please enter numbers only.")
        print("---------------------------------")

save_database(database)

# Contacts are getting loaded in but there in an error when saving over
# objects exist at runtime, but when adding new contacts, the older ones are
# overwritten with the 1st contact's data for some reason
