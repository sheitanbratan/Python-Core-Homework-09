"""Python core homework 9. Command Line Interface Bot assistant creating"""


user_data = {}


# Decorator:
def input_error(func):
    def wrapper(command):
        args = command.split(' ')
        if command.startswith('add') and len(args) < 3:
            print("Give me name and phone please")
        elif command.startswith('change') and len(args) < 3:
            print("Give me name and phone please")
        elif command.startswith('phone') and len(args) < 2:
            print("Enter user name")
        elif not (command.startswith('add')\
                  or command.startswith('change')\
                  or command.startswith('phone')\
                  or command == "hello"\
                  or command == "show all"):
            print('Unknown command ╮( ˘ ､ ˘ )╭')
        else:
            func(command)

    return wrapper


# Handler function wrapped by decorator:
@input_error
def command_handler(command):
    if command.startswith('add'):
        name, phone = str(command.split(' ')[1]).capitalize(), command.split(' ')[2]
        user_data[name] = phone
        print(f"{name}`s phone number was added successfully")
    elif command.startswith('change'):
        name, phone = str(command.split(' ')[1]).capitalize(), command.split(' ')[2]
        user_data[name] = phone
        print(f"{name}`s phone number has been successfully changed to {phone}")
    elif command.startswith('phone'):
        for name, phone in user_data.items():
            if str(command.split(' ')[1]).capitalize() == name:
                print(phone)
    elif command == "hello":
        print("How can I help you?")
    elif command == "show all":
        for name, phone in user_data.items():
            print('{:<10}{:>10}'.format(name, phone))


# Main function:
def main():
    # Greeting:
    print('Hi! I`m a bot assistant (´･ᴗ･ ` )')
    waiting = True
    while waiting:
        command = input(': ').lower()
        if command == "good bye" or command == "close" \
                or command == "exit":
            print("Good bye!")
            waiting = False

        else:
            command_handler(command)


if __name__ == '__main__':
    main()
