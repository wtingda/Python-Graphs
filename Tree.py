# some binary tree traversals and tree printing 
# (c) 2017 @author Tingda Wang

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

    # pretty printing of tree structure side ways
    def __str__(self, depth = 0):
        tree = ""
        # print right
        if self.right:
            tree += self.right.__str__(depth + 1)
        # print self
        tree += "\n" + ("    "*depth) + str(self.val)
        # print left
        if self.left:
            tree += self.left.__str__(depth + 1)
        return tree

def in_order(root):
    if root:
        in_order(root.left)
        print(root.val)
        in_order(root.right)

def pre_order(root):
    if root:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val)

def level_order(root):
    current_level = [root]
    while current_level:
        # a less beautiful way to print tree structure, but gets clearer idea
        print(' '.join(str(node.val) for node in current_level))
        next_level = []
        for i in current_level:
            if i.left:
                next_level.append(i.left)
            if i.right:
                next_level.append(i.right)
            current_level = next_level

if __name__ == "__main__":
    
    root = Node("d")
    root.left = Node("b")
    root.right = Node("f")
    root.left.left = Node("a")
    root.left.right = Node("c")
    root.right.left = Node("e")
    root.right.right = Node("g")

    print("tree looks like: ")
    print(root)
    print("\npre-order traversal of the tree: ")
    pre_order(root)
    print("\nin-order traversal of the tree: ")
    in_order(root)
    print("\npost-order traversal of the tree: ")
    post_order(root)
    print("\nlevel-order traversal of the tree: ")
    level_order(root)
