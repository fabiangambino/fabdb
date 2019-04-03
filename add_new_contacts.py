# add new contacts functionality
def add_new_contact(database, user_list):

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
    contact_type = int(input("Enter the contact type number: "))
    while contact_type_control(contact_type) is False:
        pretty_print("ERROR: Please enter a valid contact type number. Try again.")
        contact_type_ui()
        contact_type = input("Enter the contact type number: ")

    if contact_type == 1:
        contact_type = "Unassigned"
    elif contact_type == 2:
        contact_type = "Prospect"
    elif contact_type == 3:
        contact_type = "Customer"

    user_list_ui(user_list)
    ownership = int(input("Enter the contact owner number: "))
    while ownership_control(ownership, user_list) is False:
        pretty_print("ERROR: Please enter a valid owner number. Try again.")
        user_list_ui(user_list)
        ownership = int(input("Enter the contact owner number: "))
    contact_owner = user_list[ownership - 1]

    new_contact = Contact(first_name, last_name, phone_number, email_address, contact_type, contact_owner)
    database.append(new_contact)

    contact_added_message = first_name + " " + last_name + " was added to contacts!"
    pretty_print(contact_added_message)
