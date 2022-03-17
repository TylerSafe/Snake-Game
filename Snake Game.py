import pygame
from pygame.locals import *

class Snake:
    print('snake')


class Apple:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y

    def create_apple(self, board):
        apple = pygame.image.load('apple.png').convert()
        board.blit(apple, (self.start_x, self.start_y))

class Game(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def create_board(self):
        pygame.init()
        self.board = pygame.display.set_mode((self.height, self.width))
        
        # change colour of the background
        self.board.fill((225, 242, 241))
        self.get_apple()
        pygame.display.flip()

        # open the window until it is closed
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    pass
                elif event.type == QUIT:
                    running = False
        


    def get_apple(self):
        apple = Apple(100, 100)
        apple.create_apple(self.board)

if __name__ == "__main__":
    game = Game(500, 500)
    game.create_board()