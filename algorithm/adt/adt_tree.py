from abc import ABC, abstractmethod


class ADTTree(ABC):
    """
    树 - 一个根结点和若干颗子树自称.树中的结点具有相同数据类型以及层级关系
    """

    def __init__(self, s):
        pass

    @abstractmethod
    def copy(self):
        pass

    @abstractmethod
    def destroy(self):
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def clear(self, target):
        pass

    @abstractmethod
    def is_empty(self, target):
        pass

    def depth(self):
        pass

    def root(self):
        pass

    @abstractmethod
    def value(self, cur_e):
        pass

    @abstractmethod
    def assign(self, cur_e, value):
        pass

    @abstractmethod
    def parent(self, cur_e):
        pass

    @abstractmethod
    def left_child(self, cur_e):
        pass

    @abstractmethod
    def right_child(self, cur_e):
        pass

    @abstractmethod
    def insert_child(self,p,i,c):
        pass

    @abstractmethod
    def delete(self, p, i):
        pass
