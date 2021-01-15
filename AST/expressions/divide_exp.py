from compiler.asm import Asm
from compiler.reg_manager import RegManager
from .expression import Expression


class DivideExp(Expression):
    """value / value"""
    def compile(self, code, reg):
        # uwaga tutaj wszystkie rejestry beda zajete
        # dlatego poziomy wyzej musza zadbac, zeby je zwalniac
        reg_left = RegManager.get_free_register()
        self.left.compile(code, reg_left)
        reg_right = RegManager.get_free_register()
        self.right.compile(code, reg_right)

        reg_mul = RegManager.get_free_register()
        reg_temp = RegManager.get_free_register()
        reg_addr = RegManager.get_free_register()
        code.add_instr(Asm.RESET(reg))
        code.add_instr(Asm.RESET(reg_addr))

        _jump_zero = code.add_dummy()  # JZERO reg_right j # TODO to mozna chyba wyzej
        code.add_instr(Asm.RESET(reg_mul))
        code.add_instr(Asm.INC(reg_mul))  # reg_mul <- 1

        _while = code.get_count()

        code.add_instr(Asm.STORE(reg_left, reg_addr))  # p[0] <- reg_right
        code.add_instr(Asm.LOAD(reg_temp, reg_addr))     # reg_temp <- p[0]
        code.add_instr(Asm.SUB(reg_temp, reg_right))
        _jump_endwhile = code.add_dummy()  # JZERO reg_temp j
        code.add_instr(Asm.SHL(reg_right))
        code.add_instr(Asm.SHL(reg_mul))
        _jump_while = code.add_dummy()  # JUMP j
        _endwhile = code.get_count()

        _while_start = code.get_count()
        code.add_instr(Asm.STORE(reg_right, reg_addr))  # p[0] <- reg_right
        code.add_instr(Asm.LOAD(reg_temp, reg_addr))
        code.add_instr(Asm.SUB(reg_temp, reg_left))

        _jump_if = code.add_dummy()  # JZERO reg_temp
        _jump_else = code.add_dummy()  # JUMP j

        _then = code.get_count()
        code.add_instr(Asm.SUB(reg_left, reg_right))
        code.add_instr(Asm.ADD(reg, reg_mul))
        _then_end = code.get_count()

        code.add_instr(Asm.SHR(reg_right))
        code.add_instr(Asm.SHR(reg_mul))

        _jump_while_false = code.add_dummy()  # JZERO reg_mul
        _jump_while_start = code.add_dummy()  # JUMP j

        _end = code.get_count()
        code.add_instr_at_index(Asm.JZERO(reg_mul, _end-_jump_while_false), index=_jump_while_false)
        code.add_instr_at_index(Asm.JZERO(reg_temp, _then-_jump_if), index=_jump_if)
        code.add_instr_at_index(Asm.JUMP(_then_end-_jump_else), index=_jump_else)
        code.add_instr_at_index(Asm.JUMP(_while_start-_jump_while_start), index=_jump_while_start)
        code.add_instr_at_index(Asm.JUMP(_while-_jump_while), index=_jump_while)
        code.add_instr_at_index(Asm.JZERO(reg_temp, _endwhile-_jump_endwhile), index=_jump_endwhile)
        code.add_instr_at_index(Asm.JZERO(reg_right, _end-_jump_zero), index=_jump_zero)

        # Zwolnij wszystkie rejestry oprocz reg, bo tam jest wynik
        RegManager.free_register(reg_right)
        RegManager.free_register(reg_left)
        RegManager.free_register(reg_temp)
        RegManager.free_register(reg_mul)
        RegManager.free_register(reg_addr)
