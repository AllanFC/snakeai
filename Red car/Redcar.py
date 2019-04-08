import pyglet
from pyglet.gl import glClearColor
from pyglet.window import key, FPSDisplay
from GameObject import GameObject
#from maybe import GameObject


class GameWindow(pyglet.window.Window): #Basically Game Class where things are drawn and events are handled
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(360, 140)
        self.frame_rate = 1/60.0
        self.fps_display = FPSDisplay(self)
        glClearColor(0.3, 0.3, 0.3, 1.0)

        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.player_speed = 300


        self.player = GameObject(600, 400, 'red_car.png', scale=0.03) #This does what is below bascially
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

    def update(self, dt):
        self.update_player(dt)

    def update_player(self, dt):
        self.player.update(dt) #calls a function from GameObject to move the player sprite

        if self.right:
            self.player.rotate += 0.1
            self.player.velx += self.player_speed * dt

        if self.left:
            self.player.rotate -= 0.1
            self.player.velx -= self.player_speed * dt

        if self.up:
            self.player.vely += self.player_speed * dt

        if self.down:
            self.player.vely -= self.player_speed * dt

if __name__ == "__main__": #runs the game
    window = GameWindow(1200, 800, "Red Car", resizable=False) #Makes the window object
    pyglet.clock.schedule_interval(window.update, window.frame_rate) #Clock
    pyglet.app.run()








