class _DoublyLinkedBase:
    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
            
        
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_bewteen(self, e, pre, suc):
        newest = self._Node(e, pre, suc)
        pre._next = newest
        suc._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        pre = node._prev
        suc = node._next
        pre._next = suc
        suc._pre = pre
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            print ("Dequeue is Empty")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            print ("Dequeue is Empty")
        return self._trailer._prev._element

    def insert_first(self, e):
        self._insert_bewteen(e, self._header, self._header._next)
    
    def insert_last(self, e):
        self._insert_bewteen(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            print ("Dequeue is Empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            print ("Dequeue is Empty")
        return self._delete_node(self._trailer._prev)
    

class PositionalList(_DoublyLinkedBase):
    class Position:
        def __init__(self,  container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self==other)

    def _validate(self, p):
        if not isinstance(p,self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node
    
    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    
if __name__ == '__main__':
    pass
