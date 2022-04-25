import numpy

class Buffer:
    def __init__(self, data: list[float]):
        self.data = numpy.array(data, dtype=numpy.float32)