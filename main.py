import sys, random
import pygame


class Game:

    def __init__(self):

        self.screen = pygame.display.set_mode((800, 600))

        pygame.display.set_caption('Sn4k3')
        self.running_game = True

        self.snake_x_pos = 300
        self.snake_y_pos = 300
        self.snake_x_dir = 0
        self.snake_y_dir = 0
        self.snake = 10
        self.snake_pos = []

        self.apple_x_pos = random.randrange(110, 690, 10)
        self.apple_y_pos = random.randrange(110, 590, 10)
        self.apple = 10
        self.clock = pygame.time.Clock()

        self.snake_size = 1

        self.main_screen = True

        self.snake_head_img = pygame.image.load('snake_head.png')

        self.image = pygame.image.load('snake-game.jpg')
        self.title_img = pygame.transform.scale(self.image, (200, 100))

        self.score = 0

    def main_function(self):

        while self.main_screen:

            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    sys.exit()

                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_RETURN:
                        self.main_screen = False

                self.screen.fill((0, 0, 0))

                self.screen.blit(self.title_img, (300, 50, 100, 50))
                self.create_message('moyenne', 'Appuyer sur Enter pour commencer', (200, 450, 200, 5),
                                    (255, 255, 255))

                pygame.display.flip()

        while self.running_game:

            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT:
                    sys.exit()

                if evenement.type == pygame.KEYDOWN:

                    if evenement.key == pygame.K_RIGHT:
                        self.snake_x_dir = 10
                        self.snake_y_dir = 0

                    if evenement.key == pygame.K_LEFT:
                        self.snake_x_dir = -10
                        self.snake_y_dir = 0

                    if evenement.key == pygame.K_DOWN:
                        self.snake_y_dir = 10
                        self.snake_x_dir = 0

                    if evenement.key == pygame.K_UP:
                        self.snake_y_dir = -10
                        self.snake_x_dir = 0

            if self.snake_x_pos <= 100 or self.snake_x_pos >= 700 \
                    or self.snake_y_pos <= 100 or self.snake_y_pos >= 600:
                sys.exit()

            self.snake_move()

            if self.apple_y_pos == self.snake_y_pos and self.snake_x_pos == self.apple_x_pos:
                self.apple_x_pos = random.randrange(110, 690, 10)
                self.apple_y_pos = random.randrange(110, 590, 10)

                self.snake_size += 1
                self.score += 1

            snake_head = []
            snake_head.append(self.snake_x_pos)
            snake_head.append(self.snake_y_pos)

            self.snake_pos.append(snake_head)

            if len(self.snake_pos) > self.snake_size:
                self.snake_pos.pop(0)

            self.display_elements()
            self.bite_himself(snake_head)

            self.create_message('grande', 'Sn4k3', (320, 10, 100, 50), (255, 255, 255), )
            self.create_message('grande', '{}'.format(str(self.score)), (375, 50, 50, 50), (255, 255, 255), )

            self.screen_limit()
            self.clock.tick(30)

            pygame.display.flip()

    def screen_limit(self):

        pygame.draw.rect(self.screen, (255, 255, 255), (100, 100, 600, 500), 3)

    def snake_move(self):

        self.snake_x_pos += self.snake_x_dir
        self.snake_y_pos += self.snake_y_dir

    def display_elements(self):

        self.screen.fill((0, 0, 0))

        self.screen.blit(self.snake_head_img, (self.snake_x_pos, self.snake_y_pos, self.snake, self.snake))

        pygame.draw.rect(self.screen, (255, 0, 0), (self.apple_x_pos, self.apple_y_pos, self.apple, self.apple))

        self.display_snake()

    def display_snake(self):

        for snake_part in self.snake_pos[:-1]:
            pygame.draw.rect(self.screen, (0, 255, 0), (snake_part[0], snake_part[1], self.snake, self.snake))

    def bite_himself(self, snake_head):

        for snake_part in self.snake_pos[:-1]:
            if snake_part == snake_head:
                sys.exit()

    def create_message(self, font, message, message_rectangle, couleur):

        if font == 'petite':
            font = pygame.font.SysFont('Lato', 20, False)

        elif font == 'moyenne':
            font = pygame.font.SysFont('Lato', 30, False)

        elif font == 'grande':
            font = pygame.font.SysFont('Lato', 40, True)

        message = font.render(message, True, couleur)

        self.screen.blit(message, message_rectangle)


if __name__ == '__main__':
    pygame.init()
    Game().main_function()
    pygame.quit()
