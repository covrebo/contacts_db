
class Contact:
    """
    A contact object
    Attributes:
        first_name(string)
        last_name(string)
        address1(string)
        address2(string)
        city(string)
        state(string)
        zip(int)
        phone(string)
        email(string)
    """
    def __init__(self, first_name, last_name,): # address1, address2, city, state, zip, phone1, email
        self.first_name = first_name
        self.last_name = last_name
        # self.address1 = address1
        # self.address2 = address2
        # self.city = city
        # self.state = state
        # self.zip = zip
        # self.phone1 = phone1
        # self.email = email

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def create_new_contact(self):
        while True:
            try:
                first_name = input('First name: ')
                if not first_name:
                    raise ValueError
                last_name = input('Last name: ')
                if not last_name:
                    raise ValueError
                return self(first_name, last_name)
            except:
                print('Invalid input. Try again.')
                # continue



