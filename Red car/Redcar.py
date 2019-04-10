import pyglet, thistime
import cv2
import numpy as np
from decimal import Decimal, getcontext
from pyglet.gl import *
from pyglet.window import key, FPSDisplay


class GameWindow(pyglet.window.Window): #Game Class where things are drawn and events are handled
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = 1200
        self.height = 800
        self.set_location(180, 30)
        self.frame_rate = 1/60.0
        self.fps_display = FPSDisplay(self)
        self.font_size = int(self.fps_display.label.font_size)
        self.font_color = self.fps_display.label.color
        glClearColor(0.3, 0.3, 0.3, 1.0)

        self.coordinate_x = [69, 342, 665, 772, 587, 814, 923, 1135, 1176, 1138, 781, 835, 589, 58]
        self.coordinate_y = [533, 691, 707, 610, 424, 457, 680, 660, 525, 112, 28, 178, 86, 87]

        self.right = False
        self.left = False
        self.up = False
        self.down = False


        #self.player = GameObject(600, 400, 'red_car.png', scale=0.03) #This does what is below bascially
        self.player = thistime.Car(self.width, self.height)
        self.text = pyglet.text.Label(text=str(self.player.speed), x=int(self.fps_display.label.x), y=self.height-int(self.fps_display.label.y)-self.font_size, font_size=self.font_size, color=self.font_color)

        for x in range(0, len(self.coordinate_x)):
            for y in range(0, len(self.coordinate_y)):
                self.map = thistime.Map(self.coordinate_x[x], self.coordinate_y[y])

        #image = pyglet.image.load('res/sprites/red_car.png')
        #image.anchor_x = image.width // 2
        #image.anchor_y = image.height // 2
        #self.player = pyglet.sprite.Sprite(image, x=600, y=400)
        #self.player.scale = 0.03

    def on_key_press(self, symbol, modifiers): #Key events
        if symbol == key.RIGHT:
            self.right = True
        if symbol == key.LEFT:
            self.left = True
        if symbol == key.UP:
            self.up = True
        if symbol == key.DOWN:
            self.down = True

    def on_key_release(self, symbol, modifiers): #Key events
        if symbol == key.RIGHT:
            self.right = False
        if symbol == key.LEFT:
            self.left = False
        if symbol == key.UP:
            self.up = False
        if symbol == key.DOWN:
            self.down = False

        if symbol == key.ESCAPE:
            pyglet.app.exit()


    def on_draw(self): #draws player to the screen
        self.clear()
        self.player.draw() #calling function from GameObject to draw on screen
        self.fps_display.draw()
        self.text.draw()
        self.map.line.draw(GL_LINES)

    def update(self, dt):
        self.update_player(dt)

        #Display speed
        getcontext().prec = 3
        speed_display = Decimal(self.player.speed)/Decimal(1)
        self.text.text = str(speed_display)


    def update_player(self, dt):
        self.player.update() #calls a function from GameObject to move the player sprite

        if self.right:
            self.player.steerleft()

        if self.left:
            self.player.steerright()

        if self.up:
            self.player.accelerate()

        if self.down:
            self.player.deaccelerate()

        elif not self.up and not self.down:
            self.player.soften()

if __name__ == "__main__": #runs the game
    window = GameWindow(1200, 800, "Red Car", resizable=False) #Makes the window object
    pyglet.clock.schedule_interval(window.update, window.frame_rate) #Clock
    pyglet.app.run()








