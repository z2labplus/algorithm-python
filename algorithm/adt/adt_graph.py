from abc import ABC, abstractmethod


class ADTTree(ABC):
    """
    图 - 顶点有穷非空集合和边的集合
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
    def locate_vex(self):
        pass

    @abstractmethod
    def get_vex(self, v):
        pass

    @abstractmethod
    def put_vex(self, v, value):
        pass

    def first_adj_vex(self, v):
        pass

    def next_adj_vex(self, v, w):
        pass

    @abstractmethod
    def insert_vex(self, v):
        pass

    @abstractmethod
    def delete_vex(self, v):
        pass

    @abstractmethod
    def insert_arc(self, v, w):
        pass

    @abstractmethod
    def delete_arc(self, v, w):
        pass

    @abstractmethod
    def dfs_traverse(self):
        pass

    @abstractmethod
    def hfs_traverse(self):
        pass
