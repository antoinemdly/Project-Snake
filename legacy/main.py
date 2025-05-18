# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
update_clock = pygame.time.Clock()
movement_clock = pygame.time.Clock()
running = True
dt = 0
direction_x = 1
direction_y = 0

x_pos = screen.get_width() / 2
y_pos = screen.get_height() / 2
square_size = 40

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, "green", (x_pos, y_pos, square_size, square_size))

    dt_movement = movement_clock.tick(60)

    # Move the player
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
    
    x_pos += square_size/dt_movement * direction_x * dt_movement
    y_pos += square_size/dt_movement * direction_y * dt_movement

    # Game update clock tick
    dt_update = update_clock.tick(60)

pygame.quit()