
class ArrayDeclarationError(Exception):
    def __init__(self, array):
        message = "Błąd w linii {}: niewłaściwy zakres tablicy {} ".format(array.line, array.pid)
        super().__init__(message)


class MultipleDeclarationsError(Exception):
    def __init__(self, declaration):
        message = "Błąd w linii {}: druga deklaracja {} "\
            .format(declaration.line, declaration.pid)
        super().__init__(message)


class NotDeclaredError(Exception):
    def __init__(self, pid, line):
        message = "Błąd w linii {}: niezadeklarowana zmienna {} ".format(line, pid)
        super().__init__(message)  # TODO wypadaloby wypisac w jakiej linii


class NotInitializedError(Exception):
    def __init__(self, ident):
        message = "Błąd w linii {}: użycie niezainicjowanej zmiennej {} "\
            .format(ident.line, ident.pid)
        super().__init__(message)  # TODO wypadaloby wypisac w jakiej linii


class IsAnArrayError(Exception):
    def __init__(self, command):
        message = "Błąd w linii {}: niewłaściwe użycie zmiennej tablicowej {}"\
            .format(command.line, command.identifier.pid)
        super().__init__(message)


class NotAnArrayError(Exception):
    def __init__(self, var):
        message = "Błąd w linii {}: niewłaściwe użycie zmiennej {}"\
            .format(var.line, var.pid)
        super().__init__(message)


class ModifyingLocalVariable(Exception):
    def __init__(self, cmd):
        message = "Błąd w linii {}: próba modyfikacji zmiennej lokalnej {}"\
            .format(cmd.line, cmd.identifier.pid)
        super().__init__(message)


class ArrayIndexError(Exception):
    def __init__(self, array):
        message = "Index out of range in {} array at line {}"\
            .format(array.pid, array.line)
        super().__init__(message)
