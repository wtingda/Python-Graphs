import random

def remove_dup(list):
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
    if node.has_next():
        node.set_item(node.get_next().get_item())
        node.set_next(node.get_next().get_next())
    else:
        node = None

class HashMap():
    def __init__(self, size):
        self.size = size
        self.list = [[] for _ in range(self.size)]

    def _hashfunc(self, key):
        return key % self.size

    def __setitem__(self, key, value):
        hashkey = self._hashfunc(key)
        for item in self.list[hashkey]:
            if item[0] == key:
                item[1] = value
                return
        self.list[hashkey].append([key, value])

    def __getitem__(self, key):
        hashkey = self._hashfunc(key)
        for item in self.list[hashkey]:
            if item[0] == key:
                return item[1]
        raise KeyError
       
    def __delitem__(self, key):
        hashkey = self._hashfunc(key)
        for i in len(self.list[hashkey]):
            if self.list[hashkey][i][0] == key:
                del self.list[hashkey][i]
                return
        raise KeyError

    def items(self):
        for pair in self.list:
            yield pair[0], pair[1]

    def keys(self):
        for pair in self.list:
            yield pair[0]

    def values(self):
        for apir in self.list:
            yield pair[1]

    def __repr__(self):
        str = ', '.join(['Key %s: Value %s' %(item[0], item[1]) for buckets in self.list for item in buckets])
        return '{ ' + str + ' }'

