import pygame
import random
import math
import sys
import os
from pygame.locals import*

#Iniciar pygame
pygame.init()

#Establecer el tamaño de la pantalla
Ancho, Alto = 900, 680
screen = pygame.display.set_mode((Ancho, Alto))

#Funcion para obtener la ruta de los recursos
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

#Cargar imagen de fondo    
pygame.display.set_caption('Fishing Road')
icono = pygame.image.load("imagenes/iconopesca.png")
pygame.display.set_icon(icono)
lago = pygame.image.load("imagenes/lago.png")
lago = pygame.transform.scale(lago, (900,680))
screen.blit(lago, (0,0))

#Cargar sonido de fondo
musica = resource_path('imagenes/sonidodeimagenes.mp3')
musica = pygame.mixer.music.load(musica)

#Cargar imagen del jugador
jugador_a = resource_path('imagenes/caballerod.png')
jugador = pygame.image.load(jugador_a)

#Cagar fuente de texto de game over

font = pygame.font.SysFont("arialblack", 40)

#Caragar fuente para texto de puntaje
puntaje_a = resource_path('imagenes/descarga.png')
puntaje = pygame.font.Font(puntaje_a)

#Reproducir sonido de fondo en loop
pygame.mixer.music.play(-1)

#Crear reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

#Posicion inicial del jugador
jugadorX = 370
jugadorY = 470
jugadorx_change = 0
jugadory_change = 0

#Lista para almacenar posiciones de la basura
basura = []
basuraX = []
basuraY = []
basuraX_change = []
basuraY_change = []
no_of_basura = 10

#Se inicializan las variables para guardar las posiciones de la basura
for i in range(no_of_basura):
    #se carga la imagen de la basura
    basura1 = resource_path('imagenes/jugo.png')
    basura.append(pygame.image.load(basura1))

    basura2 = resource_path('imagenes/botella de agua1.png')
    basura.append(pygame.image.load(basura2))

    #Se asigna una posicion aleatoria en X y Y para la basura
    basuraX.append(random.randint(0,736))
    basuraY.append(random.randint(0,150))

    #Se establece la velocidad de movimiento de la basura en X e Y
    basuraX_change.append(5)
    basuraY_change.append(20)

    caña = pygame.image.load('imagenes/caña.png').convert_alpha
    
    #Se imicializan las variables para guardar la posicion de la caña
    cañaX = 0
    cañaY = 480
    cañaX_change = 0
    cañaY_change = 10
    caña_state = "ready"

    #Se inicializa la puntuacion en 0
    score = 0

    #Funcion para mostrar la puntuacion en la pantalla
    def show_score():
        score_value = font.render("SCORE " + str(score), True, (255,255,255))
        screen.blit(score_value, (10, 10))

    #Funcion para dibujar a la jugador en la pantalla
    def jugador(x , y):
        screen.blit(jugador, (x , y))

    #Funcion para dibujar a la basura en la pantalla
    def basura(x, y , i):
        screen.blit(basura[i], (x , y))
    
    #Funcion para bajar el hilo de la caña
    def caña_hilo(x, y):
        global caña_state

        caña_state = "bajar"
        screen.blit(caña, (x + 16, y +10) )

    #Funcion para comprobar si ha habido una colision entre el hilo y la basura
    def colision(basuraX, basuraY, cañaX, cañaY):
        distance = math.sqrt((math.pow(basuraX-cañaX, 2)) +
                             (math.pow(basuraY-cañaY, 2)))
        if distance < 27:
            return True
        else:
            return False

    #Funcion para mostrar el texto de game over en pantalla


    #Funcion principal del juego
    def gameloop():

        #Declarar variables globales
        global score
        global jugadorX
        global jugadorx_change
        global cañaX
        global cañaY
        global colision
        global caña_state

        in_game = True
        while in_game:
            #Maneja eventos, actualiza y renderiza el juego
            #Limpia la pantalla
            screen.fill((0, 0, 0))
            screen.blit(lago, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    in_game = False
                    pygame.quit()
                    sys.exit

                    if event.type == pygame.KEYDOWN:
                        #Movimientos del jugador y la caña
                        if event.key == pygame.K_LEFT:
                            jugadorx_change = -5

                        if event.key == pygame.K_RIGHT:
                            jugadorx_change = 5

                        if event.key == pygame.K_SPACE:
                            if caña_state == "ready":
                                cañaX = jugadorX
                                caña_hilo(cañaX, cañaY)

                    if event.type == pygame.KEYUP:
                        jugadorx_change = 0

            #Aqui esta actualizando la posicion del jugador 
            jugadorX += jugadorx_change

            if jugadorX <= 0:
                jugadorX = 0
            elif jugadorX >= 736:
                jugadorX = 736
            
            #Bucle que se ejecuta para cada basura
            for i in range(no_of_basura):
                if basuraY[i] > 440:
                    for j in range(no_of_basura):
                        basuraY[j] = 2000
                    

                basuraX[i] += basuraX_change[i]
                if basuraX[i] <= 0:
                    basuraX_change[i] = 5
                    basuraY[i] += basuraY_change[i]
                elif basuraX[i] >= 736:
                    basuraX_change[i] = -5
                    basuraY[i] += basuraY_change[i]

                 #Aqui se comprueba una colision entre una basura y el hilo

                collison = colision(basuraX[i], basuraY[i], cañaX, cañaY)
                if collison:
                    cañaY = 454
                    caña_state = "ready"
                    score += 1
                    basuraX[i] = random.randint(0, 736)
                    basuraY[i] = random.randint(0, 150)
                basura(basuraX[i], basuraY[i], i)

            if cañaY < 0:
                cañaY = 454
                caña_state = "ready"
            if caña_state == "lanza":
                caña_hilo(cañaX, cañaY)
                cañaY -= cañaY_change

            jugador(jugadorX, jugadorY)
            show_score()

            pygame.display.update()

            clock.tick(120)

gameloop()