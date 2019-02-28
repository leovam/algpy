class AdaptabbleHeapPriorityQueue(HeapPriorityQueue):

    class Locator(HeapPriorityQueue._item):
        __slots__ = 'index'

        def __init__(self, k, v, j):
            super