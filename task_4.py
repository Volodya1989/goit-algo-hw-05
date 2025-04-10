def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Give me valid contact."
        except IndexError:
            return "Not enough parameters. Please  try again."
        except TypeError:
            return "Unexpected input. Please try again."

    return inner


@input_error
def parse_input(user_input):
    if not user_input.strip():
        raise ValueError
    parts = user_input.split()
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return 'Contact updated.'
    else:
        return f'Contact {name} was not found.'


@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return f"Error: Contact {name} not found."


@input_error
def show_all(contacts):
    if not contacts:
        return "Your contact list is empty."
    result = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
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
