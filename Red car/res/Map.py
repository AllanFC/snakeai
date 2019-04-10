import pyglet
from pyglet.gl import *

class Map:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.line = glVertex2f(x, y)