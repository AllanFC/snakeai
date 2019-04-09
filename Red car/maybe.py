import pyglet
import math


class GameObject:
    def __init__(self, posx, posy, image=None, scale=None): #Player gameobject
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        self.turn = 180.0
        self.steering = 1.60
        self.speed = 0.0
        self.maxspeed = 11.5
        self.minspeed = -1.85
        self.acceleration = 0.095
        self.deacceleration = 0.12
        self.softening = 0.04

        if image is not None:
            image = pyglet.image.load('res/sprites/' + image)
            image.anchor_x = image.width // 2
            image.anchor_y = image.height // 2
            self.sprite = pyglet.sprite.Sprite(image, x=self.posx, y=self.posy)
            self.sprite.scale = scale
            self.width = self.sprite.width
            self.height = self.sprite.height
            self.sprite.rotation = self.turn

    def draw(self):
        self.sprite.draw()

    def accelerate(self):
        if self.speed < self.maxspeed:
            self.speed = self.speed + self.acceleration

    def soften(self):
        if self.speed > 0:
            self.speed -= self.softening
        if self.speed < 0:
            self.speed += self.softening

    def deaccelerate(self):
        if self.speed > self.minspeed:
            self.speed = self.speed - self.deacceleration

#Steer.
    def steerleft(self):
        self.turn = self.turn+self.steering
        if self.turn > 360:
            self.turn = 0
        self.sprite.rotation(self.turn)

#Steer.
    def steerright(self):
        self.turn = self.turn-self.steering
        if self.turn < 0:
            self.turn = 360
        self.sprite.rotation(self.turn)

#fix this function
    def update(self):
        self.posx = self.posx + self.speed * math.cos(math.radians(270-self.turn))
        self.posy = self.posy + self.speed * math.sin(math.radians(270-self.turn))






