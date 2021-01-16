from AST.identifiers.identifier import Identifier


class Variable:
    """pidentifier"""
    def __init__(self, pid, is_local=False, line=0):
        self.pid = pid
        self.is_local = is_local
        self.memory_addr = None
        self.line = line

    def compile(self, code, reg):
        Identifier(self.pid, line=self.line).compile(code, reg)

    def load_addr_to_reg(self, code, reg):
        Identifier(self.pid, line=self.line).load_addr_to_reg(code, reg)

    def __str__(self):
        return self.pid
