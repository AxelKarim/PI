import pygame
import button

pygame.init()

#Funcion para especificar el tamaño de la ventana
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 680

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# Icono y título
pygame.display.set_caption('Fishing Road')
icono = pygame.image.load("imagenes/iconopesca.png")
pygame.display.set_icon(icono)

pygame.mixer.music.load('imagenes/sonidodenivel1.mp3')
pygame.mixer.music.play(-1)

#game variables
game_paused = False
menu_state = "main"

#Definir fuentes
font = pygame.font.SysFont("arialblack", 40)

# Paleta de colores en formato RGB
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#background
BG = pygame.image.load("imagenes/fondo.png")
BG = pygame.transform.scale(BG, (1200, 680))

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#game loop
run = True
while run:

  screen.blit(BG, (0,0))
  
  #load button images
  jugar_imagen = pygame.image.load("imagenes/botondeplay.png").convert_alpha()
  opciones_imagen = pygame.image.load("imagenes/botondeconfiguracion.png").convert_alpha()
  creditos_imagen = pygame.image.load("imagenes/botondecreditos.png").convert_alpha()
  salir_imagen = pygame.image.load("imagenes/botondesalir.png").convert_alpha()
  video_imagen = pygame.image.load('imagenes/button_video.png').convert_alpha()
  audio_imagen = pygame.image.load('imagenes/button_audio.png').convert_alpha()
  llave_imagen = pygame.image.load('imagenes/button_keys.png').convert_alpha()
  regreso_imagen = pygame.image.load('imagenes/button_back.png').convert_alpha()
  nivel1_imagen = pygame.image.load('imagenes/botonlvl1.png').convert_alpha()
  nivel2_imagen = pygame.image.load('imagenes/botonlvl2.png').convert_alpha()
  nivel3_imagen = pygame.image.load('imagenes/botonlvl3.png').convert_alpha()
  home_imagen = pygame.image.load('imagenes/pantallaprincipal.png').convert_alpha()
  
  #Funcion para cargar las imagenes del título
  titulo1 = pygame.image.load("imagenes/fishing.png").convert_alpha()
  titulo2 = pygame.image.load("imagenes/road.png").convert_alpha()

  #Funcion para acomodar el título
  screen.blit(titulo1, (300, 35))
  screen.blit(titulo2, (430, 135))

  #Funcion para darle uso al boton después de definirlo
  jugar_button = button.Button(500, 270, jugar_imagen, 1)
  opciones_button = button.Button(390, 465, opciones_imagen, 1)
  creditos_button = button.Button(525, 465, creditos_imagen, 1)
  salir_button = button.Button(650, 470, salir_imagen, 1)
  video_button = button.Button(226, 75, video_imagen, 1)
  audio_button = button.Button(225, 200, audio_imagen, 1)
  llave_button = button.Button(246, 325, llave_imagen, 1)
  regresar_button = button.Button(332, 450, regreso_imagen, 1)
  nivel1_button = button.Button(250, 200, nivel1_imagen, 1)
  nivel2_button = button.Button(525, 200, nivel2_imagen, 1)
  nivel3_button = button.Button(800, 200, nivel3_imagen, 1)
  salir_button = button.Button(660, 465, salir_imagen, 1)
  home_button = button.Button(525, 445, home_imagen, 1)

  #Función para revisar si el juego está pausado
  if game_paused == False:

    #Función para revisar el estado del menú
    if menu_state == "main":
      #draw pause screen buttons
      if jugar_button.draw(screen):
        menu_state = "play"
      if opciones_button.draw(screen):
        menu_state = "options"
      if creditos_button.draw(screen):
        menu_state = "creditos"
      if salir_button.draw(screen):
        run = False
        
    if menu_state == "play":
      screen.blit(BG, (0,0))
      
      if nivel1_button.draw(screen):
        if menu_state == "nivel1":
          from nivel1 import nivel1

      if nivel2_button.draw(screen):
        print("Inicio")
      if nivel3_button.draw(screen):
        print("Inicio")
      if home_button.draw(screen):
        menu_state = "main"

    #Función para introducir elementos en boton opciones
    if menu_state == "options":
      screen.blit(BG, (0,0))
      #draw the different options buttons
      if video_button.draw(screen):
        print("Video Settings")
      if audio_button.draw(screen):
        print("Audio Settings")
      if llave_button.draw(screen):
        print("Change Key Bindings")
      if home_button.draw(screen):
        menu_state = "main"

    if menu_state == "creditos":
      screen.blit(BG, (0,0))

      if home_button.draw(screen):
        menu_state = "main"
  else:
    draw_text("Press SPACE to pause", font, BLANCO, 160, 250)


  #Bucle para cerrar el juego
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        game_paused = True
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()

pygame.quit()