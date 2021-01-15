from compiler.asm import Asm
from compiler.reg_manager import RegManager
from .command import Command


class IfThen(Command):
    """IF condition THEN commands ENDIF"""
    def __init__(self, condition, commands, line=0):
        self.condition = condition
        self.commands = commands
        self.line = line

    def compile(self, code):
        reg_cond = RegManager.get_free_register()
        self.condition.compile(code, reg_cond)  # reg_cond <- 0 lub > 0
        _jump_then = code.add_dummy()  # JZERO reg_cond _then
        _jump_endif = code.add_dummy()  # JUMP _endif

        # warunek zostal sprawdzony i juz rejestr mozna zwolnic
        RegManager.free_register(reg_cond)
        _then = code.get_count()
        for cmd in self.commands:
            cmd.compile(code)
        _endif = code.get_count()

        code.add_instr_at_index(Asm.JZERO(reg_cond, _then-_jump_then), index=_jump_then)
        code.add_instr_at_index(Asm.JUMP(_endif-_jump_endif), index=_jump_endif)
