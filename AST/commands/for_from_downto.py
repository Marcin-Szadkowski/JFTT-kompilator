from compiler.asm import Asm
from compiler.memory import Memory
from compiler.reg_manager import RegManager
from .command import Command
from ..declarations.variable import Variable


class ForFromDownto(Command):
    """FOR pidentifier FROM value DOWNTO value DO commands ENDFOR"""
    def __init__(self, pidentifier, value1, value2, commands, line=0):
        self.pidentifier = pidentifier
        self.value1 = value1
        self.value2 = value2
        self.commands = commands
        self.line = line

    def compile(self, code):
        # TODO to mozna lepiej napisac jak odpowiednio wybrac rejestry
        # code.add_instr("(--command for--)")
        #  lokalnie deklarujemy pidetifier
        iterator = Variable(self.pidentifier, is_local=True)
        to_range = Variable("loop_counter{}".format(self.pidentifier), is_local=True)  # loop_counter bedzie w adresie po iterator
        #  alokujemy dla niego miejsce w pamieci
        Memory.allocate(iterator)
        Memory.allocate(to_range)
        Memory.initialize(to_range)
        # iter bedzie przecowywac value2 - value1
        reg_from = RegManager.get_free_register()
        reg_to = RegManager.get_free_register()
        self.value1.compile(code, reg_from)  # reg_from <- value1
        self.value2.compile(code, reg_to)  # reg_to <- value2
        Memory.initialize(iterator)

        reg_iter = RegManager.get_free_register()
        iterator.load_addr_to_reg(code, reg_iter)   # reg_iter <- addr(iter)
        code.add_instr(Asm.STORE(reg_from, reg_iter))     # na poczatku iterator <- range_from

        code.add_instr(Asm.INC(reg_iter))       # reg_iter++
        # za iteratorem w pamieci przechowujemy licznik wykonania petli
        # value1 - value2 + 1
        code.add_instr(Asm.SUB(reg_from, reg_to))  # reg_from <- value1 - value2
        code.add_instr(Asm.INC(reg_from))
        code.add_instr(Asm.STORE(reg_from, reg_iter))  # p[reg_iter++] <- reg_to
        # tylko najpierw musimy sprawdzic czy value1 >= value2
        # czyli liczmy value2 - value1
        code.add_instr(Asm.DEC(reg_iter))
        code.add_instr(Asm.LOAD(reg_from, reg_iter))    # reg_from <- value1
        code.add_instr(Asm.SUB(reg_to, reg_from))
        _jump_start = code.add_dummy()     # JZERO reg_to _for
        _jump_endloop = code.add_dummy()    # JUMP _endfor

        RegManager.free_register(reg_from)
        # zapisujemy liczbe iteracji
        # przed sprawdzeniem ile zostalo iteracji trzeba bedzie ladowac adres tej zmiennej
        # i patrzec czy juz zero czy nie
        # FOR sprawdza na poczatku

        _for = code.get_count()     # FOR
        to_range.load_addr_to_reg(code, reg_to)  # reg_to <- addr(iter)
        code.add_instr(Asm.LOAD(reg_iter, reg_to))  # reg_iter <- loop_counter
        _jump_endfor = code.add_dummy()  # JZERO reg_iter _endfor

        RegManager.free_register(reg_iter)  # trzeba zwolnic te rejestry zeby commands mogly na nich dzialac
        RegManager.free_register(reg_to)
        for cmd in self.commands:
            cmd.compile(code)

        to_range.load_addr_to_reg(code, reg_to)     # TODO mozna by tak przed forem podobierac rejestry zeby na poczatku np nie ladowac adresu
        code.add_instr(Asm.LOAD(reg_iter, reg_to))
        code.add_instr(Asm.DEC(reg_iter))   # loop_counter--
        code.add_instr(Asm.STORE(reg_iter, reg_to))  # p[reg_to] <- reg_iter
        code.add_instr(Asm.DEC(reg_to))
        code.add_instr(Asm.LOAD(reg_iter, reg_to))  # reg_iter <- iterator
        code.add_instr(Asm.DEC(reg_iter))   # iterator--
        code.add_instr(Asm.STORE(reg_iter, reg_to))  # p[reg_to] <- reg_iter

        code.add_instr(Asm.JUMP(_for-code.get_count()))     # JUMP _for

        _endfor = code.get_count()  # ENDFOR

        code.add_instr_at_index(Asm.JZERO(reg_iter, _endfor-_jump_endfor), index=_jump_endfor)
        code.add_instr_at_index(Asm.JZERO(reg_to, _for-_jump_start), index=_jump_start)
        code.add_instr_at_index(Asm.JUMP(_endfor-_jump_endloop), index=_jump_endloop)
        #  mozemy tez usunac i z obszaru pamieci
        Memory.free(iterator)   # to wlasciwie zwolnienie z obszaru nazw
        Memory.free(to_range)
