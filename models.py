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
        print("")

# user class objects
class User:

    def __init__(self, name):

        self.name = name

    def uprint(self):

        print("User: " + self.name)
