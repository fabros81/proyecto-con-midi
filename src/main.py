import clases as cl
import pygame
from mido import MidiFile

# antes iniciar pygame
config = Config()
# pygame setup
pygame.init()


screen = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
reloj = pygame.time.Clock()
running = True
#printConstantes()
read_metamsg(file_midi_path)
MSJS = read_midi(file_midi_path)   

RECORRIDO = (ALTO_PANTALLA-ALTO_TECLA ) # RECORRIDO DE LA NOTA EN PIXELES
SEGUNDOS_POR_PULSO =  60/PPM # ESTO ES LO QUE DURA UNA NEGRA
factor_ajuste = 100.0 / AJUSTE_TEMPO_PORCENTAJE  # Aplicar mismo ajuste
SEGUNDOS_POR_PULSO_AJUSTADO = SEGUNDOS_POR_PULSO * factor_ajuste

PPS = RECORRIDO / (SEGUNDOS_POR_PULSO_AJUSTADO * PULSOS_EN_PANTALLA) #PIXELES POR SEGUNDO para que la velocidad esté a tempo

# debuggin manual
#getMSJS(MSJS) # imprime los msg´s en consola(ya procesados)


#printConstantes()
tInicio = pygame.time.get_ticks()
while running:


