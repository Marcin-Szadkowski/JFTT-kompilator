from compiler.asm import Asm
from compiler.reg_manager import RegManager
from .condition import Condition


class CondEQ(Condition):
    """value = value"""
    def compile(self, code, reg):
        """reg <- (left - right) + (right - left)"""
        self.left.compile(code, reg)
        reg_right = RegManager.get_free_register()
        self.right.compile(code, reg_right)
        reg_help = RegManager.get_free_register()
        code.add_instr(Asm.RESET(reg_help))  # reg_help <- 0
        code.add_instr(Asm.STORE(reg, reg_help))  # p[0] <- left_value
        code.add_instr(Asm.SUB(reg, reg_right))  # reg <- left_value - right_value
        code.add_instr(Asm.LOAD(reg_help, reg_help))  # reg_help <- p[0], czyli left_value
        code.add_instr(Asm.SUB(reg_right, reg_help))  # reg_right <- right_value - left_value
        code.add_instr(Asm.ADD(reg, reg_right))  # reg <- (left - right) + (right - left)
        # jak reg = 0 to rowne
        RegManager.free_register(reg_help)
        RegManager.free_register(reg_right)
