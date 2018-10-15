from abc import ABC, abstractmethod


class ADTString(ABC):
    """
    串 - 零个或多个字符组成的有限序列
    """

    def __init__(self, s):
        pass

    @abstractmethod
    def copy(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def compare(self, target):
        pass

    @abstractmethod
    def concat(self, target):
        pass

    @abstractmethod
    def sub_string(self, i1, i2):
        pass

    @abstractmethod
    def index(self, target, pos):
        pass

    @abstractmethod
    def replace(self, t, v):
        pass

    @abstractmethod
    def insert(self, pos, t):
        pass

    @abstractmethod
    def delete(self, pos, len):
        pass
