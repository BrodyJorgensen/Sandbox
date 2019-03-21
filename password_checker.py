def main():
    # statements...
    do_stuff()


def do_stuff():
    min_password_length = 3
    password = input("Password: ")
    while min_password_length >= 0:
        if len(password) >= min_password_length:
            print(len(password) * '*')
        password = input("Password: ")


# statements...

main()