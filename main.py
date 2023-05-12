from collections import UserDict
from my_class import Field, Name, Phone, Record
class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        self.contacts[name.lower()] = phone_number

    def change_phone_number(self, name, phone_number):
        if name.lower() in self.contacts:
            self.contacts[name.lower()] = phone_number
        else:
            print("Contact not found!")

    def get_phone_number(self, name):
        if name.lower() in self.contacts:
            return self.contacts[name.lower()]
        else:
            print("Contact not found!")

    def show_all_contacts(self):
        if self.contacts:
            print("Contacts:")
            for name, phone_number in self.contacts.items():
                print(f"{name.capitalize()}: {phone_number}")
        else:
            print("Phone book is empty.")

    def exit(self):
        print("Good bye!")
        exit()

    def handle_command(self, command):
        command_parts = command.split()
        command_name = command_parts[0].lower()

        if command_name == "hallo":
            print("How can I help you?")

        elif command_name == "add":
            if len(command_parts) == 3:
                name = command_parts[1].lower()
                phone_number = command_parts[2]
                self.add_contact(name, phone_number)
                print(f"Contact '{name.capitalize()}' with phone number '{phone_number}' added.")
            else:
                print("Invalid command! Usage: add [name] [phone_number]")

        elif command_name == "change":
            if len(command_parts) == 3:
                name = command_parts[1].lower()
                phone_number = command_parts[2]
                self.change_phone_number(name, phone_number)
                print(f"Phone number for contact '{name.capitalize()}' changed to '{phone_number}'.")
            else:
                print("Invalid command! Usage: change [name] [phone_number]")

        elif command_name == "phone":
            if len(command_parts) == 2:
                name = command_parts[1].lower()
                phone_number = self.get_phone_number(name)
                if phone_number:
                    print(f"Phone number for contact '{name.capitalize()}': {phone_number}")
                else:
                    print("Contact not found!")
            elif len(command_parts) == 1 or (len(command_parts) == 2 and command_parts[1] == "all"):
                self.show_all_contacts()
            else:
                print("Invalid command! Usage: show [all]")

        elif command_name in ["good", "bye", "close", "exit"]:
            self.exit()

        else:
            print("Invalid command!")

    def run(self):
        print("Welcome to Phone Book Assistant!")
        print("Enter 'hallo' to start.")
        while True:
            command = input("Enter command: ")
            self.handle_command(command)
class AddressBook(UserDict):
    def __init__(self):
        self.records = []

    def iterator(self, page_size=5):
        keys = list(self.keys())
        for i in range(0, len(keys), page_size):
            yield [self[k] for k in keys[i:i + page_size]]

    def __iter__(self):
        return self.RecordIterator(self)

    def add_record(self, record):
        self.records.append(record)

    def delete_record(self, name):
        del self.data[name]

    def __len__(self):
        return len(self.records)

    def edit_record(self, name, new_record):
        return self.RecordIterator(self)
    def show_all_records(self):
        if self.data:
            print("Records:")
            for name, record in self.data.items():
                phones = [phone.value for phone in record.phones]
                print(f"{name.capitalize()}: {', '.join(phones)}")
        else:
            print("Address book is empty.")



if __name__ == "__main__":
    phone_book = PhoneBook()
    phone_book.run()
