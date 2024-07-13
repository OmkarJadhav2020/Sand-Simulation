import pygame
import random
import colorsys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH, HEIGHT = 1300, 720
TILE_SIZE = 8
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sand Simulation")

CLOCK = pygame.time.Clock()

def draw_grid():
    for col in range(GRID_WIDTH):
        pygame.draw.line(display, WHITE, (TILE_SIZE * col, 0), (TILE_SIZE * col, HEIGHT), 1)
    for row in range(GRID_HEIGHT):
        pygame.draw.line(display, WHITE, (0, TILE_SIZE * row), (WIDTH, TILE_SIZE * row), 1)

def hsb_to_rgb(h, s, b):
    r, g, bl = colorsys.hsv_to_rgb(h, s, b)
    return int(r * 255), int(g * 255), int(bl * 255)

def create_sand(positions):
    new_positions = [[[0, 0] for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            if positions[i][j][0] == 1:
                if (i + 1) < GRID_HEIGHT and positions[i + 1][j][0] == 0:
                    new_positions[i + 1][j][0] = 1
                    new_positions[i + 1][j][1] = positions[i][j][1]
                elif (i + 1) < GRID_HEIGHT and (j + 1) < GRID_WIDTH and positions[i + 1][j + 1][0] == 0:
                    new_positions[i + 1][j + 1][0] = 1
                    new_positions[i + 1][j + 1][1] = positions[i][j][1]
                elif (i + 1) < GRID_HEIGHT and (j - 1) >= 0 and positions[i + 1][j - 1][0] == 0:
                    new_positions[i + 1][j - 1][0] = 1
                    new_positions[i + 1][j - 1][1] = positions[i][j][1]
                else:
                    new_positions[i][j][0] = 1
                    new_positions[i][j][1] = positions[i][j][1]

    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            if new_positions[i][j][0] == 1:
                color = hsb_to_rgb(new_positions[i][j][1], 1, 1)
                col, row = j, i
                top_left = (col * TILE_SIZE, row * TILE_SIZE)
                pygame.draw.rect(display, color, (*top_left, TILE_SIZE, TILE_SIZE))
    return new_positions

def main():
    running = True
    positions = [[[0, 0] for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    sand = False
    hue = 0
    while running:
        CLOCK.tick(FPS)
        hue += 0.001
        if hue > 1:
            hue = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                sand = True
            elif event.type == pygame.MOUSEBUTTONUP:
                sand = False

        if sand:
            x, y = pygame.mouse.get_pos()
            col = x // TILE_SIZE
            row = y // TILE_SIZE

            for dx in [-2, -1, 0, 1, 2]:
                for dy in [-2, -1, 0, 1, 2]:
                    x1 = row + dx
                    y1 = col + dy
                    if 0 <= x1 < GRID_HEIGHT and 0 <= y1 < GRID_WIDTH and random.choice([0, 1]):
                        positions[x1][y1][0] = 1
                        positions[x1][y1][1] = hue

        display.fill(BLACK)
        positions = create_sand(positions)
        pygame.display.update()

if __name__ == "__main__":
    main()
