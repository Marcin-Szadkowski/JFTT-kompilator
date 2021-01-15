from compiler.asm import Asm
from compiler.reg_manager import RegManager
from .condition import Condition


class CondGEQ(Condition):
    """value >= value"""
    def compile(self, code, reg):
        """w reg zawsze 0 jesli warunek jest spelniony"""
        reg_right = RegManager.get_free_register()
        self.right.compile(code, reg)  # reg <- right_value
        self.left.compile(code, reg_right)      # reg_right <- left_value

        code.add_instr(Asm.SUB(reg, reg_right))     # reg <- right_value - left_value
        RegManager.free_register(reg_right)
