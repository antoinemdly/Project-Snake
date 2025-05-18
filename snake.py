import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
		
        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
        # self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')

    def draw_snake(self):
        for index,block in enumerate(self.body):
            snake_rect = pygame.Rect(block.x * cell_size,block.y * cell_size,cell_size,cell_size)
            if block == self.body[0]:
                if self.direction == Vector2(0,1):
                    screen.blit(self.head_down,snake_rect)
                if self.direction == Vector2(0,-1):
                    screen.blit(self.head_up,snake_rect)
                if self.direction == Vector2(1,0):
                    screen.blit(self.head_right,snake_rect)
                if self.direction == Vector2(-1,0):
                    screen.blit(self.head_left,snake_rect)
            elif block == self.body[-1]:
                if self.body[-2].y < self.body[-1].y:
                    screen.blit(self.tail_down,snake_rect)
                if self.body[-2].y > self.body[-1].y:
                    screen.blit(self.tail_up,snake_rect)
                if self.body[-2].x < self.body[-1].x:
                    screen.blit(self.tail_right,snake_rect)
                if self.body[-2].x > self.body[-1].x:
                    screen.blit(self.tail_left,snake_rect)
            #elif block == self.body[1]:


            else:
                if self.body[index - 1].y < self.body[index].y < self.body[index + 1].y or self.body[index - 1].y > self.body[index].y > self.body[index + 1].y:
                    screen.blit(self.body_vertical,snake_rect)
                if self.body[index - 1].x < self.body[index].x < self.body[index + 1].x or self.body[index - 1].x > self.body[index].x > self.body[index + 1].x:
                    screen.blit(self.body_horizontal,snake_rect)
                
                if self.body[index - 1].y < self.body[index].y and self.body[index].x < self.body[index + 1].x:
                    screen.blit(self.body_tr,snake_rect)
                if self.body[index - 1].x > self.body[index].x and self.body[index].y > self.body[index + 1].y:
                    screen.blit(self.body_tr,snake_rect)

                if self.body[index - 1].y < self.body[index].y and self.body[index].x > self.body[index + 1].x:
                    screen.blit(self.body_tl,snake_rect)
                if self.body[index - 1].x < self.body[index].x and self.body[index].y > self.body[index + 1].y:
                    screen.blit(self.body_tl,snake_rect)

                if self.body[index - 1].y > self.body[index].y and self.body[index].x > self.body[index + 1].x:
                    screen.blit(self.body_bl,snake_rect)
                if self.body[index - 1].x < self.body[index].x and self.body[index].y < self.body[index + 1].y:
                    screen.blit(self.body_bl,snake_rect)

                if self.body[index - 1].y > self.body[index].y and self.body[index].x < self.body[index + 1].x:
                    screen.blit(self.body_br,snake_rect)
                if self.body[index - 1].x > self.body[index].x and self.body[index].y < self.body[index + 1].y:
                    screen.blit(self.body_br,snake_rect)
            # pygame.draw.rect(screen,"green",snake_rect)
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
        screen.blit(apple,fruit_rect)
        #pygame.draw.rect(screen,"red",fruit_rect)

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
apple = pygame.image.load('Graphics/apple.png').convert_alpha()

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