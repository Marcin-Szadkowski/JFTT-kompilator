from .asm import Asm


class Code:
    """
    Klasa beda reprezentacja kodu wynikowego
    """
    def __init__(self):
        self.instructions = list()
        self.instr_counter = 0
        # self.source_reg = None
        # self.dest_reg = None

    def add_instr(self, instruction):
        self.instructions += [instruction]
        self.instr_counter += 1

    def add_dummy(self):
        """Dodajemy pusta instrukcje, ktora tylko zapycha liste.
        Tu pozniej bedzie jakis jump ale jeszcze nie wiemy pod jaki indeks"""
        self.instructions += ["uups dummy here"]
        self.instr_counter += 1
        return self.instr_counter

    def add_instr_at_index(self, instruction, index):
        """Zastepujemy dummy instruction wlasciwa instrukcja"""
        try:
            self.instructions[index-1] = instruction
        except IndexError:
            raise Exception("There is no instruction at index: {}.\nYou tried to add {}"
                            .format(index-1, instruction))  # for debug

    def get_count(self):
        return self.instr_counter + 1

    def set_registers(self, regX=None, regY=None):
        """
        Ustawienie rejestrow, na ktorych aktualnie beda
        wykonywane operacje
         """
        if regX:
            self.source_reg = regX
        if regY:
            self.dest_reg = regY

    def set_value_in_register(self, value, register):
        """
        :param value: wartość
        :param register: rejestr, do ktorego wartosc zostanie zaladowana
        :return:
        """
        self.add_instr(Asm.RESET(register))

        binary = format(value, 'b')
        for i in range(len(binary)):
            if binary[i] == '1':
                self.add_instr(Asm.INC(register))
            if i < len(binary) - 1:
                self.add_instr(Asm.SHL(register))
