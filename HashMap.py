# (c) 2017 Tingda Wang
# HashMap implementation, equivalent to dictionaries in Python

class HashMap():
    def __init__(self, size = 10):
        self.size = size
        self.list = [[] for _ in range(self.size)]

    def _hashfunc(self, key):
        return int(key) % self.size

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

    def inverse(self):
        ''' returns an inverse mapping '''
        inverse = HashMap(self.size)

        for key, value in self.items:
            inverse[value] = key

        return inverse
        
    def __contains__(self, key):
        hashkey = self._hashfunc(key)
        for item in self.list[hashkey]:
            if item[0] == key:
                return True
        return False

    def empty(self):
        ''' checks if hashmap is empty '''
        for bucket in self.list:
            if bucket:
                return False
        return True

    def __bool__(self):
        return self.empty()
    
    @property
    def items(self):
        for items in self.list:
            for pair in items:
                yield pair[0], pair[1]
                
    @property
    def keys(self):
        for items in self.list:
            for pair in items:
                yield pair[0]

    @property
    def values(self):
        for items in self.list:
            for pair in items:
                yield pair[1]

    def __repr__(self):
        str = ', '.join(['Key %s: Value %s' %(item[0], item[1]) for buckets in self.list for item in buckets])
        return '{ ' + str + ' }'

if __name__ == '__main__':

    h = HashMap(5)
    h[5] = 'asdf'
    h[10] = 'asa'
    print(h[5])
    print(h)
    #print(h.inverse())
