class LinkedQueue:
    class _Node:
        __slots__ = '_element', "_next"
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size   

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            print ("Queue is Empty")
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            print ('Queue is Empty')
        
        ans = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return ans

    def enqueue(self,e):
        new = self._Node(e, None)
        if self.is_empty():
            self._head = new
        else:
            self._tail._next = new
        self._tail = new
        self._size += 1
        

if __name__ == '__main__':
    Queue = LinkedQueue()
    Queue.enqueue(2)
    Queue.enqueue(3)
    print (Queue.first())
    print (Queue._size)