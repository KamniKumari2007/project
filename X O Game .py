import pygame
pygame.init()

# Screen
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("X O Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

size = 200
board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]]

player = "X"
font = pygame.font.Font(None, 120)

run = True
while run:
    screen.fill(WHITE)

    # Grid lines
    pygame.draw.line(screen, BLACK, (200, 0), (200, 600), 5)
    pygame.draw.line(screen, BLACK, (400, 0), (400, 600), 5)
    pygame.draw.line(screen, BLACK, (0, 200), (600, 200), 5)
    pygame.draw.line(screen, BLACK, (0, 400), (600, 400), 5)

    # Draw X and O
    for row in range(3):
        for col in range(3):
            if board[row][col] != "":
                text = font.render(board[row][col], True, BLACK)
                screen.blit(text, (col * size + 65, row * size + 35))

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // 200
            col = mouse_x // 200

            if board[row][col] == "":
                board[row][col] = player

                # Switch player
                if player == "X":
                    player = "O"
                else:
                    player = "X"

    pygame.display.update()

pygame.quit()