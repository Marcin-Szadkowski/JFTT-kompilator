from .register import REG


class RegManager:
    # free_registers = [REG.A, REG.B, REG.C, REG.D, REG.E, REG.F]
    free_registers = [REG.F, REG.E, REG.D, REG.C, REG.B, REG.A]
    used_registers = dict()

    @staticmethod
    def get_free_register():
        """Funkcja zwraca wolny rejest TODO: i przydziela obiekt do tego rejestru"""
        try:
            reg = RegManager.free_registers.pop()
            return reg
            # {"pid": REG.A, ..}
            # RegManager.used_registers[str(var)] = reg
        except IndexError:
            raise Exception("There are no free registers!")

    @staticmethod
    def free_register(reg):
        """Funkcja zwalnia rejestr i dodaje do wolnych rejestrow"""
        # TODO: pod optymalizacje
        if reg in RegManager.free_registers:
            raise Exception("Trying to free not used register {}".format(reg))
        else:
            RegManager.free_registers += [reg]

    @staticmethod
    def get_reg_of(var):
        """Funkcja zwraca rejestr zajety przez zmienna/stala nazwana"""
        try:
            register = RegManager.used_registers[str(var)]
            return register
        except KeyError:
            raise Exception("Object {} not found in used registers\n"
                            .format(var))
