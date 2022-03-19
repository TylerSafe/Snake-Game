import pygame
from pygame.locals import *
import time

class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.snake = pygame.image.load('snake.png').convert()
        self.x_coord = 150
        self.y_coord = 150
        self.direction = 'up'

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.snake, (self.x_coord, self.y_coord))
        pygame.display.flip()

    def up(self):
        self.direction = 'up'
    
    def down(self):
        self.direction = 'down'
    
    def left(self):
        self.direction = 'left'
    
    def right(self):
        self.direction = 'right'

    def move(self):
        if self.direction == 'up':
            self.y_coord -= 10
        if self.direction == 'down':
            self.y_coord += 10
        if self.direction == 'left':
            self.x_coord -= 10
        if self.direction == 'right':
            self.x_coord += 10
        
        self.draw()


class Game:
    def __init__(self):
        # initialise the board
        pygame.init()
        self.board = pygame.display.set_mode((500, 500))
        # change colour of the background
        self.board.fill((255, 255, 255))
        self.snake = Snake(self.board)
        self.snake.draw()

    def run(self):
        # open the window until it is closed
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.up()
                    if event.key == K_DOWN:
                        self.snake.down()
                    if event.key == K_LEFT:
                        self.snake.left()
                    if event.key == K_RIGHT:
                        self.snake.right()

                elif event.type == QUIT:
                    running = False

            self.snake.move()
            time.sleep(0.25)

if __name__ == "__main__":
    game = Game()
    game.run()


    #apple = pygame.image.load('apple.png').convert()


