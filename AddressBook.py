# This Python file uses the following encoding: utf-8


class AddressBook:
    name = ''
    address = ''

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __dict__(self):
        return {"name": self.name, "address": self.address}

    def __export__(self):
        ready = self.address.replace('\n', ' ')
        return f"{self.name} = {ready}\n"
