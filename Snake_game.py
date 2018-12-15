from pygame.locals import *
import pygame
import time
from random import *
from Colors import *


class Apple:
    x = 0
    y = 0

    step = 60

    def __init__(self, x, y):
        self.x = x * self.step
        self.y = y * self.step
        self.width = 20
        self.height = 20

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, (self.x, self.y, self.width, self.height))


class Player:
    x = [100]
    y = [100]
    width = 20
    height = 20
    speed = 20
    direction = 0
    length = 3

    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):
        self.length = length
        for i in range(0, 2000):
            self.x.append(-100)
            self.y.append(-100)

        self.x[1] = 1 * 20
        self.x[2] = 2 * 20

    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            for i in range(self.length - 1, 0, -1):
                print("self.x[" + str(i) + "] = self[" + str(i-1) + "]")
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            #Update the snake direction
            if self.direction == 0:
                self.x[0] = self.x[0] + self.speed
            if self.direction == 1:
                self.x[0] = self.x[0] - self.speed
            if self.direction == 2:
                self.y[0] = self.y[0] - self.speed
            if self.direction == 3:
                self.y[0] = self.y[0] + self.speed

            self.updateCount = 0

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def draw(self, surface, color):
        for i in range(0, self.length):
            pygame.draw.rect(surface, color, (self.x[i], self.y[i], self.width, self.height), 2)


class Game:

    def isCollision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 <= x2:
            if y1 >= y2 and y1 <= y2:
                return True
        return False

    def wallCollision(self, playerx, playery, width, height):
        if playerx <= -20 or playerx >= width:
            return True
        if playery <= -20 or playery >= height:
            return True
        return False


class Window:
    windowWidth = 800
    windowHeight = 600
    player = 0

    def __init__(self, gui=True):
        self.running = True
        self.display_surface = None
        self.game = Game()
        self.player = Player(3)
        self.apple = Apple(5, 5)
        load = open('Highscore.txt', 'r')
        self.highscore = load.readline()
        load.close()
        self.highscore = int(self.highscore)
        self.score = 0
        self.clock = pygame.time.Clock()
        self.pause = 0
        self.gui = gui

    def on_init(self):
        if self.gui:
            pygame.init()
            self.display_surface = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
            pygame.display.set_caption("Snake")
        self.running = True
        #self.image_surface = pygame.image.load("hadi.jpg").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self.running = False

    def text_to_screen(self, text, color, pos):
        font = pygame.font.SysFont('Arial', 30)
        screen_text = font.render(text, True, color)
        self.display_surface.blit(screen_text, pos)

    def highestscore(self):
        self.text_to_screen('Highscore: ' + str(self.highscore), white, (20, 20))
        self.text_to_screen('Score: ' + str(self.score), white, (self.windowWidth - 130, 20))
        if self.highscore < self.score:
            save = open('Highscore.txt', 'w')
            save.write(str(self.score))
            save.close()
            self.highscore += 1
        if self.highscore > self.score:
            pass

    def on_loop(self):
        self.player.update()
        self.highestscore()

        #eat apple
        for i in range(0, self.player.length):
            if self.game.isCollision(self.apple.x, self.apple.y, self.player.x[i], self.player.y[i]):
                self.apple.x = randint(0, 39) * 20
                self.apple.y = randint(0, 29) * 20
                self.player.length = self.player.length + 3
                self.score += 1

        # does snake collide with itself?
        for i in range(2, self.player.length):
            if self.game.isCollision(self.player.x[0], self.player.y[0], self.player.x[i], self.player.y[i]):
                print("Collision: ")
                print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
                exit(0)

        if self.game.wallCollision(self.player.x[0], self.player.y[0], self.windowWidth, self.windowHeight):
            print("Collision: ")
            print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
            print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
            exit(0)

        pass

    def on_render(self):
        if self.gui:
            self.display_surface.fill((0, 0, 0))
            self.highestscore()
            self.player.draw(self.display_surface, (255, 255, 255))
            self.apple.draw(self.display_surface, (255, 0, 0))
            pygame.display.update()

    def on_cleanup(self):
        self.player.update()
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        while(self.running):
            if self.gui:
                pygame.event.pump()
                keys = pygame.key.get_pressed()

                if keys[K_RIGHT] and self.player.direction != 1:
                    self.player.moveRight()

                if keys[K_LEFT] and self.player.direction != 0:
                    self.player.moveLeft()

                if keys[K_UP] and self.player.direction != 3:
                    self.player.moveUp()

                if keys[K_DOWN] and self.player.direction != 2:
                    self.player.moveDown()

                if keys[K_ESCAPE]:
                    self.running = False

                if keys[K_p]:
                    if self.pause == 0:
                        self.pause = 1000
                    elif self.pause > 0:
                        self.pause = 0

            self.on_loop()
            self.on_render()
            self.clock.tick(15)
            time.sleep(self.pause)
        self.on_cleanup()


if __name__ == "__main__":
    app = Window(gui=True)
    app.on_execute()


