from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def compile(self, code):
        """Kompilacja na kod wynikowy"""
        pass
