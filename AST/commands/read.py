from compiler.asm import Asm
from compiler.memory import Memory
from compiler.reg_manager import RegManager
from.command import Command


class Read(Command):
    """READ identifier;"""
    def __init__(self, identifier, line=0):
        self.identifier = identifier
        self.line = line

    def compile(self, code):
        reg_ident = RegManager.get_free_register()
        self.identifier.load_addr_to_reg(code, reg_ident)
        code.add_instr(Asm.GET(reg_ident))  # p[reg_ident] <- a
        Memory.initialize(self.identifier)
        RegManager.free_register(reg_ident)
