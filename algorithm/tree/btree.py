class Tree(object):
    def __init__(self, ltree=None, rtree=None, data=None):
        self.data = data
        self.ltree = ltree
        self.rtree = rtree


class BTree(object):
    def __init__(self, base):
        self.base = base

    def pre_out(self, tree_base):
        '''
        前序遍历
        '''
        if tree_base == None:
            return
        print(tree_base.data)
        self.pre_out(tree_base.ltree)
        self.pre_out(tree_base.rtree)

    def in_out(self, tree_base):
        '''
        中序遍历
        '''
        if tree_base == None:
            return
        self.in_out(tree_base.ltree)
        print(tree_base.data)
        self.in_out(tree_base.rtree)

    def post_out(self, tree_base):
        '''
        后序遍历
        '''
        if tree_base == None:
            return
        self.in_out(tree_base.rtree)
        print(tree_base.data)
        self.in_out(tree_base.ltree)


if __name__ == '__main__':
    rtree2 = Tree(data=7)
    ltree2 = Tree(data=6)
    rtree = Tree(ltree=ltree2, rtree=rtree2, data=3)

    ltree1 = Tree(data=4)
    rtree1 = Tree(data=5)
    ltree = Tree(ltree=ltree1, rtree=rtree1, data=2)
    base = Tree(ltree=ltree, rtree=rtree, data=1)

    btree = BTree(base)
    print("----pre_out----")
    btree.pre_out(btree.base)
    print("----in_out----")
    btree.in_out(btree.base)
    print("----post_out----")
    btree.post_out(btree.base)
