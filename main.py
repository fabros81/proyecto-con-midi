import clases as cl
import pygame
from mido import MidiFile

'''

'''

# antes iniciar pygame
config = cl.Config()
msj = cl.Notas()
teclado = cl.Teclado(config.ANCHO_PANTALLA,21,60)

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
    
    #teclado.printCoordX()   
    #teclado.dibujar(screen) # esto no anda, no dibuja el teclado blanco y negro en la pantalla. Queda resolver eso.
    #pienso que el método de crear rect que propone la ia, si bien esta dentro del menu de posibilidades, tengo el vago recuerdo que 
    #no funciona bien. Que haciendo el rect(x,y,weigth,height)y poniendolo dentro de pygame.draw.rect(pantalla,tecla.mostrarColor, "y aca el rect no tuplas ni ocho cuartos")
    
    pygame.display.update()
    pygame.display.flip() # siempre va antes de clock.tick() , no despues
    

pygame.quit()