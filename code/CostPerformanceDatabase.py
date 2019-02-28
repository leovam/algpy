class CostPerformanceDatabase:
    """Maintain a database of maximal (cost, performance) pairs. """

    def __init__(self):
        """create an empty database"""
        self._M = SortedTableMap()

    def best(self, c):
        """Return (cost, performance) pair with largest cost not exceeding c.

        Return None if there is no such pair.
        """
        return self._M.find_le(c)
    
    def add(self, c, p):
        """Add new entry with cost c and performance p"""
        #determin if (c, p) is dominated by an existing pair
        other = self._M.find_le(c)              #other is at least as cheap as c
        if other is not None and other[1] >= p: #if its performance is as good
            return                              # (c,p) is dominated, so igonre
        self._M[c] = p                          #else, add (c,p) to database
        #and now remove any pairs that are dominated by (c,p)
        other = self._M.find_le(c)              #other more expensive than c
        while other is not None and other[1] <= p:
            del self._M[other[0]]
            other = self._M.find_gt(c)
