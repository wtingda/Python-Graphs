# (c) 2017 Tingda Wang
# Queue implementation using linkedlists, similar to the dequeue package

from LinkedList import SinglyLinkedList

class Queue():

    def __init__(self, ls = None):
        self.queue = SinglyLinkedList()

        if ls:
            self.build(ls)

    def build(self, ls):
        for x in ls:
            self.queue.addback(x)

    def enqueue(self, item):
        self.queue.addback(item)

    def dequeue(self):
        return self.queue.removefront()

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return "Start of Queue: " + '<-'.join(str(self.queue).split('->')) + " End"

if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(4)
    q.enqueue(3)
    q.enqueue(2)
    print(q)
