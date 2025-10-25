def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if args[0] not in contacts:
        return "Contact does not exist."

    contacts[args[0]] = args[1]
    return "Contact updated."


def show_phone(args, contacts):
    if args[0] not in contacts:
        return "Contact does not exist."

    return contacts[args[0]]


def show_all(contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print(
                """
                Invalid command. Available commands:
                hello
                add <name> <phone>
                change <name> <new_phone>
                phone <name>
                all
                close
                exit
                """.strip()
            )


if __name__ == "__main__":
    main()
