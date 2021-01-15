from compiler.asm import Asm
from .expression import Expression
from ..values.number import Number
from compiler.reg_manager import RegManager


class MinusExp(Expression):
    """value - value"""
    def compile(self, code, reg):
        self.left.compile(code, reg)
        right_reg = RegManager.get_free_register()
        self.right.compile(code, right_reg)
        code.add_instr(Asm.SUB(reg, right_reg))  # rX <- expression
        RegManager.free_register(right_reg)
