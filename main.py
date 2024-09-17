import pygame, gamefunctions, random
pygame.init()

BLACK = (0, 0, 0)
WHITE = (244,244,244)
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
vel_y = 1
direction_change = False
add_length = 0
add_count = 0
gameover_pic = pygame.image.load("g_o_t.png")
#icon = pygame.image.load("icon_snake.png")
#pause_pic = pygame.image.load("pause.png")
gameover = False
restart = False
pause = False



snake_body = [[]]
snake_body[0].append(int(len(grid)/2))
snake_body[0].append(int(len(grid)/2))

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
#pygame.display.set_icon(icon)
clock = pygame.time.Clock()

foods = []
x, y = random.randrange(len(grid)), random.randrange(len(grid))
foods.append(gamefunctions.Food(pygame, screen, block_size, GREEN, x, y))


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if pause:
                    pause = False
                else:
                    pause = True
            if event.key == pygame.K_SPACE:
                if gameover:
                    restart = True
            if not direction_change and not gameover and not pause:
                if event.key == pygame.K_RIGHT:
                    if vel_y != 0:
                        vel_y = 0
                        vel_x = 1
                        direction_change = True
                if event.key == pygame.K_LEFT:
                    if vel_y != 0:
                        vel_y = 0
                        vel_x = -1
                        direction_change = True
                if event.key == pygame.K_UP:
                    if vel_x != 0:
                        vel_x = 0
                        vel_y = -1
                        direction_change = True
                if event.key == pygame.K_DOWN:
                    if vel_x != 0:
                        vel_x = 0
                        vel_y = 1
                        direction_change = True

    if restart and gameover:
        restart = False
        gameover = False
        snake_body = [[]]
        snake_body[0].append(int(len(grid) / 2))
        snake_body[0].append(int(len(grid) / 2))
        vel_x = 0
        vel_y = 1


    gameover = gamefunctions.collide(grid_size, snake_body, (vel_x, vel_y))
    if not gameover and not pause:
        # --- Game logic

        #
        snake_body.append([])
        snake_body[len(snake_body) - 1].append(snake_body[len(snake_body) - 2][0] + vel_x)
        snake_body[len(snake_body) - 1].append(snake_body[len(snake_body) - 2][1] + vel_y)
        for food in foods:
            if snake_body[len(snake_body)-1][0] == food.pos()[0]:
                if snake_body[len(snake_body)-1][1] == food.pos()[1]:
                    x, y = random.randrange(len(grid)), random.randrange(len(grid))
                    foods.append(gamefunctions.Food(pygame, screen, block_size, GREEN, x, y))
                    add_count = food.eat()
                    foods.remove(food)
                    add_length = 1

        # managing snake growth/shrinking
        if add_length:
            if add_count > 0:
                add_count -= 1
            else:
                add_length = 0
            pass
        else:
            # just move the snake if it doesn't need growth or shrinking
            snake_body.pop(0)

        # --- Screen-clearing code
        screen.fill(WHITE)


        # --- Drawing code

        # - Drawing the snake
        for cell in snake_body:
            pygame.draw.rect(screen, BLACK, [cell[0]*block_size, cell[1]*block_size, 10, 10], 0)

        # - Drawing the grid
        gamefunctions.draw_grid(pygame, screen, [screen_width, screen_height], grid_size, block_size, WHITE)

        # - Drawing the food
        for food in foods:
            food.draw()

        direction_change = False
        # --- Update the screen
        pygame.display.flip()
    elif pause and not gameover:
        try:
            screen.blit(pause_pic, (0, 0))
        except:
            pass
        pygame.display.flip()
    else:
        screen.blit(gameover_pic, (0, 0))
        pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)

# Close the window and quit.
pygame.quit()
