import pyglet, math


class Car:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.posx = self.size_x / 2
        self.posy = self.size_y / 2
        self.dir = 0
        self.turn = 0
        self.speed = 0.0
        self.maxspeed = 11.0
        self.minspeed = -1.5
        self.acceleration = 0.1
        self.deacceleration = 0.12
        self.softening = 0.04
        self.steering = 1.6
        self.image = pyglet.image.load('res/sprites/red_car.png')
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        self.sprite = pyglet.sprite.Sprite(self.image, x=self.posx, y=self.posy)
        self.sprite.scale = 0.03


        """
        pyglet.sprite.Sprite.__init__(self)
        self.image = load_image('car_player.png')
        self.rect = self.image.get_rect()
        self.image_orig = self.image
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        CENTER_X = int(pygame.display.Info().current_w / 2)
        CENTER_Y = int(pygame.display.Info().current_h / 2)
        self.x = CENTER_X
        self.y = CENTER_Y
        self.rect.topleft = self.x, self.y
        self.x, self.y = findspawn()
        self.dir = 0
        self.speed = 0.0
        self.maxspeed = 11.5
        self.minspeed = -1.85
        self.acceleration = 0.095
        self.deacceleration = 0.12
        self.softening = 0.04
        self.steering = 1.60
        self.tracks = False
        """

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
        self.dir = self.dir + self.steering
        if self.dir > 360:
            self.dir = 0
        #self.image, self.rect = rot_center(self.image_orig, self.rect, self.dir)

    # Steer.
    def steerright(self):
        self.dir = self.dir - self.steering
        if self.dir < 0:
            self.dir = 360
        #self.image, self.rect = rot_center(self.image_orig, self.rect, self.dir)

    def draw(self):
        self.sprite.rotation = self.dir
        self.sprite.draw()

    # fix this function
    def update(self):
        self.posx = self.posx - self.speed * math.cos(math.radians(270 - self.dir))
        self.posy = self.posy - self.speed * math.sin(math.radians(270 - self.dir))
        self.sprite.x = self.posx
        self.sprite.y = self.posy


