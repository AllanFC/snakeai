import pyglet, math


class GameObject:
    def __init__(self, posx, posy, image=None, scale=None): #Player gameobject
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        self.rotate = 0
        if image is not None:
            image = pyglet.image.load('res/sprites/' + image)
            image.anchor_x = image.width // 2
            image.anchor_y = image.height // 2
            self.sprite = pyglet.sprite.Sprite(image, x=self.posx, y=self.posy)
            self.sprite.scale = scale
            self.width = self.sprite.width
            self.height = self.sprite.height

    def draw(self):
        self.sprite.draw()

    def update(self, dt):
        self.posx += dt * math.cos(math.radians(270 - self.rotate))
        self.posy += dt * math.sin(math.radians(270 - self.rotate))

        #self.posx += self.velx * dt
        #self.posy += self.vely * dt
        self.sprite.x = self.posx
        self.sprite.y = self.posy
        #self.sprite.rotation += self.rotate







