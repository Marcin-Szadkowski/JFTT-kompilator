from abc import ABC, abstractmethod


class Condition(ABC):
    def __init__(self, left_val, op, right_val):
        self.left = left_val
        self.operator = op
        self.right = right_val

    @abstractmethod
    def compile(self, code, reg):
        """Kompilacja na kod wynikowy"""
        pass
