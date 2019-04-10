import pyglet, math, random


class GameObject:
    def __init__(self, posx, posy, image=None, scale=None): #Player gameobject
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        self.rotate = 0
        self.view = 270
        if image is not None:
            image = pyglet.image.load('res/sprites/' + image)
            image.anchor_x = image.width // 2
            image.anchor_y = image.height // 2
            self.sprite = pyglet.sprite.Sprite(image, x=self.posx, y=self.posy)
            self.sprite.scale = scale
            self.width = self.sprite.width
            self.height = self.sprite.height

class Sprite():
    def Load(self):
        self.view = 270
        self.xc = 912
        self.yc = 1410
        self.xf = 912.0
        self.yf = 1410.0
        self.speed = 0

    def Draw(self, x, y, screen):
        view = self.view + int(random.gauss(0, self.wobble))
        #        print 'wobble = ',self.wobble
        if view < 0:
            view = view + 360
        view = view % 360

    #        self.view = (self.view+2)%360
    def Update(self, dt):
        self.speed = self.speed

        theta = self.view / 57.296
        vx = self.speed * math.sin(theta)
        vy = -self.speed * math.cos(theta)
        self.xf = self.xf + vx * dt
        self.yf = self.yf + vy * dt
        self.xc = int(self.xf)
        self.yc = int(self.yf)