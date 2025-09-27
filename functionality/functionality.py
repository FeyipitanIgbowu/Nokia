from functionality.main import phonebook


class Nokia:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.phonebook = []
        self.messages = []

    def get_phonebook(self):
        return self.phonebook

    def add_contact(self):
        contacts = {"Name": self.name, "Number": self.number}
        self.phonebook.append(contacts)

    def delete_contact(self):
        contacts = {"Name": self.name, "Number": self.number}
        self.phonebook.remove(contacts)

