def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        return "Invalid command. Usage: add name phone"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) < 2:
        return "Invalid command. Usage: change username phone"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return 'Contact updated.'
    else:
        return f'Contact {name} was not found.'


def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Usage: phone username."
    name = args[0]
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return f"Error: Contact {name} not found."


def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = "\n".join(
        [f"{name}: {phone}" for name, phone in contacts.items()])
    return result


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(show_all(contacts))
            case _:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