class Heap():
    def __init__(self):
        self.heap = []
        self.size = len(self.heap) 

    def build(self, ls):
        self.heap = ls
        self.size = len(ls)
        for i in reversed(range(self.size // 2)):
            self.percolate_down(i, self.size - 1)

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.percolate_up(0, self.size - 1)
        
    def remove_index(self, index):
        try:
            item = self.heap[index]

            self.size -= 1
            
            self.heap[index] = self.heap[-1]
            del self.heap[-1]
            self.percolate_down(index, self.size - 1)
            
            return item

        except IndexError:

            print("no such index!")
            return None

    def remove(self, item):
        try:
            # get the item
            index = self.heap.index(item)
            
            # decrement size
            self.size -= 1

            # move last item to location and sift down
            self.heap[index] = self.heap[-1]
            del self.heap[-1]
            self.percolate_down(index, self.size - 1)

        except ValueError:
            print("no such item in heap!")

        return item

    def percolate_down(self, parent_index, end):
        ''' 
        we use percolate_down for O(n) heapify performance 
        since as items have higher chance of being at bottom of heap 
        (there are more nodes at the bottom), there is a higher chance 
        that the elements are closer to their correct positions
        and therefore the number of swaps will be probabalistically 
        less than percolate up
        '''
        
        # node we want to sift down
        parent = self.heap[parent_index]
        
        # while there is at least a child
        while 2 * parent_index + 1 <= end:

            max_ch_index = 2 * parent_index + 1        
            
            if max_ch_index < end: # there is a 2nd child
                # get biggest child
                max_ch_index += 1 if (self.heap[max_ch_index + 1] > self.heap[max_ch_index]) else 0

            max_child = self.heap[max_ch_index]
        
            if max_child > parent:
                # move child up (NOTE: we don't have to move parent every time)
                self.heap[parent_index] = max_child
                parent_index = max_ch_index
            else:
                break

        # move parent to proper place
        self.heap[parent_index] = parent

    def percolate_up(self, top, child_index):

        # get child to move up
        child = self.heap[child_index]

        # while it has a parent
        while (child_index - 1) // 2 >= top:
            parent_ind = (child_index - 1) // 2
            parent = self.heap[parent_ind]
            
            if parent < child:
                # move parent down
                self.heap[child_index] = parent
                child_index = parent_ind
            else:
                break

        self.heap[child_index] = child

    def __str__(self):
        level = 1
        counter = 0
        string = [[]]
        for item in self.heap:
            string[-1].append(str(item))
            counter += 1
            
            if level == counter:
                level *= 2
                counter = 0
                string.append([])

        return '\n'.join([' '.join(level) for level in string])

class PriorityHeap():
    def __init__(self, ls = None):
        self.maxheap = Heap()

        if ls:
            self.maxheap.build(ls)

    def push(self, item):
        self.maxheap.insert(item)

    def pop(self):
        return self.maxheap.remove_index(0)

    def __str__(self):
        return str(self.maxheap)

# abstract node class for various node types
class Node():
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
        ''' creates cycle with tail node'''
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
    
def fizzbuzz(n):
    for i in range(1, n + 1):
        s = 'fizz' if i % 5 == 0 else ''
        s += 'buzz' if i % 3 == 0 else ''
        print(s if s else str(i))

def first_repeat(s):
    dict = {}
    for i, c in enumerate(s):
        if c in dict:
            dict[c][0] += 1
        else:
            dict[c] = [1, i]
    minimum = len(s)
    
    for item in dict:
        if dict[item][0] == 1:
            minimum = min(dict[item][1], minimum)

    return minimum if minimum is not len(s) else "All repeat!"

def n_repeat(s, n): 
    dict = {}
    count = []
    for i, c in enumerate(s):
        if c in dict:
            dict[c][0] += 1
            count[dict[c][1]] = len(s)
            dict[c][1] = i
            count.append(len(s))
        else:
            dict[c] = [1, i]
            count.append(counter)
            counter += 1
    print(count)
    nth = [i for i, x in enumerate(count) if x == n ]
    return s[nth[0]] if nth else "There doesn't exist an %sth non repeating char" %n

def merge_sort(ls):
    if not ls or len(ls) == 1:
        return ls
    else:
        mid = int(len(ls) / 2)
        left = merge_sort(ls[:mid])
        right = merge_sort(ls[mid:])
        return merge(left, right)

def merge(left, right):
    left_ind, right_ind = 0, 0
    merged = []
    while left_ind < len(left) and right_ind < len(right):
        if left[left_ind] < right[right_ind]:
            merged.append(left[left_ind])
            left_ind += 1
        else:
            merged.append(right[right_ind])
            right_ind += 1

    return merged + left[left_ind:] + right[right_ind:]

def quicksort(ls, l = 0, r = None):    
    r = r if r is not None else len(ls) - 1
    
    if l < r:
        mid = partition(ls, l, r)
        quicksort(ls, l, mid - 1)
        quicksort(ls, mid + 1, r)

def partition(ls, l, r):
    # get random pivot to avoid O(n^2) worst case
    #pivot = random.randint(l, r)

    # move pivot to starting position
    #ls[l], ls[pivot] = ls[pivot], ls[l]
    pivot = l

    for i in range(pivot + 1, r + 1):
        if ls[i] < ls[l]:
            pivot += 1
            ls[i], ls[pivot] = ls[pivot], ls[i]
    ls[l], ls[pivot] = ls[pivot], ls[l]
    
    return pivot
    
def cheapquicksort(ls):
    return ls if not ls else quicksort([x for x in ls[1:] if x <= ls[0]]) + [ls[0]] + quicksort([x for x in ls[1:] if x > ls[0]])

def selectionsort(ls):
    for i in range(len(ls)):
        min = i
        for j in range(i, len(ls)):
            if ls[j] < ls[min]:
                min = j
        ls[i], ls[min] = ls[min], ls[i]


def bubblesort(ls):
    for i in range(len(ls)):
        swapped = False
        for j in range(len(ls) - 1 - i):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
                swapped = True
        if not swapped:
            break

def insertionsort(ls):
    for i in range(1, len(ls)):
        curr = ls[i]
        j = i - 1
        for j in reversed(range(-1, i)):
            if curr < ls[j]:
                ls[j + 1] = ls[j]
            else:
                break
        ls[j + 1] = curr            

def heapsort(ls):

    # build the heap bottom up, starting with the leaves
    for i in reversed(range(0, len(ls) // 2)):
        percolate_down(ls, i, len(x) - 1)

    # repeatedly extract elements to the end of list
    for i in reversed(range(len(ls))):
        ls[0], ls[i] = ls[i], ls[0]
        percolate_down(ls, 0, i - 1)

def percolate_down(ls, parent_index, end):
    ''' 
    we use percolate_down for O(n) heapify performance 
    since as items have higher chance of being at bottom of heap 
    (there are more nodes at the bottom), there is a higher chance 
    that the elements are closer to their correct positions
    and therefore the number of swaps will be probabalistically 
    less than percolate up
    '''
    
    # node we want to sift down
    parent = ls[parent_index]

    # while there is at least a child
    while 2 * parent_index + 1 <= end:

        max_ch_index = 2 * parent_index + 1        

        if max_ch_index < end: # there is a 2nd child
            # get biggest child
            max_ch_index += 1 if (ls[max_ch_index + 1] > ls[max_ch_index]) else 0

        max_child = ls[max_ch_index]
        
        if max_child > parent:
            # move child up (NOTE: we don't have to move parent every time)
            ls[parent_index] = max_child
            parent_index = max_ch_index
        else:
            break

    # move parent to proper place
    ls[parent_index] = parent

def percolate_up(ls, top, child_index):

    # get child to move up
    child = ls[child_index]

    # while it has a parent
    while (child_index - 1) // 2 >= top:
        parent_ind = (child_index - 1) // 2
        parent = ls[parent_ind]

        if parent < child:
            # move parent down
            ls[child_index] = parent
            child_index = parent_ind
        else:
            break

    ls[child_index] = child

# again for good measure :)
def quicksort2(ls, start = 0, end = None, verbose = True):

    if verbose and end == None:
        print("The unsorted list is:\n%s\n" %ls)

    end = len(ls) - 1 if end is None else end    

    if end > start:       
        pivot = partition2(ls, start, end)
        quicksort2(ls, start, pivot - 1)
        quicksort2(ls, pivot + 1, end)
        
        if verbose:
            print("Current sorted state:\n%s\n" %ls)

def partition2(ls, start, end):
    pivot = random.randint(start, end)
    ls[start], ls[pivot], pivot = ls[pivot], ls[start], start
    value = ls[start]
    for i in range(start + 1, end + 1):
        if ls[i] < value:
            pivot += 1
            ls[pivot], ls[i] = ls[i], ls[pivot]
    ls[pivot], ls[start] = value, ls[pivot]
    return pivot

def insertionsort2(ls): # simpler and optimized
    for i in range(1, len(ls)):
        j = i
        item = ls[i]
        for j in reversed(range(0, i)):
            if item < ls[j]:
                ls[j + 1] = ls[j]
            else:
                break
        ls[j] = item

def heapsort2(ls): # again for good measure
    for i in reversed(range(len(ls) // 2)):
        sift_down(ls, i, len(ls) - 1)

    for i in range(len(ls)):
        last = len(ls) - 1 - i
        ls[0], ls[last] = ls[last], ls[0]
        sift_down(ls, 0, last - 1)
        
def sift_down(ls, start, end):
    parent = ls[start]

    while start * 2 + 1 < len(ls):
        maxi = start * 2 + 1
        if maxi + 1 < len(ls):
            maxi += 0 if ls[maxi] > ls[maxi + 1] else 1
        maxchild = ls[maxi]
        
        if parent < maxchild:
            ls[start] = maxchild
            start = maxi
        else:
            break
    ls[start] = parent

if __name__ == '__main__':

    h = HashMap(5)
    h[5] = 'asdf'
    h[10] = 'asa'
    print(h[5])
    print(h)
    
    fizzbuzz(5)

    #print(first_repeat('geekforgeeks'))
    #print(n_repeat('geekforgeeks', 3))
    print(merge_sort([5,7,8,2,4]))
    
    x = [random.randint(1, 100) for _ in range(random.randint(10,30))]
    print("unsorted: %s" %x)
    quicksort2(x)
    print("sorted: %s\n" %x)
    
    x = [random.randint(1, 100) for _ in range(random.randint(10,30))]
    print("unsorted: %s" %x)
    selectionsort(x)
    print("sorted: %s\n" %x)

    x = [random.randint(1, 100) for _ in range(random.randint(10,30))]
    print("unsorted: %s" %x)
    bubblesort(x)
    print("sorted: %s\n" %x)

    x = [random.randint(1, 100) for _ in range(random.randint(10,30))]
    print("unsorted: %s" %x)
    insertionsort2(x)
    print("sorted: %s\n" %x)

    x = [random.randint(1, 100) for _ in range(random.randint(10,30))]
    print("unsorted: %s" %x)
    heapsort(x)
    print("sorted: %s\n" %x)
    
    h = Heap()
    h.build([16,85,4,6,3,7,2])
    print(h)
    h.insert(14)
    print(h )
    h.insert(100)
    print(h)
    h.remove(85)
    print(h)

    n = Node(6)
    m = Node(5)
    print('hi: {}'.format(m))

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
    '''
    deletemiddle(sll.tail)
    print(sll)

    p = PriorityHeap()
    p.push(4)
    p.push(3)
    p.push(2)
    p.push(123)
    p.push(5)
    print(p.pop())
    print(p.pop())
    '''

    cll = CircularLinkedList()
    cll.addfront(6)
    cll.addfront(5)

    cll.add(4, 1)
    print(cll)
    cll.create_cycle(1)
    print(cll.get_cycle)
    print(cll)


    x = [9,8,7,6,5,4,3,2,1]
    quicksort(x)
    print(x)
