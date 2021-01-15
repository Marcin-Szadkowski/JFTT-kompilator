from .code import Code
from .memory import Memory


class CodeGenerator:
    """
    Klasa odpowiedzialna za generacje kodu,
    czyli wlasciwie kompilacje programu
    """
    def __init__(self, program):
        """
        :param program: referencja do korzenia AST
        """
        self.program = program
        self.code = Code()

    def set_memory(self, declarations):
        """Metoda inicjalizuje pamiec, gdy wystepuja deklaracje"""
        Memory.allocate_all(declarations)

    def run_compilation(self):
        """Uruchomienie kompilacji"""
        if self.program.declarations:
            self.set_memory(self.program.declarations)
        for cmd in self.program.commands:
            cmd.compile(self.code)

    def get_code(self):
        """Metoda zwraca kod na maszyne wirtualna"""
        self.run_compilation()
        return '\n'.join(self.code.instructions) + "\nHALT"  # TODO make sth cleaner
