# (c) 2017 Tingda Wang
# Binary Search Tree

from LinkedList import Node

import math

INF = math.inf

class BTNode(Node):
    ''' Binary Tree Node class, extends from generic Node class '''
    def __init__(self, value, left = None, right = None, parent = None):
        super().__init__(value)
        self.left = left
        self.right = right
        self.parent = parent
        
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right

    def get_parent(self):
        return self.parent
    
    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not (self.has_left() or self.has_right())

    @property
    def height(self):
        ''' determines height of node, if no children then has 0 height'''
        if self.is_leaf():
            return 0
        elif self.has_right() and self.has_left():
            return 1 + max(self.get_right().height, self.get_left().height)
        elif self.has_right():
            return 1 + self.get_right().height
        else: # has only left child
            return 1 + self.get_left().height
        
    def set_left(self, left):
        self.left = left
        self.left.set_parent(self)
        
    def set_right(self, right):
        self.right = right
        self.right.set_parent(self)
        
    def set_parent(self, parent):
        self.parent = parent
        
    # override
    def __repr__(self):
        return "BSTNode(value: %s, left: %s, right: %s)" %(self.item, self.left, self.right)


class BST:
    ''' binary search tree '''
    
    def __init__(self, nodes = []):
        self.size = len(nodes)
        self.root = None
        if nodes:
            self._build_tree(nodes)

    @property
    def is_empty(self):
        ''' boolean of whether BST is empty '''
        return self.root is None

    @property
    def height(self):
        ''' returns height of BST '''
        if not self.is_empty:
            return self.root.height
        else: # empty tree doesn't have height
            return -1
        
    def _build_tree(self, nodes):
        ''' builds BST'''
        if self.is_empty:
            self.root = BTNode(nodes.pop())

        self._add_nodes(nodes)
            

    def _add_nodes(self, nodes):
        ''' helper to add the rest of the nodes'''
        if nodes:
            self._insert(nodes.pop())
            self._add_nodes(nodes)
            

    def _insert(self, node, curr = -1):
        ''' inserts node into proper location but doesn't balance'''

        curr = self.root if curr == -1 else curr

        if self.is_empty:
            # one node only
            self.root = BTNode(node)
        else:
            if node < curr.get_item(): # go left
                if curr.has_left():
                    self._insert(node, curr.get_left())
                else:
                    curr.set_left(BTNode(node))
            else: # go right
                if curr.has_right():
                   self. _insert(node, curr.get_right())
                else:
                    curr.set_right(BTNode(node))

    def _delete(self, item):
        ''' deletes the node from BSt while maintaining BSt property '''

        curr = self.root

        # find the node
        while curr and curr.get_item() != item:
            if curr.get_item < item:
                curr = curr.get_left()

            else:
                curr = curr.get_right

        if curr is None:
            raise LookupError("No such item %s!" %item)

        else: # we have the node we want to delete

            # case 1: leaf, just delete
            if not (curr.has_left() or curr.has_right()):
                self._replace_child(curr, curr.get_parent())

            # case 2: has one child, make that child replace this one in parent
            elif curr.has_left():
                self._replace_child(curr, curr.get_parent(), curr.get_left())
            elif curr.has_right():
                self._replace_child(curr, curr.get_parent(), curr.get_right())

            else: # case 3: has two children, get inorder successor to replace

                replacement = curr.get_right() # has to have right child

                while replacement.has_left():
                    replacement = replacement.get_left()

                    # delete replacement
                    self._replace_child(replacement, replacement.get_parent())

                    # replace curr with it
                    self._replace_child(curr, curr.get_parent(), replacement)
                
            return curr

    def _replace_child(self, node, parent, newchild = None):
        ''' helper to delete node from parent by determining if it is left or right child '''
        if newchild:
            newchild.set_parent(parent)

        if parent.has_left() and parent.get_left() is node:
            parent.set_left(newchild)
                
        elif parent.has_right() and parent.get_right() is node:
            parent.set_right(newchild)
    
        else:
            raise LookupError("No such child %s!" %node)
            
    def get_root(self):
        ''' returns root '''
        return self.root

    def __len__(self):
        ''' returns size of tree '''
        return self.size
    
    def __contains__(self, item, curr = -1):
        ''' performs a binary search to see if item is in BST '''
        curr = self.root if curr == -1 else curr

        if curr is None:
            return False
        elif curr.get_item() == item:
            return True
        elif item > curr.get_item():
            return self.__contains__(item, curr = curr.get_right())
        else:
            return self.__contains__(item, curr = curr.get_left())

    def __iter__(self):
        self.curr = None
        return self

    def __next__(self):
        ''' returns next in-order node'''
        if self.curr: # get next in-order node

            if self.curr.has_right(): # if has right child
                self.curr = self.curr.get_right()

                # keep going left from right child to get smallest node bigger than curr
                while self.curr.has_left():
                    self.curr = self.curr.get_left()

                return self.curr
            
            else: # have to get ancestor that has curr on left child branch
                while not self.curr.is_root():
                    if self.curr.get_parent().get_left() == self.curr:
                        self.curr = self.curr.get_parent()
                        return self.curr

                    else:
                        self.curr = self.curr.get_parent()
                
                raise StopIteration    

        else: # first node

            self.curr = self.root
            while self.curr.has_left():
                self.curr = self.curr.get_left()
            
            return self.curr
            
        
    def __str__(self, depth = 0, node = -1):
        ''' prints BST sideways, with reasonable readability'''
        node = self.root if node == -1 else node
        
        left, right = ('', '')
        
        if node.has_left():
            left = self.__str__(depth = depth + 1, node = node.get_left())

        if node.has_right():
            right = self.__str__(depth = depth + 1, node = node.get_right())

        curr = ("    " * depth) + str(node.get_item()) + '\n'

        return ''.join([right, curr, left])
        

def is_BST(tree, min = 0, max = INF):
    ''' checks if a tree is a valid BST '''

    def helper(node, min = 0, max = INF):
        ''' helper function'''
        if node is None:
            return True
    
        if node.get_item() >= min and node.get_item() <= max:

            return helper(node.get_left(), min, node.get_item()) and helper(node.get_right(), node.get_item(), max)
        
    return helper(tree.get_root())

if __name__ == "__main__":
    bst = BST([6,3,8,3,7])
    print(bst)
    print(3 in bst)
    print(5 in bst)
    print("height: %d " % bst.height)
    for x in bst:
        print("in order: " + str(x))
    print(is_BST(bst))
