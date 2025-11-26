import clases as cl
import pygame
from mido import MidiFile

'''

'''

# antes iniciar pygame
#file = "./archivos midi/fc.mid"
#file = "./archivos midi/saxo_1_mano_miqueas_6_8.mid"
file = "./archivos midi/voz_saxo_miqueas_6_8.mid"



config = cl.Config()
archivo = cl.Archivo(file)
msj = cl.Notas()
teclado = cl.Teclado(config.ANCHO_PANTALLA,36,95)

#archivo.showOnlyRawMidi()
archivo.showOnlyRawMidi("note_on",2)

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