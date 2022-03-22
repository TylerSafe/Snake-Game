import pygame
from pygame.locals import *
import time
import random

SIZE = 20
BACKGROUND = (255, 255, 255)

class Apple:
    def __init__(self, screen):
        self.screen = screen
        self.apple = pygame.image.load('apple.png').convert()
        self.x_coord = (random.randint(2, 38) * SIZE) + 10
        self.y_coord = (random.randint(2, 28) * SIZE) + 10

    def draw(self):
        self.screen.blit(self.apple, (self.x_coord, self.y_coord))
        pygame.display.flip()

    def move(self):
        self.x_coord = (random.randint(2, 38) * SIZE) + 10
        self.y_coord = (random.randint(2, 28) * SIZE) + 10

class Snake:
    def __init__(self, screen, length, x_start, y_start):
        self.length = length
        self.screen = screen
        self.snake = pygame.image.load('snake.png').convert()
        self.x_coord = [x_start] * length
        self.y_coord = [y_start] * length
        self.direction = 'up'

    def increase_length(self):
        self.length += 1
        self.x_coord.append(-1)
        self.y_coord.append(-1)
    
    def draw(self):
        self.screen.fill(BACKGROUND)
        for i in range(self.length):
            self.screen.blit(self.snake, (self.x_coord[i], self.y_coord[i]))
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
        for i in range(self.length - 1 , 0, -1):
            self.x_coord[i] = self.x_coord[i - 1]
            self.y_coord[i] = self.y_coord[i - 1]
        
        if self.direction == 'up':
            self.y_coord[0] -= SIZE
        if self.direction == 'down':
            self.y_coord[0] += SIZE
        if self.direction == 'left':
            self.x_coord[0] -= SIZE
        if self.direction == 'right':
            self.x_coord[0] += SIZE
        
        self.draw()

class Game:
    def __init__(self):
        # initialise the board
        pygame.init()
        self.board = pygame.display.set_mode((800, 600))
        # change colour of the background
        self.board.fill(BACKGROUND)
        
        self.snake = Snake(self.board, 3, 150, 150)
        self.snake.draw()
        self.apple = Apple(self.board)
        self.apple.draw()

    def play(self):
        self.snake.move()
        self.apple.draw()
        self.score()
        pygame.display.flip()

        # when snake collides with an apple move the apple and increase the length of the snake
        if self.collision(self.snake.x_coord[0], self.snake.y_coord[0], self.apple.x_coord, self.apple.y_coord):
            self.apple.move()
            self.snake.increase_length()

        # when a snake collides with itself lose the game
        for i in range(1, self.snake.length):
            if self.collision(self.snake.x_coord[0], self.snake.y_coord[0], self.snake.x_coord[i], self.snake.y_coord[i]):
                raise 'game over'
    
    def collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True

        return False

    def score(self):
        font = pygame.font.SysFont('arial', 20)
        score = font.render('Score: ' + str(self.snake.length), True, (0, 0, 0))
        self.board.blit(score, (650, 15))

    def game_over(self):
        self.board.fill(BACKGROUND)
        font = pygame.font.SysFont('arial', 20)
        text1 = font.render('Game over! Your score is: ' + str(self.snake.length), True, (0, 0, 0))
        self.board.blit(text1, (220, 100))
        text2 = font.render('To play single player press 1 or for 2 player (vs) press 2. Escape to exit', True, (0, 0, 0))
        self.board.blit(text2, (115, 150))
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.board, 3, 150, 150)
        self.apple = Apple(self.board)
    
    def run(self):
        # open the window until it is closed
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:                    
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_1:
                        pause = False

                    if pause == False:
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

            try:
                if pause == False:
                    self.play()
            except:
                self.game_over()
                pause = True
                self.reset()
            
            
            time.sleep(0.2)

if __name__ == "__main__":
    game = Game()
    game.run()



