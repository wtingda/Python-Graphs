# different sorting algorithms in Python
# (c) 2017 @author Tingda Wang

import random as r

def insertion_sort(x):
    for i in range(1,len(x)):
        curr = x[i]
        pos = i
        for pos in reversed(range(1, i)):
            if x[pos - 1] > curr: 
                x[pos] = x[pos - 1]
            else:
                break
        x[pos] = curr

def bubble_sort(x):
    for i in reversed(range(0, len(x))):
        swapped = False
        for j in range (0, i):
            if x[j] > x[j + 1]:
                (x[j], x[j + 1]) = (x[j + 1], x[j])
                swapped = True
        if not swapped: break

def selection_sort(x):
    for i in reversed(range(0, len(x))):
        max = i
        for j in range(0, i):
            if x[j] > x[max]:
                max = j
        (x[max], x[i]) = (x[i], x[max])
 
def heap_sort(x):
    for i in range(len(x) >> 1, -1, -1):
        sift_down(x, i, len(x) - 1)

    for i in range(len(x) - 1, 0, -1):
        x[0], x[i] = x[i], x[0]
        sift_down(x, 0, i - 1)

def sift_down(x, parent, end):
    value = x[parent]
    max_child = parent * 2 + 1

    while max_child < end:
        if max_child < end and x[max_child] < x[max_child + 1]:
            max_child += 1
        if value >= x[max_child]: break         
        x[parent] = x[max_child]
        parent = max_child
        max_child = parent * 2 + 1

    x[parent] = value

def merge_sort(x):
    result = []
    if len(x) < 2:
        return x
    mid = len(x) >> 1
    left = merge_sort(x[: mid])
    right = merge_sort(x[mid:])
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
        
    result += left[i:]
    result += right[j:]
    return result

def quick_sort(x, begin = 0, end = None):
    if end is None:
        end = len(x) - 1

    def _quick_sort(x, begin, end):
        if begin >= end:
            return
        pivot = partition(x, begin, end)
        _quick_sort(x, begin, pivot - 1) 
        _quick_sort(x, pivot + 1, end)
    return _quick_sort(x, begin, end)

def partition(x, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if x[i] <= x[begin]:
            pivot += 1
            x[i], x[pivot] = x[pivot], x[i]
    x[pivot], x[begin] = x[begin], x[pivot]
    return pivot

# hacky quick sort implementation that is not in place
def quick_sort1(x):
    if len(x) == 0: return x
    else: 
        return ( quick_sort1([i for i in x[1:] if i < x[0]]) 
               + [x[0]] + quick_sort1([j for j in x[1:] if j >= x[0]]) )

# super short one liner for quicksort
qs = lambda x: x and ( qs([i for i in x[1:]if i <= x[0]]) 
                     + [x[0]] + qs([i for i in x[1:]if i>x[0]]) )

# main
if  __name__ == "__main__":
    d = [r.randint(0, 100) for i in range (10)]
    print(d)
    #tests
    #insertion_sort(d)
    #bubble_sort(d)
    #selection_sort(d)
    #heap_sort(d)
    #d = merge_sort(d)
    #d = quick_sort1(d)
    #d = qs(d)
    #quick_sort(d)
    
    print("sorted: ")
    print(d)
