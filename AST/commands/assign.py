from compiler.memory import Memory
from .command import Command
from ..declarations.array import Array
from ..identifiers.array_number import ArrayNumber
from ..identifiers.array_pid import ArrayPid
from compiler.asm import Asm
from compiler.reg_manager import RegManager
from compiler.exceptions import IsAnArrayError, ModifyingLocalVariable


class Assign(Command):
    """identifier := expression;"""

    def __init__(self, identifier, expression, line=0):
        self.identifier = identifier
        self.expression = expression
        self.line = line

    def compile(self, code):
        variable = Memory.get_var_by_pid(self.identifier.pid)

        if isinstance(variable, Array):
            if not isinstance(self.identifier, ArrayPid) and not isinstance(self.identifier, ArrayNumber):
                raise IsAnArrayError(self)

        if variable.is_local:
            raise ModifyingLocalVariable(self)
        # tu decyduje o przydzieleniu rejestrow
        reg_expr = RegManager.get_free_register()
        self.expression.compile(code, reg_expr)  # rA = value(expression)
        reg_ident = RegManager.get_free_register()
        # Przy przypisaniu do rejestru ladujemy adres zmiennej
        self.identifier.load_addr_to_reg(code, reg_ident)
        code.add_instr(Asm.STORE(reg_expr, reg_ident))  # p[rB] <- rA

        # zmienna zostala zainicjalizowana
        Memory.initialize(self.identifier)
        # Zwalniamy rejestry
        RegManager.free_register(reg_ident)
        RegManager.free_register(reg_expr)
