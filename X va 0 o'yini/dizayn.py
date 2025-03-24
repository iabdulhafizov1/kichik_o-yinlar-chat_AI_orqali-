import pygame

# Pygame-ni ishga tushirish
pygame.init()

# Oyna o‘lchamlari
WIDTH, HEIGHT = 600, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame 3x3 Kvadratlar")

# Ranglar
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

# Kvadrat sozlamalari
SQ_SIZE = 100  # Kvadrat o‘lchami
MARGIN = 10  # Kvadratlar orasidagi bo‘shliq
START_X, START_Y = 50, 50  # Kvadratlarning boshlang‘ich joyi

# Oynacha va tugma o‘lchamlari
INPUT_WIDTH, INPUT_HEIGHT = 130, 40
INPUT_X, INPUT_Y = 50, 430
BUTTON_X = INPUT_X + INPUT_WIDTH + 10  # Tugma input maydonining o'ng tomonida

# Input maydon va tugma
input_rect = pygame.Rect(INPUT_X, INPUT_Y, INPUT_WIDTH, INPUT_HEIGHT)
button_rect = pygame.Rect(BUTTON_X, INPUT_Y, INPUT_WIDTH, INPUT_HEIGHT)

# **Shu o‘zgaruvchilarni voqea.py import qilib oladi**
