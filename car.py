command = ""
started = False

while True:
    command = str(input("> ")).lower()
    print(command)
    if command == 'help':
        print('''
        start: to start the car
        stop: to stop the car
        quit: to exit the program
        ''')
    elif command == 'start':
        print("car started... Ready to go!")
    elif command == 'stop':
        print("Car stopped.")
    elif command == 'quit':
        break;
    else:
        print("I don't understand that...")