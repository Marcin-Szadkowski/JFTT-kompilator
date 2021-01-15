from compiler.asm import Asm
from compiler.reg_manager import RegManager
from .command import Command


class WhileDo(Command):
    """WHILE condition DO commands ENDWHILE"""
    def __init__(self, condition, commands, line=0):
        self.condition = condition
        self.commands = commands
        self.line = line

    def compile(self, code):
        reg_cond = RegManager.get_free_register()
        _while = code.get_count()
        self.condition.compile(code, reg_cond)
        _jump_do = code.add_dummy()     # JZERO reg_cond _do
        _jump_endwhile = code.add_dummy()   # JUMP _endwhile
        RegManager.free_register(reg_cond)  # zwalniamy rejestr warunku
        _do = code.get_count()
        for cmd in self.commands:
            cmd.compile(code)
        code.add_instr(Asm.JUMP(_while-code.get_count()))  # JUMP _while
        _endwhile = code.get_count()

        code.add_instr_at_index(Asm.JZERO(reg_cond, _do-_jump_do), index=_jump_do)
        code.add_instr_at_index(Asm.JUMP(_endwhile-_jump_endwhile), index=_jump_endwhile)
