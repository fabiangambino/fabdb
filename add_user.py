# add users functionality
def add_user(user_list):

    user_management_ui()

    ownership = int(input("\nEnter the task number and press enter: "))
    while user_control(ownership) is False:
        pretty_print("Error! Please enter task numbers only.")
        user_management_ui()
        ownership = input("\nEnter the task number and press enter: ")

    if ownership == 1:
        name = input("\nEnter the user's name: ")
        new_user = User(name)
        user_list.append(new_user)
        pretty_print(name + " was added to the users!")
    elif ownership == 2:
        pretty_print("This feature is not built yet.")
