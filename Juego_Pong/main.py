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