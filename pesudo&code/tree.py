class Tree:
    '''
    Abstract base class representing a tree structure
    '''
    class Position:
        def element(self):
            raise NotImplementedError("Must be implemented by subclass")

        def __eq__(self, other):
            raise NotImplementedError("Must be implemented by subclass")

        def __ne__(self, other):
            return not(self==other)

    def root(self):
        raise NotImplementedError("Must be implemented by subclass")
    
    def parent(self, p):
        raise NotImplementedError("Must be implemented by subclass")

    def num_children(self, p):
        raise NotImplementedError("Must be implemented by subclass")
    
    def children(self,p):
        raise NotImplementedError("Must be implemented by subclass")

    def __len__(self):
        raise NotImplementedError("Must be implemented by subclass")

    def is_root(self, p):
        return self.root() == p
    
    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0
    
    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
    
    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))
    
    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)

class BinaryTree(Tree):
    def left(self,p):
        return NotImplementedError("Must be implemented by subclass")

    def right(self,p):
        return NotImplementedError("Must be implemented by subclass")

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self,p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = '_element', "_parent", "_left", "_right"
        def __init__(self, element, parent, left, right):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
    
    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._containter = container
            self._node = node
        

        def element(self):
            return self._node._element
        
        def __eq__(self, other):
            '''
            Return True if other is a Position representing the same location
            '''
            return type(other) is type(self) and other._node is self._node
    
    def _validate(self, p):
        '''
        validate the associated node
        '''
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._value

    def _make_positon(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def root(self):
        return self._make_positon(self._root)
    
    def parent(self,p):
        node = self._validate(p)
        return self._make_positon(node._parent)
    
    def left(self, p):
        node = self._validate(p)
        return self._make_positon(node._left)
    
    def right(self, p):
        node = self._validate(p)
        return self._make_positon(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count
    
    def _add_root(self, e):
        if self._root is not None:
            raise ValueError("Root Exists")
        self._size = 1
        self._root = self._Node(e)
        return self._make_positon(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Left child exists")
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_positon(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child exists")
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_positon(node._right)

    def _replace(self, p, e):
        """
        replace the element at postion p with e
        and return old element
        """
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        '''
        Delete the node at Position p, and replace it with its child, if any.

        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        '''
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children')
        child = node._left if node.left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element
    
    def _attach(self, p, t1, t2):
        '''
        Attach tree t1 and t2 as left and right substree of external p
        '''
        node = self._validate(p)
        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree type must be the same")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0        
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0
        

    

