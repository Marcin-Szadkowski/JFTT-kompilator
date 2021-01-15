from compiler.asm import Asm
from compiler.memory import Memory
from compiler.reg_manager import RegManager
from.command import Command


class Write(Command):
    """WRITE value;
    value -> num | identifier"""
    def __init__(self, value, line=0):
        self.value = value
        self.line = line

    def compile(self, code):
        # PUT x, wyswietlenie zawartosci p[rX]
        reg = RegManager.get_free_register()  # TODO tu jakby sprawdzic czy to Number czy Indetifier to mozna zoptymalizowac
        self.value.compile(code, reg)  # reg <- value
        reg_help = RegManager.get_free_register()
        code.add_instr(Asm.RESET(reg_help))
        code.add_instr(Asm.STORE(reg, reg_help))  # p[0] <- value
        code.add_instr(Asm.PUT(reg_help))  # wyswietlenie p[0] czyli value
        try:
            pid = self.value.identifier.pid
            mem = Memory.get_var_by_pid(pid)
            print("Zmienna {} w linii {} i adresie {}"
                  .format(pid, self.line, mem.memory_addr))
        except AttributeError:
            pass
        RegManager.free_register(reg_help)
        RegManager.free_register(reg)
