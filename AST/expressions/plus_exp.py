from compiler.reg_manager import RegManager
from .expression import Expression
from compiler.asm import Asm


class PlusExp(Expression):
    """value + value"""
    def compile(self, code, reg):
        self.left.compile(code, reg)
        right_reg = RegManager.get_free_register()
        self.right.compile(code, right_reg)
        code.add_instr(Asm.ADD(reg, right_reg))  # rX <- expression
        RegManager.free_register(right_reg)
