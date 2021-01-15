from .value import Value


class ValueIdentifier(Value):
    def __init__(self, identifier, line=0):
        self.identifier = identifier
        self.line = line

    def compile(self, code, reg):
        # ValueIdentifier zawsze kompilujemy prze compile(),
        # bo nie ma takiego wyprowadzenia zeby trzeba bylo ladowac do rejestru adres
        # TODO: tu mozna sprawdzic czy ma jakas wartosc, bo jak nie to error
        self.identifier.compile(code, reg)
