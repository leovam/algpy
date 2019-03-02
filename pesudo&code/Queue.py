class Queue:
    Max_Capacity = 10

    def __init__(self):
        self._data = [None] * Queue.Max_Capacity
        self._size = 0
        self._read = 0

    def __len__(self):
        return len(self._data)  

    def is_empty(self):
        return self._size == 0

    def reader(self):
        if self.is_empty():
            print ('Queue is empty')
        return self._data[self._read]

    def dequeue(self):
        if self.is_empty:
            print ('Queue is empty')
        reader = self._data[self._read]
        self._data[self._read] = None
        self._read = (self._read + 1) % len(self._data)
        self._size -= 1
        return reader
    
    def enqueue(self, i):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        write = (self._read + self._size) % len(self._data)
        self._data[write] = i
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._read
        for k in range (self._size):
            self._data[k] = old[walk]
            walk = (1+ walk) % len(old)
        self._read = 0

        
    