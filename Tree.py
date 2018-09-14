# mainly some binary tree traversals
# (c) 2017 Tingda Wang

from LinkedList import Node

class TreeNode(Node):
    ''' basic tree node'''

    def __init__(self, value, left = None, right = None):
        super().__init__(value)
        self.left = left
        self.right = right

    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def set_left(self, left):
        self.left = left
        
    def set_right(self, right):
        self.right = right
        
    def is_leaf(self):
        return not (self.has_left() or self.has_right())    

     # override
    def __repr__(self):
        return "TreeNode(value: %s, left: %s, right: %s)" %(self.item, self.left, self.right)


class Tree():

    def __init__(self, value = None):
        self.root = TreeNode(value)
        self.size = 1 if value else 0


    def get_root(self):
        return self.root

    def __str__(self, depth = 0, node = -1):
        ''' pretty prints tree sideways'''
        node = self.root if node == -1 else node
    
        tree = []
        
        # print right
        if node.has_right():
            tree.append(self.__str__(depth + 1, node.get_right()))

        tree.append('\n')
        
        # print self
        tree.append(("    "*depth) + str(node.get_item()))

        tree.append('\n')
        
        # print left
        if node.has_left():
            tree.append(self.__str__(depth + 1, node.get_left()))

        return ''.join(tree)

    
    # recursive tree traversals
    
    def in_order(self, node = -1):
        node = self.root if node == -1 else node
        
        if node:
            self.in_order(node.get_left())
            print(node.get_item())
            self.in_order(node.get_right())

    def pre_order(self, node = -1):
        node = self.root if node == -1 else node

        if node:
            print(node.get_item())
            self.pre_order(node.get_left())
            self.pre_order(node.get_right())

    def post_order(self, node = -1):
        node = self.root if node == -1 else node
        
        if node:
            self.post_order(node.get_left())
            self.post_order(node.get_right())
            print(node.get_item())

    def level_order(self, node = -1):
        ''' not really recursive... '''
        node = self.root if node == -1 else node
        current_level = [node]
        while current_level:
            # a less beautiful way to print tree structure, but gets clearer idea
            print(' '.join(str(n.get_item()) for n in current_level))
            next_level = []
            for i in current_level:
                if i.has_left():
                    next_level.append(i.get_left())
                if i.has_right():
                    next_level.append(i.get_right())
            current_level = next_level

if __name__ == "__main__":
    tree = Tree('d')
    root = tree.get_root()
    root.set_left(TreeNode("b"))
    root.set_right(TreeNode("f"))
    root.get_left().set_left(TreeNode("a"))
    root.get_left().set_right(TreeNode("c"))
    root.get_right().set_left(TreeNode("e"))
    root.get_right().set_right(TreeNode("g"))

    print("tree looks like: ")
    print(tree)
    print("\npre-order traversal of the tree: ")
    tree.pre_order()
    print("\nin-order traversal of the tree: ")
    tree.in_order()
    print("\npost-order traversal of the tree: ")
    tree.post_order()
    print("\nlevel-order traversal of the tree: ")
    tree.level_order()
