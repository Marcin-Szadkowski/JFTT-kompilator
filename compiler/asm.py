class Asm:
    """
    Class holds instructions of virtual machine
    """
    @staticmethod
    def GET(reg):
        return "GET {}".format(reg)

    @staticmethod
    def PUT(reg):
        return "PUT {}".format(reg)

    @staticmethod
    def LOAD(regX, regY):
        return "LOAD {} {}".format(regX, regY)

    @staticmethod
    def STORE(regX, regY):
        return "STORE {} {}".format(regX, regY)

    @staticmethod
    def ADD(regX, regY):
        return "ADD {} {}".format(regX, regY)

    @staticmethod
    def SUB(regX, regY):
        return "SUB {} {}".format(regX, regY)

    @staticmethod
    def RESET(regX):
        return "RESET {}".format(regX)

    @staticmethod
    def INC(regX):
        return "INC {}".format(regX)

    @staticmethod
    def DEC(regX):
        return "DEC {}".format(regX)

    @staticmethod
    def SHR(regX):
        return "SHR {}".format(regX)

    @staticmethod
    def SHL(regX):
        return "SHL {}".format(regX)

    @staticmethod
    def JUMP(j):
        return "JUMP {}".format(j)

    @staticmethod
    def JZERO(regX, j):
        return "JZERO {} {}".format(regX, j)

    @staticmethod
    def JODD(regX, j):
        return "JODD {} {}".format(regX, j)

    @staticmethod
    def HALT():
        return "HALT"
