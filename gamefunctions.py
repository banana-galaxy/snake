import random

def initiate_grid(window_size, block_size):
    grid = []
    size = window_size
    iterations = int(size / block_size)
    for x in range(iterations):
        grid.append([])
        for y in range(iterations):
            grid[x].append(0)

    return grid


def draw_grid(pygame, screen, screenSize, grid_size, block_size, color):
    for x in range(grid_size):
        pygame.draw.line(screen, color, [block_size*x, 0], [block_size * x, screenSize[1]])
    for y in range(grid_size):
        pygame.draw.line(screen, color, [0, block_size*y], [screenSize[0], block_size * y])


def collide(grid_size, snake, velocities):
    head = len(snake)-1
    next_head_x = snake[head][0]+velocities[0]
    next_head_y = snake[head][1] + velocities[1]

    # snake collision
    for cell in range(len(snake)):
        if cell != head:
            if snake[cell][0] == next_head_x and snake[cell][1] == next_head_y:
                return True

    # wall collision
    if next_head_x >= grid_size or next_head_x < 0:
        return True
    if next_head_y >= grid_size or next_head_y < 0:
        return True


class Food:

    def __init__(self, pygame, screen, block_size, color, x, y):
        self.pygame = pygame
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        self.block_size = block_size

    def pos(self):
        return self.x, self.y

    def eat(self):
        return 2

    def draw(self):
        self.pygame.draw.rect(self.screen, self.color, [self.x * self.block_size, self.y * self.block_size, self.block_size, self.block_size], 0)



'''collides = False
        for i in range(amount):
            while True:
                self.x = random.randrange(self.grid_size)
                self.y = random.randrange(self.grid_size)
                for cell in snake:
                    if cell == [self.x, self.y]:
                        collides = True
                if collides:
                    continue
                else:
                    break'''