from abc import ABC, abstractmethod


class ADTList(ABC):
    """
    线性表
    1. 除首元素,每个元素有一个直接前驱元素
    2. 除末元素,每个元素有一个直接后驱元素
    3. 一对一
    """

    def __init__(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def get_elem(self, i):
        pass

    @abstractmethod
    def locate_elem(self, elem):
        pass

    @abstractmethod
    def insert(self, i, elem):
        pass

    @abstractmethod
    def delete(self, i, elem):
        pass

    @abstractmethod
    def length(self):
        pass

    @abstractmethod
    def union(self, l):
        pass


class SequenceList(ADTList):
    """
    线性表 顺序存储结构
    """

    def __init__(self):
        super().__init__()

    def is_empty(self):
        pass

    def clear(self):
        pass

    def get_elem(self, i):
        pass

    def locate_elem(self, elem):
        pass

    def insert(self, i, elem):
        pass

    def delete(self, i, elem):
        pass

    def length(self):
        pass

    def union(self, l):
        pass


class LinkedList(ADTList):
    """
    线性表 链式存储结构
    """

    def is_empty(self):
        pass

    def clear(self):
        pass

    def get_elem(self, i):
        pass

    def locate_elem(self, elem):
        pass

    def insert(self, i, elem):
        pass

    def delete(self, i, elem):
        pass

    def length(self):
        pass

    def union(self, l):
        pass


class ADTStack(ABC):
    """
    栈 - 同线性表
    """

    def __init__(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    @property
    def top(self):
        pass

    @abstractmethod
    def push(self, e):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def length(self):
        pass


class ADTQueue(ABC):
    """
    队列 - 同线性表
    """

    def __init__(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    @property
    def head(self):
        pass

    @abstractmethod
    def enqueue(self, e):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def length(self):
        pass
