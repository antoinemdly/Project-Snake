import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Multiple Timers Example')

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
direction_x = 1
direction_y = 0

x_pos = screen.get_width() / 2
y_pos = screen.get_height() / 2

# Set up the clock
main_clock = pygame.time.Clock()

# Define custom events
TIMER_EVENT_1 = pygame.USEREVENT + 1
TIMER_EVENT_2 = pygame.USEREVENT + 2

# Set the timers
pygame.time.set_timer(TIMER_EVENT_1, 1000)  # 1 second interval
pygame.time.set_timer(TIMER_EVENT_2, 500)   # 0.5 second interval

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == TIMER_EVENT_1:
            print("Timer 1 event")
        elif event.type == TIMER_EVENT_2:
            print("Timer 2 event")

    # Update display
    screen.fill("black")
    pygame.display.flip()

    pygame.draw.rect(screen, "green", (x_pos, y_pos, 400, 400))

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
    
    # x_pos += 40 * direction_x * TIMER_EVENT_1
    # y_pos += 40 * direction_y * TIMER_EVENT_1

    # Control the frame rate of the main loop
    main_clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
