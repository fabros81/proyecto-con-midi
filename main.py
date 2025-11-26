import clases as cl
import pygame
from mido import MidiFile

'''

'''

# antes iniciar pygame
config = cl.Config()
msj = cl.Notas()
teclado = cl.Teclado(config.ANCHO_PANTALLA,24,84)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((config.ANCHO_PANTALLA,config.ALTO_PANTALLA))
reloj = pygame.time.Clock()
running = True



tInicio = pygame.time.get_ticks()
while running:
    
    for event in pygame.event.get(): # itera sobre cada evento (movimiento de mouse y precion de tecla)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
    
    
    screen.fill(config.BLACK)
    
    teclado.dibujar(screen)
    
    
    pygame.display.update()
    pygame.display.flip() # siempre va antes de clock.tick() , no despues
    

pygame.quit()