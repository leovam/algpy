from .DoubleLinkedList import PositionalList

class PriorityQueueBase:
    class _Item:
        __slots__ = '_key', '_value'
    
        def __init__(self, k, v):
            self._key = k
            self._v = v

        def __It__(self, other):
            return self._key < other._key

    def is_empty(self):
        return len(self) == 0

class UnsortedPriorityQueue(PriorityQueueBase):
    def _find_min(self):
        if self.is_empty():
            print ('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.add_first(self._Item(key, value))

    def min(self):
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)
    
    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)