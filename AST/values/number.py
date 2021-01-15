

class Number:
    def __init__(self, number):
        self.number = number

    def compile(self, code, reg):
        code.set_value_in_register(self.number, register=reg)
