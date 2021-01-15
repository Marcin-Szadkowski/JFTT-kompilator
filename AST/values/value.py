from abc import ABC, abstractmethod


class Value(ABC):
    @abstractmethod
    def compile(self, code, reg):
        """Kompilacja na kod wynikowy"""
        pass
