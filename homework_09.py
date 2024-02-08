def main():
    global contacts
    contacts = {'Bartek': 123, 'Marcin': 12413, 'Damian': 12314293}

    def input_error(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except KeyError:
                print('Nie znaleziono podanego kontaktu, wprowadź kontakt poprawnie lub dodaj nowy')
                return
            except ValueError:
                print('Telefon musi składać się z samuch cyfr')
                return
            except IndexError:
                print('Nie istnieje kontakt o podanym indeksie')
                return
        return wrapper
        
    

    @input_error
    def add(arg):
        arg = arg.split(' ')
        print(arg)
        contacts.update({arg[1]: int(arg[2])})
        print(f'dodano {arg[1]}: {arg[2]}')
    
    @input_error
    def change(arg):
        arg.split(' ')
        contacts[str(arg[1])] = int(arg[2])
        print(f'zmieniono na {arg[1]}: {arg[2]}')

    @input_error
    def phone_by_key(arg):
        print(f'Numer do {arg.split(' ')[1]}: {contacts[arg.split(' ')[1]]})

    @input_error
    def show_all():
        print(contacts)

    endings = ['good bye!', 'close', 'exit', '.'] 
    def end():
        print('Good bye!')

    start = input('Write "hello" to start the bot: ')
    if start.lower() == 'hello':
        print('bot started')
        while True:
            command_raw = input('How can i help you?: ')
            command_lower = command_raw.lower()
            if command_lower.startswith('add'):
                add(command_raw)
                pass
            elif command_lower.startswith('zmień'):
                change(command_raw)
                pass
            elif command_lower.startswith('phone'):
                phone_by_key(command_raw)
                pass
            elif command_lower == 'show all':
                show_all()
                pass
            elif command_lower in endings:
                print('bot stopped')
                end()
                break
            else:
                print('Nie znam takiej komendy', command_raw)
                pass

if __name__ == '__main__':
    main()