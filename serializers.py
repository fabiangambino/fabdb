# serializing database objects into a string
def serialize_contacts(database_contacts):

    s_contacts = ""
    for contact in database_contacts:
        s_contacts = s_contacts + contact.first_name + "," + contact.last_name + "," + contact.phone_number + "," + contact.email_address + "," + contact.contact_type + "," + contact.contact_owner.name + "\n"
    return s_contacts

# serializing user objects into a string
def serialize_users(user_list):

    s_users = ""
    for user in user_list:
        s_users = s_users + user.name + "," + "\n"
    return s_users
