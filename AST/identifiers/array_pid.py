from AST.declarations.array import Array
from compiler.asm import Asm
from compiler.memory import Memory
from compiler.reg_manager import RegManager


class ArrayPid:
    def __init__(self, pid, pid2):
        self.pid = pid
        self.pid2 = pid2

    def compile(self, code, reg):
        """Ladujemy do rejestru wartosc zmiennej tablica[index]"""
        array = Memory.get_var_by_pid(self.pid)
        var = Memory.get_var_by_pid(self.pid2)
        # TODO: sprawdzic czy tablica jest zadeklarowana
        start_adr = array.memory_addr
        # wartosc ladujemy do rejestru reg
        reg_temp = RegManager.get_free_register()
        # TODO: tu chyba trzeba by sprawdzic czy to nie kolejna tablica
        if not isinstance(array, Array):
            # TODO zmienic exception
            raise Exception("{} is a variables but it is accessed as Array type at {} line\n"
                            .format(self.pid, self.line))
        var.compile(code, reg_temp)  # reg_temp <- wartosc var
        code.set_value_in_register(array.left_range, reg)
        code.add_instr(Asm.SUB(reg_temp, reg))
        code.set_value_in_register(start_adr, reg)
        code.add_instr(Asm.ADD(reg_temp, reg))
        code.add_instr(Asm.LOAD(reg, reg_temp))  # reg <- p[reg_temp]
        # Zwolnienie rejestru
        RegManager.free_register(reg_temp)

    def load_addr_to_reg(self, code, reg):
        """
        Ladujemy do rejetru adres zmiennej
        To wlasciwie do uzytku tylko do operacji przypisania,
        ale osobna funkcja duzo ulatwia
        """
        """Ladujemy do rejestru wartosc zmiennej tablica[index]"""
        array = Memory.get_var_by_pid(self.pid)
        var = Memory.get_var_by_pid(self.pid2)
        # TODO: sprawdzic czy tablica jest zadeklarowana
        if not isinstance(array, Array):
            # TODO zmienic exception
            raise Exception("{} is a variables but it is accessed as Array type at {} line\n"
                            .format(self.pid, self.line))
        start_adr = array.memory_addr
        # wartosc ladujemy do rejestru reg
        reg_temp = RegManager.get_free_register()
        # TODO: tu chyba trzeba by sprawdzic czy to nie kolejna tablica
        var.compile(code, reg_temp)  # reg_temp <- wartosc var
        code.set_value_in_register(array.left_range, reg)
        code.add_instr(Asm.SUB(reg_temp, reg))
        code.set_value_in_register(start_adr, reg)
        code.add_instr(Asm.ADD(reg, reg_temp))  # reg <- reg + reg_temp = addr tab[i]
        # Zwolnienie rejestru
        RegManager.free_register(reg_temp)

    def __str__(self):
        return self.pid
