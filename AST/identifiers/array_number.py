from AST.declarations.array import Array
from compiler.memory import Memory
from compiler.reg_manager import RegManager
from compiler.asm import Asm
from compiler.exceptions import NotAnArrayError


class ArrayNumber:
    def __init__(self, pid, number, line):
        self.pid = pid
        self.number = number
        self.line = line

    def compile(self, code, reg):
        """Ladujemy do rejestru wartosc zmiennej tablica[index]"""
        array = Memory.get_var_by_pid(self.pid)
        if not isinstance(array, Array):
            raise NotAnArrayError(self)
        if not array.left_range <= self.number <= array.right_range:
            # TODO zmienic exception
            raise IndexError("Index out of range in {} array at line {}".format(self.pid, self.line))
        # TODO: sprawdzic czy tablica jest zadeklarowana

        start_adr = array.memory_addr
        mem_index = self.number - array.left_range + start_adr
        reg_mem = RegManager.get_free_register()  # pomocniczy rejestr na pamiec
        code.set_value_in_register(mem_index, reg_mem)  # reg_mem <- adres elementu tab[i]
        code.add_instr(Asm.LOAD(reg, reg_mem))  # reg <- p[reg_mem]
        RegManager.free_register(reg_mem)

    def load_addr_to_reg(self, code, reg):
        """
        Ladujemy do rejetru adres zmiennej
        To wlasciwie do uzytku tylko do operacji przypisania,
        ale osobna funkcja duzo ulatwia
        """
        array = Memory.get_var_by_pid(self.pid)
        if not isinstance(array, Array):
            raise NotAnArrayError(self)
        if not (array.left_range <= self.number <= array.right_range):
            raise IndexError("Index {} out of range in {} array at line {}".format(self.number, self.pid, self.line))
        # TODO: sprawdzic czy tablica jest zadeklarowana

        start_adr = array.memory_addr
        mem_index = self.number - array.left_range + start_adr
        code.set_value_in_register(mem_index, reg)  # reg <- adres elementu tab[i]

    def __str__(self):
        return self.pid
