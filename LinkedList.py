# (c) 2017 Tingda Wang
# Python Linked List data structures (singly, doubly, and circularly)


class Node():
    '''abstract node class for various node types'''
    
    def __init__(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def set_item(self, item):
        self.item = item

    def copy(self):
        return Node(self.item)

    # --- special methods ---

    def __str__(self):
        return str(self.item)
    
    def __repr__(self):
        return 'Node: ' + self.__str__()

    def __hash__(self):
        return hash(self.item)

    def __format__(self, formatitem):
        return 'Node: {}'.format(self.item).__format__(formatitem)

    def __eq__(self, other):
        return isinstance(other, type(self)) and other.item == self.item

    def __lt__(self, other):
        return isinstance(other, type(self)) and other.item >= self.item

    def __le__(self, other):
        return isinstance(other, type(self)) and other.item >= self.item

    def __bool__(self):
        return self.item is not None
 
class SLLNode(Node):
    ''' node class for SinglyLinkedList nodes, with wrapper functions '''

    def __init__(self, item, next = None):
        super().__init__(item)
        self.next = next
    
    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next is not None
    
    # override
    def copy(self):
        return SLLNode(self.item, self.next)

    #override
    def __str__(self):
        return "SLLNode: %s" % self.item

class SinglyLinkedList():
    ''' SinglyLinkedList with a head and tail pointer '''

    def __init__(self, head = None):
        self.head = self.tail = SLLNode(head) if head else None
        self.size = 1 if self.head else 0

    def add(self, item, index):
        if index == 0 or not self.head:
            self.addfront(item)
        elif index == self.size:
            self.addback(item)
        elif index < self.size and index > 0:
            curr = self.head
            while index - 1 > 0: # move to node that will point to new item
                curr = curr.get_next()
                index -= 1
            # create node pointing to curr.next
            temp = SLLNode(item, next = curr.get_next())
            curr.set_next(temp) # set node as after curr
            self.size += 1
        else:
            raise IndexError

    def addfront(self, item):
        self.head = SLLNode(item, next = self.head)
        self.tail = self.tail if self.tail else self.head # in case SLL empty
        self.size += 1
    
    def addback(self, item): # aka append
        newtail = SLLNode(item, next = None)
        if self.tail:
            self.tail.set_next(newtail)
        self.tail = newtail
        self.head = self.head if self.head else self.tail
        self.size += 1
    
    def gethead(self):
        return self.head
    
    def gettail(self):
        return self.tail

    def __getitem__(self, index):
        if index == 0:
            return self.gethead()
        elif index == self.size - 1:
            return self.gettail()
        elif index > 0 and index < self.size - 1:
            curr = self.head
            while index > 0:
                index -= 1
                curr = curr.get_next()
            return curr
        else:
            raise IndexError
        
    def __setitem__(self, index, item):
        if index == 0:
            self.head.set_item(item)
        elif index == self.size - 1:
            self.tail.set_item(item)
        elif index > 0 and index < self.size - 1:
           curr = self.head
           while index > 0:
               index -= 1
               curr = curr.get_next()
           curr.set_item(item)
        else:
            raise IndexError
    
    def removefront(self): 
        # returns removed head
        removed = self.head
        self.head = self.head.get_next()
        self.size -= 1
        return removed
    
    def removetail(self): 
        # returns removed tail
        # warning: expensive! has to traverse whole list to find new tail
        removed = self.tail
        self.tail = self.__getitem__(self.size - 2) # get second to last node
        self.size -= 1 # decrement after to avoid calling gettail
        return removed

    def __delitem__(self, index): # returns removed item
        if index == 0:
            return self.removefront()
        elif index == self.size - 1:
            return self.removetail()
        elif index > 0 and index < self.size - 1:
            curr = self.head
            while index > 1:
                curr = curr.get_next()
                index -= 1
            removed = curr.get_next()
            self.size -= 1
            curr.set_next(removed.get_next())
            return removed
        else:
            raise IndexError        
                
    def __len__(self):
        return self.size

    def __contains__(self, item):
        curr = self.head
        while curr.has_next():
            if curr.get_item() == item:
                return True
            else:
                curr = curr.get_next()

        return curr.get_item() == item

    def __iter__(self):
        self.curr = SLLNode(None, next = self.head)
        return self

    def __next__(self):
        if self.curr.has_next():
            self.curr = self.curr.get_next()
            return self.curr 
        else:
            raise StopIteration

    def __str__(self):

        curr = self.head
        string = [str(curr.get_item())]

        while curr.has_next():
            curr = curr.get_next()
            string.append(str(curr.get_item()))
            
        return ' -> '.join(string)

class CircularLinkedList():
    ''' circular singly linked list with head pointer '''
    
    def __init__(self, head = None):
        self.head = SLLNode(head)
        self.size = 1 if head else 0
        self.has_cycle = False

    def addfront(self, item):
        self.head = SLLNode(item, next = self.head)
        self.size += 1

    def add(self, item, index):
        if index == 0 or not self.head:
            self.addfront(item)

        elif index <= self.size and index > 0:
            
            # get node that points to item
            curr = self.__getitem__(index - 1)

            # creates target node pointing to curr.next                                                                                  
            temp = SLLNode(item, next = curr.get_next())
            curr.set_next(temp) # set node as after curr                       
            self.size += 1
        else:
            raise IndexError
        
    def get_head(self):
        return self.head

    def get_tail(self):
        curr = self.head
        while curr.has_next():
            curr = curr.get_next()
        return curr

    def __getitem__(self, index):
        if index == 0:
            return self.get_head()
        elif index == self.size - 1:
            return self.gettail()
        elif index > 0 and index < self.size - 1:
            curr = self.head
            while index > 0:
                index -= 1
                curr = curr.get_next()
            return curr
        else:
            raise IndexError

    def create_cycle(self, index):
        ''' creates cycle between node at index and tail node'''
        assert index < self.size - 1, "index cannot be last!"
        tail = self.get_tail()
        item = self.__getitem__(index)
        tail.set_next(item)
        self.has_cycle = True
    
    def get_cycle(self):
        ''' 
        returns the node at start of cycle
        implemented for practice, could've just stored cycle node during create_cycle :)
        '''
        if self.has_cycle:
            slow = self.head.get_next()
            fast = slow.get_next()
            
            # find meeting pt
            while slow != fast:
                slow = slow.get_next()
                fast = fast.get_next().get_next()

            fast = self.head
            while slow != fast: # get start of cycle
                fast = fast.get_next()
                slow = slow.get_next()

            return fast
        else:
            return None
 
    def __len__(self):
        return self.size

    def __contains__(self, item):
        curr = self.head
        counter = self.size
        while curr.has_next and counter > 0:
            if curr.get_item() == item:
                return True
            else:
                curr = curr.get_next()
                counter -= 1
        return curr.get_item() == item

    def __iter__(self):
        self.curr = SLLNode(None, next = self.head)
        self.counter = self.size
        return self

    def __next__(self):
        if self.curr.has_next() and self.counter > 0:
            self.curr = self.curr.get_next()
            self.counter -= 1
            return self.curr 
        else:
            raise StopIteration

    def __str__(self):

        curr = self.head
        string = [str(curr.get_item())]
        counter = self.size - 1
        while curr.has_next() and counter > 0:
            curr = curr.get_next()
            string.append(str(curr.get_item()))
            counter -= 1

        if self.has_cycle:
            string.append(str(self.get_cycle().get_item()))

        return ' -> '.join(string)

    
class DLLNode(Node):
    ''' node class for DoublyLinkedList nodes, with wrapper functions '''
    def __init__(self, item, next = None, prev = None):
        super().__init__(item)
        self.next = next
        self.prev = prev
    
    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next is not None

    def set_prev(self, prev):
        self.prev = prev

    def get_prev(self):
        return self.prev

    def has_prev(self):
        return self.prev is not None

    #override
    def __str__(self):
        return "DLLNode: %s" % self.item

class DoublyLinkedList():
    ''' SinglyLinkedList with a head and tail pointer '''
    def __init__(self, head = None):
        self.head = self.tail = DLLNode(head) if head else None
        self.size = 1 if self.head else 0

    def add(self, item, index):
        if index == 0 or not self.head:
            self.addfront(item)
        elif index == self.size:
            self.addback(item)
        elif index < self.size and index > 0:
            if index < self.size // 2:
                
                curr = self.head
                while index - 1 > 0: # move to node that will point to new item
                    curr = curr.get_next()
                    index -= 1

                # create node pointing to curr.next            
                temp = DLLNode(item, next = curr.get_next(), prev = curr)
                curr.get_next().set_prev(temp)
                curr.set_next(temp) # set node as after curr
                self.size += 1
            else:
                curr = self.tail
                while index + 1 < self.size: # move to node that new item points to
                    curr = curr.get_prev()
                    index += 1
                temp = DLLNode(item, next = curr, prev = curr.get_prev())
                curr.get_prev().set_next(temp)
                curr.set_prev(temp)
                self.size += 1
        else:
            raise IndexError

    def addfront(self, item):
        newhead = DLLNode(item, next = self.head, prev = None)
        
        if self.head:
            self.head.set_prev(newhead)
        
        self.head = newhead
        self.tail = self.tail if self.tail else self.head # in case SLL empty
        self.size += 1
    
    def addback(self, item): # aka append
        newtail = DLLNode(item, next = None, prev = self.tail)
        if self.tail:
            self.tail.set_next(newtail)
        self.tail = newtail
        self.head = self.head if self.head else self.tail # in case empty
        self.size += 1
    
    def gethead(self):
        return self.head
    
    def gettail(self):
        return self.tail

    def __getitem__(self, index): # optimizes traversal to start at end closer to index
        if index == 0:
            return self.gethead()
        elif index == self.size - 1:
            return self.gettail()
        elif index > 0 and index < self.size - 1:
            if index < self.size // 2:
                curr = self.head
                while index > 0:
                    index -= 1
                    curr = curr.get_next()
                return curr
            else:
                curr = self.tail
                while index < self.size - 1:
                    index += 1
                    curr = curr.get_prev()
                return curr
        else:
            raise IndexError
        
    def __setitem__(self, index, item):
        if index == 0:
            self.head.set_item(item)
        elif index == self.size - 1:
            self.tail.set_item(item)
        elif index > 0 and index < self.size - 1:
            if index < self.size // 2:
                
                curr = self.head
                while index > 0:
                    index -= 1
                    curr = curr.get_next()
                curr.set_item(item)
            else:
                curr = self.tail
                while index < self.size - 1:
                    index += 1
                    curr =  curr.get_prev()
                curr.set_item(item)
        else:
            raise IndexError
    
    def removefront(self): 
        # returns removed head
        removed = self.head
        self.head = self.head.get_next()
        self.head.set_prev(removed.get_prev())
        self.size -= 1
        return removed
    
    def removetail(self): 
        # returns removed tail (it's fast now!)
        removed = self.tail
        self.tail = removed.get_prev()
        self.tail.set_next(removed.get_next())
        self.size -= 1 # decrement after to avoid calling gettail
        return removed

    def __delitem__(self, index): # returns removed item
        if index == 0:
            return self.removefront()
        elif index == self.size - 1:
            return self.removetail()
        elif index > 0 and index < self.size - 1:
            if index < self.size // 2:
                curr = self.head
                while index > 0:
                    curr = curr.get_next()
                    index -= 1
                prev = curr.get_prev()
                next = curr.get_next()
                prev.set_next(next)
                next.set_prev(prev)
                self.size -= 1
                return curr
            else:
                curr = self.tail
                while index < self.size - 1:
                    curr = curr.get_prev()
                    index += 1
                prev = curr.get_prev()
                next = curr.get_next()
                prev.set_next(next)
                next.set_prev(prev)
                self.size -= 1
                return curr
        else:
            raise IndexError        
                
    def __len__(self):
        return self.size

    def __contains__(self, item):
        curr = self.head
        while curr.has_next():
            if curr.get_item() == item:
                return True
            else:
                curr = curr.get_next()
        return curr.get_item() == item

    def __iter__(self):
        self.curr = DLLNode(None, next = self.head, prev = None)
        return self

    def __next__(self):
        if self.curr.has_next():
            self.curr = self.curr.get_next()
            return self.curr 
        else:
            raise StopIteration

    def __reversed__(self):
        curr = DLLNode(None, next = None, prev = self.tail)
        while curr.has_prev():
            curr = curr.get_prev()
            yield curr

    def __str__(self):

        curr = self.head
        string = [str(curr.get_item())]

        while curr.has_next():
            curr = curr.get_next()
            string.append(str(curr.get_item()))
            
        return ' <-> '.join(string)


def remove_dup(list):
    ''' removes duplicates in SLL '''
    assert isinstance(list, SinglyLinkedList), "list must be a SLL!"
    curr = list.gethead()
    map = {}
    map[curr] = 1
    while curr.has_next():
        if curr.get_next() in map:
            curr.set_next(curr.get_next().get_next())
            print(list)
        else:
            map[curr.get_next()] = 1
            curr = curr.get_next()

def remove_inplace(list):
    ''' removes duplicates in place '''
    assert isinstance(list, SinglyLinkedList), "list must be a SLL!"
    curr = list.gethead()
    while curr:
        tmp = curr
        while tmp:
            if curr == tmp.get_next():
                tmp.set_next(tmp.get_next().get_next())
            else:
                tmp = tmp.get_next()
        curr = curr.get_next()

def ktolast(ls, k):
    ''' returns kth to last item in SLL'''
    first = ls.gethead()
    second = ls.gethead()
    
    while first.has_next():
        first = first.get_next()
        if k > 0:
            k -= 1
        else:
            second = second.get_next()

    return second

def deletemiddle(node):
    ''' deletes node at the middle of SLL '''
    if node.has_next():
        node.set_item(node.get_next().get_item())
        node.set_next(node.get_next().get_next())
    else:
        node = None

if __name__ == '__main__':

    sll = SinglyLinkedList()
    sll.addfront(6)
    sll.addfront(5)
    print(sll)
    sll.add(8, 2)
    sll.add(7, 2)
    print(sll)
    sll.add(9, 3)
    print(sll)
    del sll[0]
    print(sll)
    
    remove_dup(sll)
    print(sll)

    dll = DoublyLinkedList()
    dll.addfront(6)
    dll.addfront(5)
    print(dll)
    dll.add(8, 2)
    dll.add(7, 2)
    print(dll)
    dll.add(9, 3)
    print(dll)
    del dll[0]
    print(dll)
    
    sll = SinglyLinkedList()
    sll.addfront(1)
    sll.addfront(1)
    sll.addfront(1)
    sll.addfront(1)
    
    remove_inplace(sll)
    print(sll)

    cll = CircularLinkedList()
    cll.addfront(6)
    cll.addfront(5)

    cll.add(4, 1)
    print(cll)
    cll.create_cycle(1)
    print(cll.get_cycle)
    print(cll)
