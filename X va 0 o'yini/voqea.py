import pygame

# Oyna o‘lchamlari
WIDTH, HEIGHT = 600, 800

# Pygame-ni ishga tushirish
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("X va O O'yini")

# Ranglar va shrift
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
font = pygame.font.Font(None, 72)
small_font = pygame.font.Font(None, 40)

# 3x3 kvadratlarning o‘lchamlari
SQ_SIZE = 120
MARGIN = 10

# Barcha elementlarni markazga joylash uchun boshlang‘ich koordinata
START_X = (WIDTH - (3 * SQ_SIZE + 2 * MARGIN)) // 2
START_Y = HEIGHT // 4

# Yangilash tugmasining o‘lchamlari va joylashuvi
BUTTON_WIDTH, BUTTON_HEIGHT = 180, 50
BUTTON_X = (WIDTH - BUTTON_WIDTH) // 2
BUTTON_Y = START_Y + 3 * (SQ_SIZE + MARGIN) + 40  # Kvadratlarning tagida
button_rect = pygame.Rect(BUTTON_X, BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT)

# O‘yinning boshlang‘ich holati
board = [["" for _ in range(3)] for _ in range(3)]
turn = "X"
game_over = False

# G‘olibni tekshiruvchi funksiya
def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]

    return None

# Durang bo‘lganini tekshiruvchi funksiya
def is_draw():
    for row in board:
        for cell in row:
            if cell == "":
                return False  # Hali bo‘sh joy bor, o‘yin davom etadi
    return True  # Hamma joy to‘ldi, lekin yutuvchi yo‘q

# O‘yinni qayta boshlash funksiyasi
def reset_game():
    global board, turn, game_over
    board = [["" for _ in range(3)] for _ in range(3)]
    turn = "X"
    game_over = False

# O‘yin tsikli
running = True
while running:
    win.fill(WHITE)

    # 3x3 kvadratlarni chizish
    for row in range(3):
        for col in range(3):
            rect_x = START_X + col * (SQ_SIZE + MARGIN)
            rect_y = START_Y + row * (SQ_SIZE + MARGIN)
            pygame.draw.rect(win, BLACK, (rect_x, rect_y, SQ_SIZE, SQ_SIZE), 2)

            # Kvadrat ichiga "X" yoki "O" chiqarish
            if board[row][col] == "X":
                text = font.render("X", True, RED)
                text_rect = text.get_rect(center=(rect_x + SQ_SIZE // 2, rect_y + SQ_SIZE // 2))
                win.blit(text, text_rect)
            elif board[row][col] == "O":
                text = font.render("O", True, BLUE)
                text_rect = text.get_rect(center=(rect_x + SQ_SIZE // 2, rect_y + SQ_SIZE // 2))
                win.blit(text, text_rect)

    # G‘olibni yoki durangni chiqarish
    winner = check_winner()
    draw = is_draw()

    if winner or draw:
        game_over = True
        message = f"{winner} yutdi!" if winner else "Durang!"
        
        # Xabar tugmadan 5 piksel pastda chiqadi
        text = small_font.render(message, True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, BUTTON_Y - 35))  # -40 emas, -35 bo‘ldi
        win.blit(text, text_rect)

        # Yangilash tugmasini chiqarish
        pygame.draw.rect(win, GRAY, button_rect)
        button_text = small_font.render("Yangilash", True, BLACK)
        text_rect = button_text.get_rect(center=button_rect.center)
        win.blit(button_text, text_rect)

    # Hodisalarni tekshirish
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Sichqoncha bosilganda
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # O'yin tugagan bo‘lsa va tugma bosilsa
            if game_over and button_rect.collidepoint(mouse_x, mouse_y):
                reset_game()

# O'yin davom etayotgan bo'lsa, yurish qilish
            if not game_over:
                for row in range(3):
                    for col in range(3):
                        rect_x = START_X + col * (SQ_SIZE + MARGIN)
                        rect_y = START_Y + row * (SQ_SIZE + MARGIN)

                        if rect_x <= mouse_x <= rect_x + SQ_SIZE and rect_y <= mouse_y <= rect_y + SQ_SIZE:
                            if board[row][col] == "":
                                board[row][col] = turn
                                turn = "O" if turn == "X" else "X"

    pygame.display.update()

pygame.quit()
