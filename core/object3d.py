from .vector import Vector

class Object3D:
    def __init__(self):
        self.location = Vector(0, 0, 0)
        self.rotation = Vector(0, 0, 0)
        self.scale = Vector(1, 1, 1)