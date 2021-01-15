from compiler.asm import Asm
from compiler.reg_manager import RegManager
from .condition import Condition


class CondNEQ(Condition):
    """value != value"""
    def compile(self, code, reg):
        """reg <- (left - right) + (right - left)"""
        self.left.compile(code, reg)
        reg_right = RegManager.get_free_register()
        self.right.compile(code, reg_right)
        reg_help = RegManager.get_free_register()
        code.add_instr(Asm.RESET(reg_help))  # reg_help <- 0
        code.add_instr(Asm.STORE(reg, reg_help))  # p[0] <- reg
        code.add_instr(Asm.SUB(reg, reg_right))  # reg <- reg - reg_right
        code.add_instr(Asm.LOAD(reg_help, reg_help))  # reg_help <- p[0]
        code.add_instr(Asm.SUB(reg_right, reg_help))  # reg_right <- reg_right - reg_help
        code.add_instr(Asm.ADD(reg, reg_help))  # reg <- (left - right) + (right - left)
        # jak reg = 0 to , czyli musimy zamienic na np 1, a jak > 0 to zamienic na 0
        _jump_add = code.add_dummy()  # JZERO reg
        code.add_instr(Asm.RESET(reg))   # reg <- 0
        _jump_end = code.add_dummy()  # JUMP _end
        _add = code.get_count()
        code.add_instr(Asm.INC(reg))    # reg <- reg + 1
        _end = code.get_count()

        code.add_instr_at_index(Asm.JZERO(reg, _add-_jump_add), index=_jump_add)
        code.add_instr_at_index(Asm.JUMP(_end-_jump_end), index=_jump_end)

        RegManager.free_register(reg_help)
        RegManager.free_register(reg_right)
