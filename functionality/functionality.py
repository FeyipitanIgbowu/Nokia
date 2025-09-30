class Nokia:
    def __init__(self):
        self.phonebook = []
        self.messages = []

    def get_phonebook(self):
        return self.phonebook

    def search_contacts(self):
        name = input("Enter name: ")
        for contact in self.phonebook:
            if contact["Name"] == name:
                return contact
        return None

    def search_contacts_with_number(self):
        number = input("Enter number: ")
        for contact in self.phonebook:
            if contact["Number"] == number:
                return contact
        return None

    def add_contact(self):
        name = input("Name: ")
        number = input("Number: ")
        contacts = {"Name": name, "Number": number}
        self.phonebook.append(contacts)
        return "Contact added"

    def delete_contact(self):
        choice = input("Delete by (name/number): ").strip().lower()

        if choice == "name":
            name = input("Enter name: ").strip().lower()
            for contact in self.phonebook:
                if contact["Name"].lower() == name:
                    self.phonebook.remove(contact)
                    return "Contact deleted"
        elif choice == "number":
            number = input("Enter number: ").strip()
            for contact in self.phonebook:
                if contact["Number"] == number:
                    self.phonebook.remove(contact)
                    return "Contact deleted"
        raise Exception("Contact not found")

    def edit_contact(self):
        contact = self.search_contacts_with_number()
        if contact:
            new_name = input("Enter new Name: ")
            new_number = input("Enter new Number: ")
            contact["Name"] = new_name
            contact["Number"] = new_number
            return "Contact edited"
        raise Exception("Contact not found")


    def get_messages(self):
        return self.messages

    def check_messages(self):
        if not self.messages:
            return "No messages found"
        return self.messages

    def send_messages(self):
        choice = input("Send by (name/number): ").strip().lower()

        if choice == "name":
            contact = self.search_contacts()
            if contact:
                message = input("Enter your message: ")
                prompt = {"To": contact["Name"], "Number": contact["Number"], "Message": message}
                self.messages.append(prompt)
                return "Message sent successfully"
            return "Contact not found"

        elif choice == "number":
            number = input("Enter recipient number: ")
            message = input("Enter your message: ")
            prompt = {"To": number, "Message": message}
            self.messages.append(prompt)
            return "Message sent successfully"

        return "Invalid option"

    def delete_message(self):
        number = input("Enter recipient name: ")
        for msg in self.messages:
            if msg["To"] == number:  # check recipient
                self.messages.remove(msg)
                return "Message deleted"
        return "Message not found"


