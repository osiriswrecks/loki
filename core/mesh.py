from .object3d import Object3D
from .vector import Vector

class MeshData:
    def __init__(self):
        self.vertices: list[Vector] = []

class Mesh(Object3D):
    def __init__(self):
        super().__init__()

        self.data = MeshData()