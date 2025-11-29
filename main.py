import clases as cl
import pygame
from mido import MidiFile

'''

'''

# antes iniciar pygame
file = "./archivos midi/fc.mid"
#file = "./archivos midi/saxo_1_mano_miqueas_6_8.mid"
#file = "./archivos midi/voz_saxo_miqueas_6_8.mid"


# Cambiar el orden de instanciación causa problemas, no modificarlo!!! (orden: config,archivo,teclado,msj)

config = cl.Config() # config se instancia antes de teclado obligatoriamente
archivo = cl.Archivo(config, file)
teclado = cl.Teclado(config,36,95)
msj = cl.Mensajes(config,archivo,teclado)
#config.verAtributosEnNone()

# herramientas para ver mensajes

#archivo.showOnlyRawMidi('note_on',1) # sintaxis: tipo de mensaje: 'note_on' or None, channel: None or [1,2,3,4]) 
msj.printMsj1()


# pygame setup
pygame.init()
screen = pygame.display.set_mode((config.ANCHO_PANTALLA,config.ALTO_PANTALLA))
reloj = pygame.time.Clock()
running = True



tInicio = pygame.time.get_ticks()
while running:
    dt_ms = reloj.tick(60)
    dt_s = dt_ms/1000
    
    for event in pygame.event.get(): # itera sobre cada evento (movimiento de mouse y precion de tecla)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
    
    
    screen.fill(config.BLACK)
    
    
    #msj.dibujar(screen,tInicio,dt_s)
    teclado.dibujar(screen)
    #msj.actualizar(tInicio,dt_s)
    
    
    pygame.display.update()
    pygame.display.flip() # siempre va antes de clock.tick() , no despues
    

pygame.quit()