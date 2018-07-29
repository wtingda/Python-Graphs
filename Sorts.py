# (c) 2017 Tingda Wang
# So many sorting algorithms!

import random

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

# dirty one liner that will get you kicked out of any bar you go into
qsort = lambda l : l if len(l) < 2 else qsort([x for x in l[1:] if x < l[0]]) + [l[0]] + qsort([x for x in l[1:] if x >= l[0]])

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

def quicksort3(x, start = 0, end = None):
    end = end if end is not None else len(x) - 1

    if start < end:
        pivot = partition3(x, start, end)
        
        quicksort3(x, start, pivot - 1)
        quicksort3(x, pivot + 1, end)


def partition3(x, start, end):
    
    pivot = random.randint(start, end)
    x[start], x[pivot] = x[pivot], x[start]

    pivot = start

    for i in range(start + 1, end + 1):
        if x[start] > x[i]:
            pivot += 1
            x[i], x[pivot] = x[pivot], x[i]

    x[pivot], x[start] = x[start], x[pivot]
    
    return pivot


def heapsort3(x):
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

# recursive
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

# dangerous material
def bogosort(ls):
    ''' Don't try this at home... '''

    sorted = False
    
    while not sorted:
        
        random.shuffle(ls)
        sorted = True
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                sorted = False
    
        
if __name__ == '__main__':

    
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

    x = [5,48,1,4,7,843,21,8,2]
    heapsort3(x)
    print(x)

    x = [5,48,1,4,7,843,21,8,2]
    heapsortr(x)
    print(x)

    x = [9,8,7,6,5,4,3,2,1]
    quicksort3(x)
    print(x)

    # try at your own peril
    ''' 
    x = [random.randint(1, 100) for _ in range(random.randint(5, 10))]
    print("unsorted: %s" %x)
    bogosort(x)
    print("sorted: %s\n" %x)
    '''
