# (c) 2017 Tingda Wang
# Stack implementation, even with O(n^2) sorting!

class Stack():

    def __init__(self, ls = []):
        self.ls = ls

    def push(self, item):
        self.ls.append(item)


    def peek(self):
        return self.ls[-1]
    
    def pop(self):
        item = self.ls[-1]
        del self.ls[-1]
        return item

    @property
    def empty(self):
        return self.__len__() == 0

    # i'm so sorry
    @property
    def overflow(self):
        raise Exception("Stack Overflow!!!!!!!!!!!!!!!!!!!!!!!!")
    
    def __len__(self):
        return len(self.ls)

    def __str__(self):
        s = '\n-\n'.join([str(i) for i in self.ls[::-1]])
        return '-\n' + s + '\n____\nStack\n'

def stacksort(stack):
    ''' sorts a stack using a temporary stack in O(n^2) time'''
    tmp = Stack()
    while not stack.empty:
        item = stack.pop()
        while not tmp.empty and item < tmp.peek():
            stack.push(tmp.pop())
        tmp.push(item)

    return tmp

def stacksort_recursive(stack):
    ''' recursive stack sort using the interpreter's stack'''
    if not stack.empty:
        item = stack.pop()
        stacksort_recursive(stack)

        def insert(stack, item):
            ''' helper function to insert item into correct location'''
            if not stack.empty and stack.peek() > item:
                tmp = stack.pop()
                insert(stack, item)
                stack.push(tmp)
            else:
                stack.push(item)

        insert(stack, item)

    
if __name__ == '__main__':
    
    stack = Stack([1,2,3,4])
    stack.push(7)
    stack.pop()
    stack.pop()
    stack.push(4)
    stack.push(5)
    print(stack)

    
    stack = Stack([5,7,8,1,4])
    print(stacksort(stack))

    stack = Stack([5,7,8,1,4])
    stacksort_recursive(stack)
    print(stack)

    stack.overflow
