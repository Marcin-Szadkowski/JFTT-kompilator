from enum import Enum


# TODO refector
class REG(Enum):
    """Dostepne rejestry w maszynie wirtualnej"""
    A = 'a'
    B = 'b'
    C = 'c'
    D = 'd'
    E = 'e'
    F = 'f'

    def __str__(self):
        return self.value
