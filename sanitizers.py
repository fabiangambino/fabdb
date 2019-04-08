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

    if len(domain_split[0]) == 0 or len(domain_split[1]) == 0:
        return False

    return True

# input control for contact_owner field
def sanitize_contact_owner(choice, user_list):

    if choice < 1 or choice > len(user_list):
        return False
    else:
        return True

# input control for managing users
def sanitize_user(choice):

    if choice == 1:
        return True
    elif choice == 2:
        return True
    else:
        return False

# input control for usernames
def sanitize_username(username):

    username_split = username.split(" ")
    if len(username_split) == 2:
        if sanitize_name_fields(username_split[0]) is True and sanitize_name_fields(username_split[1]) is True:
            return True
    return False

# generic sanitizer
def input_sanitized(terminal_message, sanitizer):

    user_input = input(terminal_message)

    while sanitizer(input) is False:
        print(Error_msg)
        input = input(terminal_message)
    return input
