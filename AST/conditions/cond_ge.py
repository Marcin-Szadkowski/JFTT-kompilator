from compiler.asm import Asm
from compiler.reg_manager import RegManager
from .condition import Condition


class CondGE(Condition):
    """value > value"""
    def compile(self, code, reg):
        """w reg zawsze 0 jesli warunek jest spelniony"""
        reg_left = RegManager.get_free_register()
        self.right.compile(code, reg)   # reg <- right_value
        self.left.compile(code, reg_left)  # reg_left <- left_value

        code.add_instr(Asm.INC(reg))  # left_value += 1
        # teraz jak odejmiemy right - left i bedzie 0 to wiemy, ze left > right
        code.add_instr(Asm.SUB(reg, reg_left))
        RegManager.free_register(reg_left)
