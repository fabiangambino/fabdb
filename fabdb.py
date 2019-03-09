class Contact:

    def __init__(self, name, phone_number, email_address):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address

    def cprint(self):
        print("Name: " + self.name)
        print("Phone Number: " + str(self.phone_number))
        print("Email Address: " + self.email_address)

database = []

def welcome():
    print("\n------------------------")
    print("Welcome to Fab Database!")
    print("------------------------")

def user_ui():
    print("\nWhat would you like to do?\n")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Exit\n")

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

# options 2, 3, and 4 are not built out yet
while True:
    user_ui()
    task = int(input("Enter the task number and press enter: "))
    if task == 1:
        add_new_contact()
    elif task == 2:
        print("\n------------------------------")
        print("This feature is not built yet.")
        print("------------------------------")
    elif task == 3:
        print("\n------------------------------")
        print("This feature is not built yet.")
        print("------------------------------")
    elif task == 4:
        print("\n------------------------------")
        print("This feature is not built yet.")
        print("------------------------------")
    elif task == 5:
        print("\n-------------------")
        print("Exited Fab Database")
        print("-------------------\n")
        break

print(database)
