class Snake:
    print('snake')


class Apple:
    print('apple')


class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def board(self):
        print('┌' + '─' * (self.width - 2) + '┐')
        print(('│' + ' ' * (self.width - 2) + '│' + '\n') * (self.height - 2) + ('└' + '─' * (self.width - 2) + '┘'))

    def create_board(self):
        self.board()



if __name__ == "__main__":
    game = Game(20, 40)
    game.create_board()