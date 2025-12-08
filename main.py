import clases as cl
import pygame
from mido import MidiFile

'''
- Estoy cambiando el mensaje midi para que sea una lista en vez de un objeto Nota. No logre todavía lanzar los objetos sin que lance un error


'''

# antes iniciar pygame
#file = "./archivos midi/fc.mid"
#file = "./archivos midi/saxo_1_mano_miqueas_6_8.mid"
file = "./archivos midi/voz_saxo_miqueas_6_8.mid"
#file = "./archivos midi/ch4_miqueas_6_8.mid"

# Cambiar el orden de instanciación causa problemas, no modificarlo!!! (orden: config,archivo,teclado,msj)

config = cl.Config() # config se instancia antes de teclado obligatoriamente
archivo = cl.Archivo(config, file)

#archivo.showOnlyRawMidi() # sintaxis: tipo de mensaje: 'note_on' or None, channel: None or [1,2,3,4]) 

teclado = cl.Teclado(config,36,95)
msj = cl.Mensajes(config,archivo, teclado)

# herramientas para ver mensajes

#msj.printMsj1() 


# pygame setup
pygame.init()
screen = pygame.display.set_mode((config.ANCHO_PANTALLA,config.ALTO_PANTALLA))
reloj = pygame.time.Clock()
running = True





config.setTiempoInicio()
#config.verAtributosEnNone()
while running:
    config.dt(reloj)
        
    for event in pygame.event.get(): # itera sobre cada evento (movimiento de mouse y precion de tecla)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
        
    screen.fill(config.BLACK)
        
    msj.dibujar(screen)
    teclado.dibujar(screen)
    msj.actualizar()
    
    
    pygame.display.update()
    pygame.display.flip() # siempre va antes de clock.tick() , no despues
    

pygame.quit()
