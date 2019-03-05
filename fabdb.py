class Contact:

    def __init__(self, name, phone_number, email_address):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address

    def cprint(self):
        print("Name: " + self.name)
        print("Phone Number: " + str(self.phone_number))
        print("Email Address: " + self.email_address)

#robert = Contact("Robert Smith", 7185556666, "robert@pyproj.com")
#jason = Contact("Jason Brown", 7185557777, "jason@pyproj.com")
#michael = Contact("Michael Freedman", 7185558888, "michael@pyproj.com")
#eric = Contact("Eric Oswlad", 7185559999, "eric@pyproj.com")

def user_ui():
    print("\nWhat would you like to do?\n")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Exit\n")

contacts = []

#run
print("\n------------------------")
print("Welcome to Fab Database!")
print("------------------------")

while True:
    user_ui()
    task = int(input("Enter the task number: "))
    if task == 1:
        name = input("Enter the contact's name: ")
        phone_number = input("Enter the contact's phone number: ")
        email_address = input("Enter the contact's email address: ")
        print("\n" + name + " was added to contacts!")
