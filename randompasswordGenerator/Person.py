class Person:

    def __init__(self, name, password):
        self._name = name
        self._password = password

    def get_name(self):
        return self._name

    def set_name(self, x):
        self._name = x

    def set_password(self, x):
        self._password = x

    def get_password(self):
        return self._password

