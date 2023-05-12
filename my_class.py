import datetime
import re
import self as self


class Field:
    def __init__(self, value=None):
        self.name = None
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def set_name(self, name):
        self.name = name

    def set_value(self, value):
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def validate(self, value):
        return True

    def __repr__(self):
        return f"{self.__class__.__name__}({self._value})"


class Name(Field):
    def __init__(self, name):
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)

    def validate(self, value):
        return isinstance(value, str) and len(value) == 10 and value.isdigit()


class Birthday(Field):
    def days_to_birthday(self):
        if not self.value:
            return None
        today = datetime.date.today()
        bday = self.value.replace(year=today.year)
        if bday < today:
            bday = bday.replace(year=today.year + 1)
        return (bday - today).days

    def validate(self, value):
        return isinstance(value, datetime.date)


class Record:
    def __init__(self, name, phone, birthday=None):
        self.name = name
        self.phone = phone
        self.birthday = birthday

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.birthday.value if self.birthday else None}"

    def days_to_birthday(self):
        if self.birthday:
            return self.birthday.days_to_birthday()

    @property
    def phone(self):
        return self._phone.value if self._phone else None

    @phone.setter
    def phone(self, value):
        if isinstance(value, str) and re.match(r'^\+?\d{9,15}$', value):
            self._phone = Phone(value)
        else:
            raise ValueError(f"Invalid phone number: {value}")

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, value):
        if value is None or isinstance(value, Birthday):
            self._birthday = value
        else:
            raise ValueError(f"Invalid birthday: {value}")

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, index):
        del self.phones[index]

    def edit_phone(self, index, new_phone):
        self.phones[index].value = new_phone

    def set_birthday(self, date):
        self.birthday = Birthday(date)


class RecordIterator:
    def __init__(self, address_book, records_per_page=10):
        self.address_book = address_book
        self.records_per_page = records_per_page
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.address_book):
            raise StopIteration

        start_index = self.current_index
        end_index = self.current_index + self.records_per_page
        self.current_index = end_index
        return self.address_book.records[start_index:end_index]


