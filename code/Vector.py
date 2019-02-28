class Vector(object):

    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        else:
            self._coords = d

    def __eq__(self, other):
        return self._coords == other._coords
    
    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must agree...')
        
        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimensions must agree...')
        
        result = Vector(len(self))

        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Dimension must agree...')
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] - other[i]
        return result

    def __ne__(self, other):
        return not self == other

    def __neg__(self):
        for i in range(len(self)):
            self._coords[i] = -self._coords[i]
        return '<' + str(self._coords)[1:-1] + '>'

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

    def __mul__(self, val):
        if isinstance(val, int) or isinstance(val, float):
            print 'vector * value'
            #print type(val)
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self._coords[i] * val
            return result

        else:
            print "Vector * Vector"
            #print type(val)
            if len(self) != len(val):
                raise ValueError('Dimension must agree...')
            else:
                result = Vector(len(self))
                for i in range(len(self)):
                    result[i] = self._coords[i] * val._coords[i]
                return sum(result)

    def __rmul__(self, val):
        #print type(val)
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self._coords[i] * val
        return result

if __name__ == "__main__":
    # v = Vector(5)
    # v[1] = 23
    # v[-1] = 45
    # print v * 3
    # print 3 * v
    # print -v
    # u =  [5, 3, 10, -2, 1] + v
    # print u * v
    # total = 0
    # for entry in v:
    #     total += entry
    # print total
    print Vector([4, 7, 5])
