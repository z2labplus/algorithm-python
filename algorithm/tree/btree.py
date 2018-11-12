class Tree(object):
    def __init__(self, ltree=0, rtree=0, data=0):
        self.data = data
        self.ltree = ltree
        self.rtree = rtree


class BTree(object):
    def __init__(self, base=0):
        self.base = base

    def pre_out(self, tree_base):
        '''
        前序遍历
        '''
        if tree_base == 0:
            return
        print(tree_base.data)
        self.pre_out(tree_base.ltree)
        self.pre_out(tree_base.rtree)

    def in_out(self, tree_base):
        '''
        中序遍历
        '''
        if tree_base == 0:
            return
        self.in_out(tree_base.ltree)
        print(tree_base.data)
        self.in_out(tree_base.rtree)

    def post_out(self, tree_base):
        '''
        后序遍历
        '''
        if tree_base == 0:
            return
        self.in_out(tree_base.ltree)
        self.in_out(tree_base.rtree)
        print(tree_base.data)


if __name__ == '__main__':
    tree1 = Tree(data=1)
    tree2 = Tree(data=2)
    tree3 = Tree(tree1, data=3)
    tree4 = Tree(tree2, 0, data=5)
    base = Tree(tree3, tree4, 6)
    btree = BTree(base)

    btree = BTree(base)
    print("----pre_out----")
    btree.pre_out(btree.base)
    print("----in_out----")
    btree.in_out(btree.base)
    print("----post_out----")
    btree.post_out(btree.base)
