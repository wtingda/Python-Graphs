import random

def quicksort(x, start = 0, end = None):
    end = end if end is not None else len(x) - 1

    if start < end:
        pivot = partition(x, start, end)
        
        quicksort(x, start, pivot - 1)
        quicksort(x, pivot + 1, end)


def partition(x, start, end):
    
    #pivot = random.randint(start, end)
    #x[start], x[pivot] = x[pivot], x[start]

    pivot = start

    for i in range(start + 1, end + 1):
        if x[start] > x[i]:
            pivot += 1
            x[i], x[pivot] = x[pivot], x[i]

    x[pivot], x[start] = x[start], x[pivot]
    
    return pivot


def heapsort(x):
    for i in reversed(range(len(x) // 2)):
        siftd(x, i, len(x) - 1)

    for i in reversed(range(len(x))):
        x[0], x[i] = x[i], x[0]
        siftd(x, 0, i - 1)


def siftd(x, start, end):

    parent = x[start]

    while start * 2 + 1 <= end:
        c_i = start * 2 + 1
        if c_i + 1 <= end:
            c_i += 1 if x[c_i] < x[c_i + 1] else 0

        child = x[c_i]

        if parent < child:
            x[start] = child
            start = c_i
        else:
            break
    x[start] = parent

def heapsortr(x):
    for i in reversed(range(len(x) // 2)):
        siftrecursive(x, i, len(x) - 1)

    for i in reversed(range(len(x))):
        x[0], x[i] = x[i], x[0]
        siftrecursive(x, 0, i - 1)


def siftrecursive(x, start, end):

    parent = x[start]

    if start * 2 + 1 <= end:
        c_i = start * 2 + 1
        if c_i + 1 <= end:
            c_i += 1 if x[c_i] < x[c_i + 1] else 0

        child = x[c_i]

        if parent < child:
            x[start] = child
            x[c_i] = parent
            siftrecursive(x, c_i, end)

if __name__ == '__main__':

    x = [5,48,1,4,7,843,21,8,2]
    heapsort(x)
    print(x)

    x = [5,48,1,4,7,843,21,8,2]
    heapsortr(x)
    print(x)

    x = [9,8,7,6,5,4,3,2,1]
    quicksort(x)
    print(x)
