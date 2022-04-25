import numpy

class Vector:
    def __init__(self, x, y, z):
        self._data = numpy.array(
            [x, y, z],
            dtype=numpy.float32
            )
    
    def __str__(self):
        return "{}, {}, {}".format(self.x, self.y, self.z)

    @property
    def x(self):
        return self._data[0]

    @property
    def y(self):
        return self._data[1]

    @property
    def z(self):
        return self._data[2]
    
    def copy(self):
        return Vector(self.x, self.y, self.z)

    def magnitude(self):
        return numpy.linalg.norm(self._data)

    '''
    This function replaces existing data in the Vector object. To return
    a copy, use the `normalized()` method below.
    '''
    def normalize(self):
        self._data = self.normalized()._data

    '''
    This function returns a normalized copy of the Vector object data. To
    fully replace existing data within the Vector object, use the `normalize()`
    method above.
    '''
    def normalized(self):
        norm = self.magnitude()
        
        if norm == 0:
            return self.copy()
        
        nd = self._data / norm # normalized data
        return Vector(nd[0], nd[1], nd[2])
        
