from compiler.asm import Asm
from compiler.memory import Memory
from compiler.reg_manager import RegManager
from compiler.exceptions import NotInitializedError


class Identifier:
    def __init__(self, pid, line):
        self.pid = pid
        self.line = line

    def compile(self, code, reg):
        """Ladujemy do rejestru wartosc zmiennej"""
        if not Memory.is_initialized(self.pid):
            raise NotInitializedError(self)
        address = Memory.get_var_by_pid(self.pid, self.line).memory_addr
        reg_mem = RegManager.get_free_register()
        code.set_value_in_register(address, register=reg_mem)
        code.add_instr(Asm.LOAD(reg, reg_mem))
        RegManager.free_register(reg_mem)

    def load_addr_to_reg(self, code, reg):
        """Ladujemy do rejetru adres zmiennej"""
        address = Memory.get_var_by_pid(self.pid, self.line).memory_addr
        code.set_value_in_register(address, register=reg)

    def __str__(self):
        return self.pid
