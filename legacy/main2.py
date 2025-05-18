# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
clock2 = pygame.time.Clock()
running = True
dt = 0
dt2 = 0
square_size = 50

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

direction_x = 1
direction_y = 0

TIMER_EVENT_1 = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT_1, 1)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.rect(screen, "red", (player_pos.x, player_pos.y, square_size, square_size))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and direction_y != 1:
        direction_x = 0
        direction_y = -1
    if keys[pygame.K_s] and direction_y != -1:
        direction_x = 0
        direction_y = 1
    if keys[pygame.K_a] and direction_x != 1:
        direction_x = -1
        direction_y = 0
    if keys[pygame.K_d] and direction_x != -1:
        direction_x = 1
        direction_y = 0
    
    player_pos.x += square_size * direction_x * dt
    player_pos.y += square_size * direction_y * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    

    dt = clock.tick(60) / 1000

    dt2 = clock2.tick(1)

    # print(dt2)
    print(TIMER_EVENT_1)

pygame.quit()