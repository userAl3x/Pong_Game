# Juego Pong 🎮

Un juego clásico de Pong implementado en Python utilizando Pygame. El jugador compite contra una IA básica para alcanzar la mayor puntuación.

**Autor:** Alex Jiménez Quiñonero  
**Fecha:** 27/11/2024

## 📋 Descripción

Este proyecto es una implementación del clásico juego Pong donde el jugador controla una paleta en el lado derecho de la pantalla y compite contra una IA que controla la paleta del lado izquierdo. El objetivo es hacer que la bola pase la paleta del oponente mientras evitas que pase la tuya.

## 🎯 Características

- **Juego para un jugador**: Compite contra una IA que sigue automáticamente la bola
- **Sistema de puntuación**: Marcador en tiempo real para jugador y máquina
- **Física de rebote**: La bola rebota en las paredes superior e inferior y en las paletas
- **Interfaz limpia**: Diseño minimalista en blanco y negro con línea divisoria central
- **Movimiento fluido**: 60 FPS para una experiencia de juego suave

## 🛠️ Requisitos

- Python 3.x
- Pygame

## 📦 Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/tu-usuario/Juego_Pong.git
cd Juego_Pong
```

2. Instala Pygame:
```bash
pip install pygame
```

## 🚀 Ejecución

Para iniciar el juego, ejecuta:
```bash
python main.py
```

## 🎮 Controles

- **Flecha Arriba (↑)**: Mover la paleta del jugador hacia arriba
- **Flecha Abajo (↓)**: Mover la paleta del jugador hacia abajo
- **Cerrar ventana**: Terminar el juego

## 📝 Explicación del Código

### Estructura del Proyecto

El juego está completamente contenido en el archivo `main.py` y utiliza programación orientada a objetos para organizar los elementos del juego.

### Configuración Inicial

```python
pygame.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
```

- Se inicializa Pygame
- La ventana del juego tiene dimensiones de 900x600 píxeles
- Se definen constantes para colores, velocidades y dimensiones de objetos

### Clases Principales

#### 1. Clase `Paddle` (Paleta/Raqueta)

Representa las paletas que controlan tanto el jugador como la IA.

**Métodos:**
- `__init__(x, y)`: Inicializa la paleta en una posición específica
- `move(up)`: Mueve la paleta arriba o abajo, limitando el movimiento dentro de la pantalla
- `draw()`: Dibuja la paleta en la pantalla

#### 2. Clase `Ball` (Bola)

Representa la bola del juego.

**Métodos:**
- `__init__()`: Inicializa la bola en el centro de la pantalla con velocidad inicial
- `move()`: Actualiza la posición de la bola y maneja los rebotes en paredes superior/inferior
- `reset()`: Reinicia la posición de la bola al centro e invierte su dirección horizontal
- `draw()`: Dibuja la bola como una elipse blanca

### Lógica del Juego

#### Instanciación de Objetos

```python
player_paddle = Paddle(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
opponent_paddle = Paddle(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball()
```

- `player_paddle`: Paleta del jugador en el lado derecho
- `opponent_paddle`: Paleta de la IA en el lado izquierdo
- `ball`: Bola del juego

#### Bucle Principal

El bucle `while running` maneja toda la lógica del juego:

**1. Gestión de Eventos**
```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
```
Detecta si el usuario cierra la ventana.

**2. Control del Jugador**
```python
keys = pygame.key.get_pressed()
if keys[pygame.K_UP]:
    player_paddle.move(up=True)
if keys[pygame.K_DOWN]:
    player_paddle.move(up=False)
```
Lee las teclas presionadas y mueve la paleta del jugador.

**3. IA del Oponente**
```python
if opponent_paddle.rect.centery < ball.rect.y:
    opponent_paddle.move(up=False)
if opponent_paddle.rect.centery > ball.rect.y:
    opponent_paddle.move(up=True)
```
La IA sigue la posición vertical de la bola, creando un oponente automático.

**4. Detección de Colisiones**
```python
if ball.rect.colliderect(player_paddle.rect) or ball.rect.colliderect(opponent_paddle.rect):
    ball.speed_x *= -1
```
Invierte la dirección horizontal de la bola cuando colisiona con una paleta.

**5. Sistema de Puntuación**
```python
if ball.rect.left <= 0:
    player_score += 1
    ball.reset()
if ball.rect.right >= SCREEN_WIDTH:
    opponent_score += 1
    ball.reset()
```
Incrementa la puntuación cuando la bola sale por un lado de la pantalla.

**6. Renderizado**
```python
screen.fill(BLACK)
pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
# ... dibuja marcadores, paletas y bola
pygame.display.flip()
pygame.time.Clock().tick(60)
```
- Limpia la pantalla
- Dibuja la línea central
- Muestra los marcadores
- Dibuja las paletas y la bola
- Actualiza la pantalla a 60 FPS

## 🎨 Parámetros Personalizables

Puedes modificar estas constantes al inicio del código para ajustar la dificultad y apariencia:

- `SCREEN_WIDTH` / `SCREEN_HEIGHT`: Tamaño de la ventana
- `PADDLE_WIDTH` / `PADDLE_HEIGHT`: Dimensiones de las paletas
- `BALL_SIZE`: Tamaño de la bola
- `BALL_SPEED_X` / `BALL_SPEED_Y`: Velocidad de la bola
- `PADDLE_SPEED`: Velocidad de movimiento de las paletas

## 📚 Conceptos de Programación Utilizados

- **Programación Orientada a Objetos**: Clases `Paddle` y `Ball`
- **Bucle de Juego**: Patrón de game loop con actualización y renderizado
- **Detección de Colisiones**: Usando `colliderect()` de Pygame
- **Gestión de Eventos**: Manejo de entrada del teclado y cierre de ventana
- **Renderizado 2D**: Dibujo de formas y texto en pantalla

## 🔮 Posibles Mejoras

- Añadir niveles de dificultad
- Implementar efectos de sonido
- Agregar un menú principal
- Modo para dos jugadores
- Efectos de partículas al colisionar
- Guardar puntuación máxima

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

---

¡Disfruta del juego! 🎮✨
