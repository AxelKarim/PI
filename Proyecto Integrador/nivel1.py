import pygame
import random
import math
import sys
import os

from pygame.locals import *

pygame.init()

#aqui configuras el ancho de la pantalla
Ancho, Alto = 900, 680
screen = pygame.display.set_mode((Ancho, Alto))

# Títulos de juego
pygame.display.set_caption('Fishing Road')
icono = pygame.image.load("imagenes/iconopesca.png")
pygame.display.set_icon(icono)

# Carga de imágenes y música
lago = pygame.image.load("imagenes/lago.png").convert_alpha()
lago = pygame.transform.scale(lago, (900, 680))

pygame.mixer.music.load('imagenes/sonidodenivel1.mp3')
pygame.mixer.music.play(-1)

# Jugador
jugadors1 = pygame.image.load('imagenes/caballerod.png').convert_alpha()

# Bucle del juego principal
def gameloop():
    jugadorX = 150
    jugadorY = 290
    jugadorx_change = 0
    
    # Puntuación
    score = 0
    myfont = pygame.font.Font(None, 32)  # Utilizando una fuente predeterminada

    #Tiempo
    Fuente = pygame.font.SysFont(None,32)
    tiempo_limite = 120 

    # Basura
    basuras_a = pygame.image.load('imagenes/jugo.png').convert_alpha()
    basuras_b = pygame.image.load('imagenes/BOLSA DE PAPAS.png').convert_alpha()
    basuras_c = pygame.image.load('imagenes/botella de agua1.png').convert_alpha()
    basuras_d = pygame.image.load('imagenes/LATA DE SODA.png').convert_alpha()
    basuras_f = pygame.image.load('imagenes/LLANTA.png').convert_alpha()
    basuras = []
    for i in range(3):  # Crear 10 basuras
        basuras.append({
            'x': random.randint(0, 170),
            'y': random.randint(0, 290),
            'x_change': 0.5,
            'y_change': 0.5,
            'img': basuras_a
        })
#inicio de bucle
    running = True
    while running:
        #Tiempo
        screen.fill((255,255,255))
        Tiempo = pygame.time.get_ticks()/1000
        if Tiempo > tiempo_limite:
           break
          
            

        screen.blit(lago, (0, 0))

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jugadorx_change = -3
                    jugadors = pygame.image.load('imagenes/fbizq.png').convert_alpha()
                    screen.blit(jugadors, (jugadorX, jugadorY))
                elif event.key == pygame.K_RIGHT:
                    jugadorx_change = 3
            elif event.type == pygame.KEYUP:
                jugadorx_change = 0

        # Mover jugador
        jugadorX += jugadorx_change
        jugadorX = max(170, min(jugadorX, 600))  # Asegurate de que el jugador no salga de la pantalla
        
        # Mostrar jugador
        screen.blit(jugadors1, (jugadorX, jugadorY))

        # Mostrar y mover basuras
        for basura in basuras:
            screen.blit(basura['img'], (basura['x'], basura['y']))
            basura['x'] += basura['x_change']
            basura['y'] += basura['y_change']
            
            # Si la basura sale de la pantalla, reinicia su posición
            if basura['y'] > Alto:
                basura['y'] = 0
                basura['x'] = random.randint(170, 736)

        # Mostrar puntuación
        score_value = myfont.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_value, (10, 10))

        #Mostrar Tiempo
        contador = Fuente.render("Tiempo : "+str(Tiempo), True, (255,255,255))
        screen.blit(contador,(10,30))

        pygame.display.update()
        pygame.time.Clock().tick(120)  #aqui estan los fotogramas

# Ejecutar el bucle de juego
gameloop()
pygame.quit()
