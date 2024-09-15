import random
import pygame
from sys import exit
import time

pygame.init()
width = 400
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("")

COLS = 20
ROWS = 20
DED = 0
LIVE = 1

grid = [[random.choice([0, 1]) for _ in range(COLS)] for _ in range(ROWS)]
for i in grid:
    print(i)

num = 4
counter = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    for row in range(len(grid)):
        for colum in range(len(grid[0])):
            if row < ROWS or colum < COLS:
                for i in range(row - 1, row + 2):
                    for j in range(colum - 1, colum + 2):
                        if (0 <= i < ROWS and 0 <= j < COLS) and grid[i][j] == 1:
                            counter += 1

                if grid[row][colum] == LIVE:
                    counter -= 1
                    if counter <= 1:
                        grid[row][colum] = DED
                        print("Died from loneliness")
                    elif counter > 3:
                        grid[row][colum] = DED
                        print("Died from density")
                    else:
                        grid[row][colum] = LIVE
                        print("Not change")
                else:
                    if counter == 3:
                        grid[row][colum] = LIVE
                        print("Born")
                    else:
                        grid[row][colum] = DED
                        print("Not change")
            counter = 0
            for i in grid:
                print(i)

            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 1:
                        rect = pygame.Rect(i * 20, j * 20, height / 20, width / 20)
                        pygame.draw.rect(screen, 'green', rect, 10)
                    else:
                        rect = pygame.Rect(i * 20, j * 20, height / 20, width / 20)
                        pygame.draw.rect(screen, 'white', rect, 10)

            for i in range(0, width, int(height / 20)):
                for j in range(0, height, int(width / 20)):
                    rect = pygame.Rect(i, j, height / 20, width / 20)
                    pygame.draw.rect(screen, 'black', rect, 1)
            pygame.display.update()



