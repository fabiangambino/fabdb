from serializers import *
from models import *

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
                    contact_owner = User(cleaned_contact[5])
                    contact = Contact(first_name, last_name, phone_number, email_address, contact_type, contact_owner)
                    database.append(contact)

    except FileNotFoundError as e:
        pass

    return database

# save users to file
def save_users(user_list):

    with open("users.txt", "w") as users:
        users.write(serialize_users(user_list))

# load users from file
def load_users():

    user_list = []

    try:

        with open("users.txt", "r+") as users:
            file = users.read()

            for item in file.split("\n"):
                if item != "":
                    cleaned_user = item.split(",")
                    name = cleaned_user[0]
                    user = User(name)
                    user_list.append(user)

    except FileNotFoundError as e:
        pass

    return user_list
