import pygame
import random
import sys

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40

# This sets the margin between each cell
MARGIN = 5

answer = []
grid = []
for row in range(8):
    grid.append([])
    answer.append([])
    for column in range(8):
        grid[row].append(0)  # Append a cell
        answer[row].append(0)

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [365, 420]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Memory Test")

# Loop until the user clicks the close button.
done = False
done1 = False
check = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
smallfont = pygame.font.SysFont(None, 35)
bigfont = pygame.font.SysFont(None, 60)

n = 0

while not check:
    done = False
    done1 = False

    n = n + 1

    level = smallfont.render('Level ' + str(n), True, WHITE)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            check = True  # Flag that we are done so we exit this loop
            done = True
            done1 = True

    while True:
        rr = random.randint(0, 7)
        cc = random.randint(0, 7)
        if answer[rr][cc] == 1:
            continue
        else:
            answer[rr][cc] = 1
            break

    frame_count = 0
    frame_rate = 60
    start_time = 5
    fight_time = 10

    while not done:
        screen.fill(BLACK)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
                check = True
                done1 = True
            if seconds == 0:
                done = True
        # Set the screen background

        total_seconds = start_time - (frame_count // frame_rate)
        if total_seconds < 0:
            total_seconds = 0

        seconds = total_seconds % 60

        # Blit to the screen
        text = smallfont.render('Time ' + str(seconds), True, WHITE)

        screen.blit(text, (270, 370))

        for row in range(8):
            for column in range(8):
                color = WHITE
                if answer[row][column] == 1:
                    color = GREEN
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        frame_count += 1
        screen.blit(level, (10, 370))

        # Limit frames per second
        clock.tick(frame_rate)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    frame_count = 0
    frame_rate = 60
    start_time = 5
    fight_time = 10

    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0
    seconds = total_seconds % 60

    grid = []
    for row in range(8):
        grid.append([])
        for column in range(8):
            grid[row].append(0)  # Append a cell

    while not done1:

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done1 = True
                check = True
                done = True
            elif seconds == 0:
                run = False
                while not run:

                    for event in pygame.event.get():  # User did something
                        if event.type == pygame.QUIT:  # If user clicked close
                            done = True
                            check = True
                            done1 = True
                            run = True
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            run = True

                    screen.fill(BLACK)

                    lose = bigfont.render('LOSE !!', True, WHITE)
                    screen.blit(lose, (120, 180))

                    clock.tick(frame_rate)
                    pygame.display.flip()

                answer = []
                for row in range(8):
                    answer.append([])
                    for column in range(8):
                        answer[row].append(0)

                n = 0

                done1 = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                if row >= 0 and row < 8 and column >= 0 and column < 8:
                    if grid[row][column] == 0:
                        grid[row][column] = 1
                    else:
                        grid[row][column] = 0
                    print("Click ", pos, "Grid coordinates: ", row, column)

            ch = 0
            for i in range(8):
                for j in range(8):
                    if (grid[i][j] != answer[i][j]):
                        ch = 1
                        break
                if ch == 1:
                    break
            if ch == 0 and done1 == False:
                run = False
                while not run:

                    for event in pygame.event.get():  # User did something
                        if event.type == pygame.QUIT:  # If user clicked close
                            done = True
                            check = True
                            done1 = True
                            run = True
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            run = True

                    screen.fill(BLACK)

                    win = bigfont.render('WIN !!', True, WHITE)
                    screen.blit(win, (120, 180))

                    clock.tick(frame_rate)
                    pygame.display.flip()

                done1 = True

        screen.fill(BLACK)

        total_seconds = fight_time - (frame_count // frame_rate)
        if total_seconds < 0:
            total_seconds = 0

        seconds = total_seconds % 60

        # Blit to the screen
        text = smallfont.render('Time ' + str(seconds), True, WHITE)

        screen.blit(text, (270, 370))

        frame_count += 1
        # Set the screen background

        # Draw the grid
        for row in range(8):
            for column in range(8):
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])

        screen.blit(level, (10, 370))

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
