from compiler.asm import Asm
from compiler.reg_manager import RegManager
from .expression import Expression


class TimesExp(Expression):
    """value * value"""
    def compile(self, code, reg):
        reg_right = RegManager.get_free_register()
        reg_acc = RegManager.get_free_register()
        self.left.compile(code, reg_acc)  # reg_acc <- left_value
        self.right.compile(code, reg_right)  # reg_right <- right_value
        # chcemy zeby w reg_acc byla wieksza liczba
        code.add_instr(Asm.RESET(reg))
        code.add_instr(Asm.STORE(reg_right, reg))  # p[0] <- right_value
        code.add_instr(Asm.SUB(reg_right, reg_acc))  # reg_right <- right_value - left_value
        if_left_le_right = code.add_dummy()  # JZERO left_value > right_value ? jump : zamien
        # TODO te zamiane mozna by zrobic na funkcje jakas
        code.add_instr(Asm.INC(reg))  # reg <- 1
        code.add_instr(Asm.STORE(reg_acc, reg))  # p[1] <- left_value, czyli mniejsza
        code.add_instr(Asm.LOAD(reg_right, reg))
        code.add_instr(Asm.DEC(reg))    # reg <- 0
        code.add_instr(Asm.LOAD(reg_acc, reg))  # reg_acc <- right_value
        code.add_instr(Asm.STORE(reg_right, reg))  # p[0] <- lef_value, czyli mniejsza
        # koniec zamiany
        code.add_instr_at_index(Asm.JZERO(reg_right, code.get_count()-if_left_le_right), index=if_left_le_right)
        # jak nie wykonalismy zamiany to do reg_right trzeba przywrocic oryinalna wartosc
        code.add_instr(Asm.LOAD(reg_right, reg))

        _start = code.get_count()
        _jump_end = code.add_dummy()  # JZERO reg_acc
        _jump_add = code.add_dummy()  # JODD reg_acc
        _jump_sh = code.add_dummy()  # JUMP

        _add = code.get_count()
        code.add_instr(Asm.ADD(reg, reg_right))
        _sh = code.get_count()
        code.add_instr(Asm.SHR(reg_acc))  # reg_acc <- reg_acc / 2
        code.add_instr(Asm.SHL(reg_right))
        _jump_start = code.add_dummy()  # JUMP

        _end = code.get_count()
        code.add_instr_at_index(Asm.JZERO(reg_acc, _end-_jump_end), index=_jump_end)  # JZERO reg_acc _end
        code.add_instr_at_index(Asm.JODD(reg_acc, _add-_jump_add), index=_jump_add)   # JODD reg_acc _add
        code.add_instr_at_index(Asm.JUMP(_sh-_jump_sh), index=_jump_sh)    # JUMP _sh
        code.add_instr_at_index(Asm.JUMP(_start-_jump_start), index=_jump_start)    # JUMP _start

        # free registers
        RegManager.free_register(reg_acc)
        RegManager.free_register(reg_right)
