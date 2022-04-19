import pygame
from pygame.locals import *
import time
import random

# declare constants
SIZE = 20
BACKGROUND = (255, 255, 255)
WIDTH = 800
HEIGHT = 600

# creates the apple for the snake to eat as well as controlling its movement
class Apple:
    # information required to create an apple
    def __init__(self, screen):
        self.screen = screen
        self.apple = pygame.image.load('apple.png').convert()
        self.x_coord = (random.randint(2, 38) * SIZE) + 10
        self.y_coord = (random.randint(2, 28) * SIZE) + 10

    # draw the apple on the screen
    def draw(self):
        self.screen.blit(self.apple, (self.x_coord, self.y_coord))
        pygame.display.flip()

    # define the next location the apple will move to
    def move(self):
        self.x_coord = (random.randint(2, 38) * SIZE) + 10
        self.y_coord = (random.randint(2, 28) * SIZE) + 10

# create the snake including movement and size
class Snake:
    # information required to create a snake
    def __init__(self, screen, length, x_start, y_start):
        self.length = length
        self.screen = screen
        self.snake = pygame.image.load('snake.png').convert()
        self.x_coord = [x_start] * length
        self.y_coord = [y_start] * length
        self.direction = 'up'

    # increases the length of the snake by 1
    def increase_length(self):
        self.length += 1
        self.x_coord.append(-1)
        self.y_coord.append(-1)
    
    # draw the snake on the screen
    def draw(self):
        self.screen.fill(BACKGROUND)
        pygame.draw.rect(self.screen, (189, 189, 189), pygame.Rect(0, 0, WIDTH, HEIGHT),  10)
        for i in range(self.length):
            self.screen.blit(self.snake, (self.x_coord[i], self.y_coord[i]))
        pygame.display.flip()

    # control what direction the snake goes based on input
    def up(self):
        self.direction = 'up'
    
    def down(self):
        self.direction = 'down'
    
    def left(self):
        self.direction = 'left'
    
    def right(self):
        self.direction = 'right'

    # move the entire length of the snake based on user input
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

        # redraw the snake after a move        
        self.draw()

# create the game board and run time interactions
class Game:
    def __init__(self):
        # initialise the board
        pygame.init()
        self.board = pygame.display.set_mode((WIDTH, HEIGHT))
        # change colour of the background
        self.board.fill(BACKGROUND)
        # initialise a snake and apple
        self.snake = Snake(self.board, 3, 150, 150)
        self.snake.draw()
        self.apple = Apple(self.board)
        self.apple.draw()

    # start the game and check if the snake collides with anything
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
    
    # determine whether a collision occurs between the snake and another object
    def collision(self, x1, y1, x2, y2):
        # if the snake hits itself the game is over
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True

        # if the snake hits the edge of the screen the game is over
        if self.snake.x_coord[0] > WIDTH - SIZE or self.snake.x_coord[0] < 0 or self.snake.y_coord[0] > HEIGHT - SIZE or self.snake.y_coord[0] < 0:
            return True
        
        return False

    # keep track of the amount of apples a user has eaten
    def score(self):
        font = pygame.font.SysFont('arial', 20)
        score = font.render('Score: ' + str(self.snake.length), True, (0, 0, 0))
        self.board.blit(score, (650, 15))

    # display screen when game is opened and when game is lost
    def game_over(self, reason):
        # create background with text to replace game board
        self.board.fill(BACKGROUND)
        font = pygame.font.SysFont('arial', 20)
        # if called because game lost print the score on screen
        if reason == 'game over':
            text1 = font.render('Game over! Your score is: ' + str(self.snake.length), True, (0, 0, 0))
            self.board.blit(text1, (220, 100))
        # give the user an option to play solo or vs another player
        text2 = font.render('To play single player press 1 or for 2 player (vs) press 2. Escape to exit', True, (0, 0, 0))
        self.board.blit(text2, (115, 150))
        pygame.display.flip()

    # reset the game to intial state once the user has lost
    def reset(self, option = 1):
        self.snake = Snake(self.board, 3, 150, 250)
        self.apple = Apple(self.board)
        if option == 2:
            self.snake2 = Snake(self.board, 3, (WIDTH - 250), 250)
    
    def run(self):
        # open the window until it is closed
        running = True
        pause = True
        self.game_over('start menu')
        while running:
            for event in pygame.event.get():
                # determine action when a key is pressed
                if event.type == KEYDOWN:                    
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_1:
                        pause = False
                    if event.key == K_2:
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
            # check if the game has been paused, if not continue
            try:
                if pause == False:
                    self.play()
            # pause the game when the user has lost and give them the option to try again
            except:
                self.game_over('game over')
                pause = True
                self.reset()
            
            # interval of time between each movement
            time.sleep(0.2)

if __name__ == "__main__":
    game = Game()
    game.run()



