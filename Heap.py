# (c) 2017 Tingda Wang
# Heap data structure as well as additional Heap-based PriorityQueue implementation

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
        ''' Heap based PriorityQueue with optional list args to build Heap using list'''
        self.maxheap = Heap()

        if ls:
            self.maxheap.build(ls)

    def push(self, item):
        ''' inserting item into Heap'''
        self.maxheap.insert(item)

    def pop(self):
        ''' removing top item from heap'''
        return self.maxheap.remove_index(0)

    def __str__(self):
        return str(self.maxheap)

if __name__ == '__main__':

    h = Heap()
    h.build([16,85,4,6,3,7,2])
    print(h)
    h.insert(14)
    print(h)
    h.insert(100)
    print(h)
    h.remove(85)
    print(h)

    p = PriorityHeap()
    p.push(4)
    p.push(3)
    p.push(2)
    p.push(123)
    p.push(5)
    print(p.pop())
    print(p.pop())
