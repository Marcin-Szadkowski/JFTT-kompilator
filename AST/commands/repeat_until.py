from compiler.asm import Asm
from compiler.reg_manager import RegManager
from .command import Command


class RepeatUntil(Command):
    """REPEAT commands UNTIL condition;"""
    def __init__(self, commands, condition, line=0):
        self.commands = commands
        self.condition = condition
        self.line = line

    def compile(self, code):
        _repeat = code.get_count()
        for cmd in self.commands:
            cmd.compile(code)
        # teraz sprawdzamy warunek
        reg_cond = RegManager.get_free_register()
        self.condition.compile(code, reg_cond)
        code.add_instr(Asm.JZERO(reg_cond, _repeat-code.get_count()))  # JZERO reg_cond _repeat

        RegManager.get_free_register(reg_cond)
