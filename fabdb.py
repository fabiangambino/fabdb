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

# comma separated contacts added to database
def csv_contacts(database):
    csv_contacts = ""
    for contact in database:
        csv_contacts = csv_contacts + str(contact.name) + "," + str(contact.phone_number) + "," + str(contact.email_address) + "\n"
    return csv_contacts

#Program Runs

welcome()

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

csv_contacts(database)
