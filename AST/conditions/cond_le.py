from compiler.asm import Asm
from compiler.reg_manager import RegManager
from .condition import Condition


class CondLE(Condition):
    """value < value"""
    def compile(self, code, reg):
        """w reg zawsze 0 jesli warunek jest spelniony"""
        reg_right = RegManager.get_free_register()
        self.right.compile(code, reg_right)
        self.left.compile(code, reg)

        code.add_instr(Asm.INC(reg))
        code.add_instr(Asm.SUB(reg, reg_right))
        RegManager.free_register(reg_right)
