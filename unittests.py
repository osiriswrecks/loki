import random
from core import *

def random_numbers(length):
    result = []

    for i in range(0, length):
        result.append(random.uniform(0, 10))
    
    return result

def test_vector():
    vec = Vector(*random_numbers(3))

    print("Vector Test")
    print("------------")
    print("x: {}".format(vec.x))
    print("y: {}".format(vec.y))
    print("z: {}\n".format(vec.z))

    length = vec.magnitude()
    print("Magnitude: {}\n".format(length))

    # This will create a normalized copy
    normalized = vec.normalized()
    print("Normalized copy: {}".format(normalized))
    print("Original: {}\n".format(vec))

    # This will change the original
    vec.normalize()
    print("Normalized original: {}\n".format(vec))

def test_buffer():
    pixels = [0] * 2 * 4 # 2 RGBA pixels
    buffer = Buffer(pixels)

    print("Buffer")
    print("------")
    print(buffer.data)
    print()

def test_mesh():
    mesh = Mesh()

    print("Mesh")
    print("----")
    print("Location: {}".format(mesh.location))
    print("Rotation: {}".format(mesh.rotation))
    print("Scale: {}".format(mesh.scale))
    print("Vertices: {}".format(mesh.data.vertices))

if __name__ == "__main__":
    print()
    
    test_vector()
    test_buffer()
    test_mesh()

    print()