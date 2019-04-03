# pretty print function
def pretty_print(some_string, should_add_newline = True):

    stringify = ""

    for char in some_string:
        stringify += "~"

    if should_add_newline == True:
        print("")

    print(stringify)
    print(some_string)
    print(stringify)
