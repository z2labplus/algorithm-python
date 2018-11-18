from btree import Tree


class BinarySearchTree(object):
    def __init__(self, base):
        self.base = base

    def find(self, data):
        '''
        查找
        '''
        p = self.base
        while p and p.data != data:
            p = p.ltree if p.data > data else p.rtree
        return p

    def insert(self, data):
        '''
        插入
        '''
        if not self.base:
            self.base = Tree(data=data)
            return
        pp = None
        p = self.base
        while p:
            pp = p
            p = p.ltree if p.data > data else p.rtree
        new_p = Tree(data=data)
        if pp.data > data:
            pp.ltree = new_p
        else:
            pp.rtree = new_p

    def delete(self, data):
        '''
        删除
        '''
        p = self.base
        pp = None
        while p and (p.data != data):
            pp = p
            p = p.ltree if p.data > data else p.rtree
        if not p: return

        if p.ltree and p.rtree:
            successor = p.rtree
            successor_pp = p
            while successor.ltree:
                successor_pp = successor
                successor = successor.ltree
            p.data = successor.da
            pp, p = successor_pp, successor

        child = p.ltree if p.ltree else p.rtree
        if not pp:
            self.base = child
        elif pp.ltree == p:
            pp.ltree = p
        else:
            pp.rtree = child


if __name__ == '__main__':
    tree = Tree(data=3)
    bst = BinarySearchTree(tree)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)
    bst.insert(8)
    bst.insert(10)
    bst.insert(13)
    bst.insert(33)
    bst.insert(44)
    bst.insert(1)
    bst.insert(2)
    target = bst.find(8)
    print("--------------------")
    print(target.data)
    print(target.ltree)
    print(target.rtree.data)
    print("++++++++++++++++++++")
    bst.delete(8)
    print(bst.find(8))
