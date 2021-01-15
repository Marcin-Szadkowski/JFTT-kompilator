from compiler.exceptions import ArrayDeclarationError


class Array:
    """pidentifier(num:num)"""
    def __init__(self, pid, left_range, right_range, is_local=False, line=0):
        self.line = line
        self.pid = pid
        if left_range > right_range:
            raise ArrayDeclarationError(self)
        self.left_range = left_range
        self.right_range = right_range
        # dla tab(10:100) mamy 91 elementow indeksowanych od 10 do 100
        self.arr_len = right_range - left_range + 1
        self.is_local = is_local
        self.memory_addr = None

    def __str__(self):
        return self.pid
