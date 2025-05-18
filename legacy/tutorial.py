import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
    def draw_snake(self):
        for block in self.body:
            snake_rect = pygame.Rect(block.x * cell_size,block.y * cell_size,cell_size,cell_size)
            pygame.draw.rect(screen,"green",snake_rect)
    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy

class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size,self.pos.y * cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,"red",fruit_rect)

    def eaten(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.eaten()
            self.snake.body.append(self.snake.body[-1] - self.snake.direction)

    def check_fail(self):
        if not 0 <= self.snake.body[0].x <= cell_number - 1 or not 0 <= self.snake.body[0].y <= cell_number - 1:
            self.game_over()

        for block in self.snake.body[1:]:
            if self.snake.body[0] == block:
                self.game_over()
        
    def game_over(self):
        pygame.quit()
        sys.exit()

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('')

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and main_game.snake.direction != Vector2(0,1):
                main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_s and main_game.snake.direction != Vector2(0,-1):
                main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_a and main_game.snake.direction != Vector2(1,0):
                main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_d and main_game.snake.direction != Vector2(-1,0):
                main_game.snake.direction = Vector2(1,0)

    screen.fill("gold")

    main_game.draw_elements()

    pygame.display.update()

    clock.tick(60)