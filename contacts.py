from classes import Contact
import csv_utils

def main():
    print_header()
    program_loop()

contact_list = []

def print_header():
    print('-' * 45 + '\n')
    print(' ' * 17 + 'CONTACTS DB' + '\n')
    print('-' * 45 + '\n')

def create_contact():
    contact = Contact.create_new_contact()
    contact_list.append(contact)

def search_contacts(contact_list):
    search_parameter = input(f'Would you like to search by [F]irst or [L]ast name: ')
    search_params = ['f', 'l']
    try:
        if search_parameter.lower() in search_params:
            # search by first letter of first name
            if search_parameter.lower() == 'f':
                search_letter = input(f'What is the first letter of the first name you are searching for: ')
                results = []
                for contact in contact_list:
                    if search_letter.lower() == contact.first_name[0].lower():
                        results.append(contact)
                if results:
                    for result in results:
                        print(result.full_name())
                else:
                    print(f'No results.')
            # TODO implement last name search
            # TODO implement full name search
            # TODO implement search by all parameters
        else:
            raise ValueError
    except:
        print('Input not recognized.')

    # Ask for search parameter - first name, last name, etc
    # Ask for exact match or first letter match
    # Ask for search term to match
    # Search contact list for search term
    # Return results to user and let the user pick which one to look at full contact info

def print_contacts(contact_list):
    contact_num = 1
    for contact in contact_list:
        print(f'Contact {contact_num}: {contact.first_name} {contact.last_name}')
        contact_num += 1


# method to import contacts from a csv
def import_contacts():
    # TODO prompt user if file is in place or if they need to download template
    contact_import = csv_utils.init()
    for contact in contact_import:
        print(f'Your contacts: {contact.first_name} {contact.last_name}')
        contact_import = Contact.import_new_contact(contact.first_name, contact.last_name)
        contact_list.append(contact_import)


# TODO write method to export a contacts template

#TODO write a method to export contacts list

def program_loop():
    valid_inputs = ['c', 'i', 'p', 'q', 's']
    while True:
        task = input(f'What would you like to do?\n'
                     f'\t[C]reate new contact\n'
                     f'\t[P]rint contacts\n'
                     f'\t[S]earch contacts\n'
                     f'\t[I]mport contacts\n'
                     f'\t[Q]uit\n'
                     f'\t> ')
        try:
            if task.lower() in valid_inputs:
                if task.lower() == 'c':
                    create_contact()
                elif task.lower() == 'i':
                    import_contacts()
                elif task.lower() == 'p':
                    print_contacts(contact_list)
                elif task.lower() == 's':
                    search_contacts(contact_list)
                elif task.lower() == 'q':
                    print('Good Bye')
                    break
            else:
                raise ValueError
        except:
            print('Please enter "C", "I", "P", "Q", or "S" to continue')
            continue

if __name__ == '__main__':
    main()

# TODO Database support
# TODO File i/o
# TODO Tests
# TODO Logging
# TODO Email/share contact
# TODO Look at pyinputplus for input validation
# TODO more things
