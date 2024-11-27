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

# Clase para la bola
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def move(self):
        # Movimiento de la bola
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Rebote en el borde superior e inferior
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1

    def reset(self):
        # Reinicio de la posición de la bola
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed_x *= -1

    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)

# Creación de las Raquetas y la bola (Player es la maquina, Oponnent es el usuariO)
player_paddle = Paddle(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
opponent_paddle = Paddle(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball()

# Variables para la puntuación
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 36)

# Bucle principal del juego
running = True
while running:
    # Manejo de eventos, es decir, cuando el usuario decide cerrar el juego (Finalizarlo)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimientos del jugador (Usuario)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_paddle.move(up=True)
    if keys[pygame.K_DOWN]:
        player_paddle.move(up=False)

    # Movimiento del oponente (básico) (Máquina)
    if opponent_paddle.rect.centery < ball.rect.y:
        opponent_paddle.move(up=False)
    if opponent_paddle.rect.centery > ball.rect.y:
        opponent_paddle.move(up=True)

    # Movimiento de la bola
    ball.move()

    # Colisiones con las Raquetas
    if ball.rect.colliderect(player_paddle.rect) or ball.rect.colliderect(opponent_paddle.rect):
        ball.speed_x *= -1

    # Marcador del juego
    if ball.rect.left <= 0:
        player_score += 1
        ball.reset()
    if ball.rect.right >= SCREEN_WIDTH:
        opponent_score += 1
        ball.reset()

    # Dibujo de la pantalla, es decir, el Renderizar el juego
    screen.fill(BLACK)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    # Mostramos la puntuación
    player_text = font.render(f"Jugador: {player_score}", True, WHITE)  # Puntuación del jugador (usuario)
    opponent_text = font.render(f"Máquina: {opponent_score}", True, WHITE)  # Puntuación de la máquina (oponente)

    # Colocamos el marcador de la máquina (oponente) en el lado izquierdo
    screen.blit(opponent_text, (30, 20))

    # Colocamos el marcador del jugador (usuario) en el lado derecho, asegurándonos de que se ajuste al ancho del texto
    screen.blit(player_text, (SCREEN_WIDTH - player_text.get_width() - 30, 20))
