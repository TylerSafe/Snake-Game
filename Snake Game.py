import pygame
from pygame.locals import *

class Snake:
    print('snake')


class Apple:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y

    def create_apple(self, board):
        # load apple image and place it on board
        apple = pygame.image.load('apple.png').convert()
        board.blit(apple, (self.start_x, self.start_y))

    def create_snake(self, board, x_coord, y_coord):
        snake = board.fill((110, 110, 5))
        board.blit(snake, (x_coord, y_coord))

class Game(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def create_board(self):
        pygame.init()
        self.board = pygame.display.set_mode((self.height, self.width))
        
        # change colour of the background
        self.board.fill((255, 255, 255))
        # render the apple and put it in its starting position
        self.get_apple()
        pygame.display.flip()

        # open the window until it is closed
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        y_coord -= 10
                        self.draw()
                    if event.key == K_DOWN:
                        y_coord += 10
                        draw()
                    if event.key == K_LEFT:
                        x_coord -= 10
                        draw()
                    if event.key == K_RIGHT:
                        x_coord += 10
                        draw()

                elif event.type == QUIT:
                    running = False

    # create apple and put it in given location    
    def get_apple(self):
        apple = Apple(100, 100)
        apple.create_apple(self.board)

    def draw(self):
        snake = Apple(120, 120)
        snake.create_snake(self.board)

if __name__ == "__main__":
    game = Game(500, 500)
    game.create_board()