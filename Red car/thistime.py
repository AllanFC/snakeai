import pyglet, math
from pyglet.gl import *


class Map:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.line = pyglet.graphics.vertex_list(2, ('v2i', self.x), ('c3B', self.y))

        # self.x = x
        # self.y = y
        # self.lines = []
        # self.batch = pyglet.graphics.Batch()


    # def map(self):
    #     for x in self.coordinate_x:
    #         for y in self.coordinate_y:
    #             self.batch = self.batch.add(glVertex2f(x, y))



class Car:
    def __init__(self, screen_w, screen_h):
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.posx = self.screen_w / 2
        self.posy = self.screen_h / 2
        self.dir = 0
        self.turn = 0
        self.speed = 0.0
        self.maxspeed = 3
        self.minspeed = -2
        self.acceleration = 0.1
        self.deacceleration = 0.1
        self.softening = 0.03
        self.steering = 1.6
        self.image = pyglet.image.load('res/sprites/red_car.png')
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        self.sprite = pyglet.sprite.Sprite(self.image, x=self.posx, y=self.posy)
        self.sprite.scale = 0.02

    def lines(self):
        glBegin(GL_LINES)

        # front
        glVertex2f((self.posx - self.sprite.width / 2), (self.posy + self.sprite.height / 2))
        glVertex2f((self.posx + self.sprite.width / 2), (self.posy + self.sprite.height / 2))
        # right
        glVertex2f((self.posx + self.sprite.width / 2), (self.posy + self.sprite.height / 2))
        glVertex2f((self.posx + self.sprite.width / 2), (self.posy - self.sprite.height / 2))
        # left
        glVertex2f((self.posx - self.sprite.width / 2), (self.posy + self.sprite.height / 2))
        glVertex2f((self.posx - self.sprite.width / 2), (self.posy - self.sprite.height / 2))
        # back
        glVertex2f((self.posx - self.sprite.width / 2), (self.posy - self.sprite.height / 2))
        glVertex2f((self.posx + self.sprite.width / 2), (self.posy - self.sprite.height / 2))

        glEnd()


    def distance(self):
        pass


    # Reset the car.
    def reset(self):
        self.posx = pyglet.window.Window.width / 2
        self.posy = pyglet.window.Window.height / 2
        self.dir = 0
        self.speed = 0.0


    def soften(self):
        if self.speed > 0:
            self.speed -= self.softening
        if self.speed < 0:
            self.speed += self.softening
        if 0.05 > self.speed > -0.5:
            self.speed = round(self.speed)

    # Accelerate the vehicle
    def accelerate(self):
        if self.speed < self.maxspeed:
            self.speed += self.acceleration


    # Deaccelerate.
    def deaccelerate(self):
        if self.speed > self.minspeed:
            self.speed -= self.deacceleration


    # Steer.
    def steerleft(self):
        if self.speed > 0.9 or self.speed < -0.9:
            self.dir = self.dir + self.steering
            if self.dir > 360:
                self.dir = 0

    # Steer.
    def steerright(self):
        if self.speed > 0.9 or self.speed < -0.9:
            self.dir = self.dir - self.steering
            if self.dir < 0:
                self.dir = 360

    def draw(self):
        self.sprite.rotation = self.dir
        self.sprite.draw()
        self.lines()

    # fix this function
    def update(self):
        self.posx = self.posx - self.speed * math.cos(math.radians(270 - self.dir))
        self.posy = self.posy - self.speed * math.sin(math.radians(270 - self.dir))
        self.sprite.x = self.posx
        self.sprite.y = self.posy
        self.lines()
        #self.distance()


