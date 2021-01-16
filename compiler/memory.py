from AST.declarations.array import Array
from compiler.exceptions import MultipleDeclarationsError
from compiler.exceptions import NotDeclaredError


class Memory:
    """
    :param current_address
    :param memory_space
    """
    # p[0] i p [1] rezerwujemy na swapy wartosci i instrukcje PUT
    current_address = 2
    initialized = set()
    memory_space = dict()
    
    # TODO refactor
    @staticmethod
    def allocate(declaration):
        """
        Metoda przydziela miejsce w pamiec dla deklaracji.
        Jest to abstrakcyjna realizacja pamieci maszyny wirtualnej
        """
        pid = declaration.pid

        allocate_space = 1
        Memory.memory_space[pid] = declaration
        declaration.memory_addr = Memory.current_address
        Memory.current_address += allocate_space

    @staticmethod
    def free(declaration):
        """Metoda usuwa deklaracje z przestrzeni nazw"""
        try:
            Memory.memory_space.pop(declaration.pid)
            Memory.initialized.remove(declaration.pid)
        except KeyError:
            raise Exception("Cannot free memory space for {} as it is not declared"
                            .format(declaration.pid))

    @staticmethod
    def allocate_all(declarations):
        Memory.check_duplicates(declarations)
        for decl in declarations:
            Memory.allocate(decl)

    @staticmethod
    def check_duplicates(declarations):
        """Metoda sprawdza czy nie zostaly powtorzone deklracje zmiennych"""
        seen = set()
        uniq = []
        invalid = []
        for decl in declarations:
            if decl.pid not in seen:
                uniq.append(decl)
                seen.add(decl.pid)
            else:
                invalid.append(decl)
        if len(invalid):
            for decl in invalid:
                raise MultipleDeclarationsError(decl)

    @staticmethod
    def get_var_by_pid(pid, line):
        if pid in Memory.memory_space:
            return Memory.memory_space[pid]
        else:
            raise NotDeclaredError(pid, line)

    @staticmethod
    def initialize(var):
        Memory.initialized.add(var.pid)

    @staticmethod
    def is_initialized(pid):
        return pid in Memory.initialized
