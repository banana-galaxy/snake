import pygame, gamefunctions, random
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
screen_width = 500
screen_height = 500
size = (screen_width, screen_height)
block_size = 10
done = False
grid = gamefunctions.initiate_grid(screen_width, block_size)
grid_size = len(grid)
vel_x = 0
vel_y = 0
add_length = 0

snake_body = [[]]
snake_body[0].append(random.randrange(len(grid)))
snake_body[0].append(random.randrange(len(grid)))
print(snake_body[0][0], snake_body[0][1])

screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vel_y = 0
                if vel_x < 1:
                    vel_x = 1
            if event.key == pygame.K_LEFT:
                vel_y = 0
                if vel_x > -1:
                    vel_x = -1
            if event.key == pygame.K_UP:
                vel_x = 0
                if vel_y > -1:
                    vel_y = -1
            if event.key == pygame.K_DOWN:
                vel_x = 0
                if vel_y < 1:
                    vel_y = 1
            if event.key == pygame.K_SPACE:
                add_length = 1

    print(vel_x, vel_y)

    # --- Game logic
    snake_body.append([])
    snake_body[len(snake_body) - 1].append(snake_body[len(snake_body) - 2][0] + vel_x)
    snake_body[len(snake_body) - 1].append(snake_body[len(snake_body) - 2][1] + vel_y)
    if add_length:
        add_length = 0
        pass
    else:
        snake_body.pop(0)

    '''grid[snake_x][snake_y] = 0
    snake_x += vel_x
    snake_y += vel_y
    grid[snake_x][snake_y] = 1'''

    # --- Screen-clearing code
    screen.fill(WHITE)

    # --- Drawing code

    # - Drawing the food

    # - Drawing the snake
    for cell in snake_body:
        pygame.draw.rect(screen, BLACK, [cell[0]*block_size, cell[1]*block_size, 10, 10], 0)

    # - Grid should always be on top of everything, so this is the last thing to be drawn
    gamefunctions.draw_grid(pygame, screen, [screen_width, screen_height], grid_size, block_size, WHITE)

    # --- Update the screen
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)

# Close the window and quit.
pygame.quit()