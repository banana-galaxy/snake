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