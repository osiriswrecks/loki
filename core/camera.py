from .object3d import Object3D

class Camera(Object3D):
    def __init__(self):
        super().__init__()

        self.near_clip = 0.1
        self.far_clip = 1000