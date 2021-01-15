
class ArrayDeclarationError(Exception):
    def __init__(self, array):
        message = "Invalid range of {} Array at line {}\n".format(array.pid, array.line)
        super().__init__(message)


class MultipleDeclarationsError(Exception):
    def __init__(self, declaration):
        message = "It seems like {} is declared more than once at {} line"\
            .format(declaration.pid, declaration.line)
        super().__init__(message)


class NotDeclaredError(Exception):
    def __init__(self, pid):
        message = "Reaching {} variable without declaration"\
            .format(pid)
        super().__init__(message)  # TODO wypadaloby wypisac w jakiej linii


class NotInitializedError(Exception):
    def __init__(self, pid):
        message = "Reaching {} variable that wasn`t initialized"\
            .format(pid)
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
