class SequenceIterator(object):

    def __init__(self, sequence):

        self._seq = sequence
        self._k = -1

    def __next__(self):

        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()
    
    ##python 2
    next = __next__
    
    def __iter__(self):

        return self

## test
L1 = [1, 2, 3, 4, 5, 6]
I1 = SequenceIterator(L1)

for i in range(len(L1)):
    print next(I1)
