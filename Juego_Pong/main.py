import pygame
import sys

# Autor: Alex Jiménez Quiñonero
# Ejercicio: Programem jocs amb Python
# Fecha: 27/11/2024

# Iniciamos el Pygame
pygame.init()

# Configuración de la pantalla
SCREEN_WIDTH = 900  # Anchura
SCREEN_HEIGHT = 600  # Altura
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego Pong by Alex JQ")  # Título del Juego

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Dimensiones de la paleta y la bola
PADDLE_WIDTH = 10  # Raqueta
PADDLE_HEIGHT = 100
BALL_SIZE = 20  # Bola

# Velocidades de la bola y las raquetas (Paddle)
BALL_SPEED_X = 7  # Bola
BALL_SPEED_Y = 7
PADDLE_SPEED = 7  # Raqueta

# Clase para la Raqueta
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, up=True):
        if up:
            self.rect.y -= PADDLE_SPEED
        else:
            self.rect.y += PADDLE_SPEED

        # Limitamos el movimiento dentro de la pantalla
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)