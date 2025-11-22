# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 13:33:37 2024

@author: Administrador
se creo con el ambiente base de anaconda hasta que tuve que incluir la librería opencv(cv2), la cual no pude hacerla andar con conda.
Armé el env "entorno_prueba" e instalé cv2  pygame desde un github y funcionó. Quedo trabajando en este entorno


https://github.com/tdrmk/pygame_recorder
este github tiene un trabajo hecho para poder capturar los frame´s en pygame que esto intentando aprovechar

"""
#%%  path cancion

file_midi_path = "C:/Users/Fabianr/Desktop/UNSAM/programación 1/proyecto con midi/feliz cumpleaños.mid"

# file_midi_path = "C:/Users/Fabianr/Desktop/UNSAM/programación 1/proyecto con midi/roca_fuerte.mid"
#%% librerias

import pygame
from mido import MidiFile
from pygame_recorder import ScreenRecorder

#%%  variables constantes

ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600 
#colores en rgb
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
# cantidad de teclas blancas : 35 (desde nota 36 a 95)
CANT_TECLAS_BL = 35  # OJO CON CAMBIARLA!!!!! vas a tener que revisar el diccionario con las coordenadas para la nueva cantidad de teclas, no probé si funciona para otra cantidad de teclas
MIN_MAX_TECLA = [36,95] # indica el primer y último número de tecla del piano
ANCHO_TECLA = ANCHO_PANTALLA / CANT_TECLAS_BL
ALTO_TECLA = ANCHO_TECLA*150/26
# si son 35 teclas blancas, arrancando de La 50 a la 85
FINAL_RECORRIDO = 470 # intenté poner algo asi como alto_pantalla-alto_tecla-nota.height, pero no funcionaba. Usmeando encontré que solo reconocía numeros enteros pares.
# de hecho si asignas a FINAL_RECORRIDO un número impar no funciona. No se porqué todavía.

PPM = 80 # lo definen los metamensajes, por ahora es manual
TICKS_X_PULSO = 24 # lo definen los metamensajes, por ahora es manual
CLAVE = "cuatro_cuartos" # lo definen los metamensajes, por ahora es manual
PULSO = 60000/PPM# en milisegundos  # variable constante (60000 milisegundos / PPM)
TICK = PULSO/TICKS_X_PULSO #variable constante
PIXELES_X_PULSO = 60
VELOCIDAD = 2 # solo numeros enteros >= 1
FPS = 60
lanzar = []

coord_nota_35={36:0,
               37:0+12/23*ANCHO_TECLA,
               38:0+ANCHO_TECLA*1,
               39:0+40/23*ANCHO_TECLA,
               40:0+ANCHO_TECLA*2,
               41:0+ANCHO_TECLA*3,
               42:0+80/23*ANCHO_TECLA,
               43:0+ANCHO_TECLA*4,
               44:0+108/23*ANCHO_TECLA,
               45:0 + ANCHO_TECLA * 5,
               46:0+136/23*ANCHO_TECLA,
               47:0 + ANCHO_TECLA * 6,
               48:1*(7*ANCHO_TECLA),
               49:1*(7*ANCHO_TECLA)+12/23*ANCHO_TECLA, 
               50:1*(7*ANCHO_TECLA)+ANCHO_TECLA*1,
               51:1*(7*ANCHO_TECLA)+40/23*ANCHO_TECLA,
               52:1*(7*ANCHO_TECLA)+ANCHO_TECLA*2,
               53:1*(7*ANCHO_TECLA)+ANCHO_TECLA*3,
               54:1*(7*ANCHO_TECLA)+80/23*ANCHO_TECLA,
               55:1*(7*ANCHO_TECLA)+ANCHO_TECLA * 4,
               56:1*(7*ANCHO_TECLA)+108/23*ANCHO_TECLA,
               57:1*(7*ANCHO_TECLA)+ANCHO_TECLA * 5,
               58:1*(7*ANCHO_TECLA)+136/23*ANCHO_TECLA,
               59:1*(7*ANCHO_TECLA)+ANCHO_TECLA * 6,
               60:2*(7*ANCHO_TECLA), 
               61:2*(7*ANCHO_TECLA)+12/23*ANCHO_TECLA, 
               62:2*(7*ANCHO_TECLA)+ANCHO_TECLA*1,
               63:2*(7*ANCHO_TECLA)+40/23*ANCHO_TECLA,
               64:2*(7*ANCHO_TECLA)+ANCHO_TECLA*2,
               65:2*(7*ANCHO_TECLA)+ANCHO_TECLA*3,
               66:2*(7*ANCHO_TECLA)+80/23*ANCHO_TECLA,
               67:2*(7*ANCHO_TECLA)+ANCHO_TECLA*4,
               68:2*(7*ANCHO_TECLA)+108/23*ANCHO_TECLA,
               69:2*(7*ANCHO_TECLA)+ANCHO_TECLA * 5,
               70:2*(7*ANCHO_TECLA)+136/23*ANCHO_TECLA,
               71:2*(7*ANCHO_TECLA)+ANCHO_TECLA * 6,
               72:3*(7*ANCHO_TECLA), 
               73:3*(7*ANCHO_TECLA)+12/23*ANCHO_TECLA, 
               74:3*(7*ANCHO_TECLA)+ANCHO_TECLA*1,
               75:3*(7*ANCHO_TECLA)+40/23*ANCHO_TECLA,
               76:3*(7*ANCHO_TECLA)+ANCHO_TECLA*2,
               77:3*(7*ANCHO_TECLA)+ANCHO_TECLA*3,
               78:3*(7*ANCHO_TECLA)+80/23*ANCHO_TECLA,
               79:3*(7*ANCHO_TECLA)+ANCHO_TECLA*4,
               80:3*(7*ANCHO_TECLA)+108/23*ANCHO_TECLA,
               81:3*(7*ANCHO_TECLA)+ANCHO_TECLA * 5,
               82:3*(7*ANCHO_TECLA)+136/23*ANCHO_TECLA,
               83:3*(7*ANCHO_TECLA)+ANCHO_TECLA * 6,
               84:4*(7*ANCHO_TECLA), 
               85:4*(7*ANCHO_TECLA)+12/23*ANCHO_TECLA, 
               86:4*(7*ANCHO_TECLA)+ANCHO_TECLA*1,
               87:4*(7*ANCHO_TECLA)+40/23*ANCHO_TECLA,
               88:4*(7*ANCHO_TECLA)+ANCHO_TECLA*2,
               89:4*(7*ANCHO_TECLA)+ANCHO_TECLA*3,
               90:4*(7*ANCHO_TECLA)+80/23*ANCHO_TECLA,
               91:4*(7*ANCHO_TECLA)+ANCHO_TECLA*4, 
               92:4*(7*ANCHO_TECLA)+108/23*ANCHO_TECLA,
               93:4*(7*ANCHO_TECLA)+ANCHO_TECLA * 5,
               94:4*(7*ANCHO_TECLA)+136/23*ANCHO_TECLA,
               95:4*(7*ANCHO_TECLA)+ANCHO_TECLA * 6      }

tecl_bla = [36,38,40,41,43,45,47,48,50,52,53,55,57,59,60,62,64,65,67,69,71,72,74,76,77,79,81,83,84,86,88,89,91,93,95]
tecl_neg = [37,39,42,44,46,49,51,54,56,58,61,63,66,68,70,73,75,78,80,82,85,87,90,92,94]  
# x_tecl_neg = [ int(coord_nota_35[i]) for i in tecl_neg]

#carga imagen
img_tecl = pygame.image.load("img_tecla.png")

tecl_bla_img_size = (50,50)
tecl_neg_img_size = (30,50)

# funciones
#%% busqueda binaria
def busqueda_binaria(lista,x):
    
    '''
    Busca x en lista ordenada 
    devuelve True/False
 
    
 
    
    '''
 
    pos = False # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        
        medio = (izq + der) // 2
        
        if lista[medio] == x:
            pos = True    # elemento encontrado!
            
        
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    
    return pos


#%%  def midi file parse
def read_midi(file_midi_path):
    '''
    pre: toma midifile como parámetro y deben estar definidas en el entorno las variables SCREEN, ...(colores, coord_35, etc)
    post: ordena los datos para ser lanzados por "releser()"
    
    formato de salida = [nota,abre acumulado, cierra (ms),channel, 
                         Rect(left,top,width,height),
                         encendido(ms o pixeles, no se aún), apagado), Color figura(mano der/izq)]

        '''

    mid = MidiFile(file_midi_path) # EL archivo de entrada es un .mid que generé desde musecord y lo exporté como .mid
    
    MSJS = []
    abre_acu = 0 # esta en tick´s
    ultimo_delta_tiempo = 0 #cuando hay polifonía los msjs midi se pueden cerrar en un mismo tiempo varias notas. Solo la primer nota de ese tiempo acumulado lleva valor de duración , el resto no lo tiene
    for i, track in enumerate(mid.tracks[0]):
        
        if track.type == "note_on" and track.velocity > 0: #abre nota
            # agrego al msj nota, tiempo inicio y dejo espacio en 0 para completar con el track.time de cierre
            MSJS.append([track.note, track.time + abre_acu,0,track.channel])
            abre_acu += track.time
            
    
        if track.type == "note_on" and track.velocity == 0 and track.time != 0: #cierra nota con detalle de tiempo
            for j in MSJS: # busca el mensaje abierto e incompleto en elemento 2 para completarlo
                if j[0] == track.note and j[2] == 0:
                     j[2]= track.time
                     ultimo_delta_tiempo = track.time
                     break
         
        if track.type == "note_on" and track.velocity == 0 and track.time == 0: #cierra nota SIN detalle de tiempo
            for j in MSJS: # busca el mensaje abierto e incompleto en elemento 2 para completarlo
                if j[0] == track.note and j[2] == 0:
                    j[2] = ultimo_delta_tiempo
                    ultimo_delta_tiempo = 0
                    break
    
# le agrego pygame.rect a cada MSJ
    
    for i in MSJS:
        
        # if i[0] in tecl_neg:
        if busqueda_binaria(tecl_neg, i[0]):
            ancho_tecla = 16/26 * ANCHO_TECLA # ANCHO_TECLA es una variable en entorno con el ancho de la tecla blanca   
        else:
            ancho_tecla = ANCHO_TECLA
        
        # Rect(left, top, width, height) -> Rect
        # Rect(coord x, coord y , ancho figura, alto figura)
        
        i.append(pygame.Rect(coord_nota_35[i[0]]+1 , PIXELES_X_PULSO * PPM / 60000 * i[2]*-1, ancho_tecla-1, PIXELES_X_PULSO * PPM / 60000 * i[2]))                           

# le agrego el encendido a cada MSJ

    for i in MSJS:
        i.append(FINAL_RECORRIDO - i[4].height)   # encender
        i.append(i[2]) # para descontar en encender
        
    return MSJS        
        





#%%  def piano print sin encendido
# hago el piano   
def piano_bla(CANT_TECLAS_BL):
    '''
    pre: CANT_TECLAS_BL: cantidad de teclas blancas del teclado.
    post: imprime en screen el piano
    
    # esta función no la revisé , seguramente se puede optimizar y mejorar. Ojo , las relaciones se obtuvieron de un piano real  y todas estan ancladas a las variablea ANCHO_TECLA 

    '''
    X = 0
    for i in range (CANT_TECLAS_BL):
        pygame.draw.rect(screen,WHITE,(X+1,ALTO_PANTALLA-ALTO_TECLA,ANCHO_TECLA-1,ALTO_TECLA))
        
        X += ANCHO_TECLA


def piano_neg(CANT_TECLAS_BL):
    Z = 0   # se utiliza para determinar posición de las teclas en los bucles 
    for i in range((CANT_TECLAS_BL//7) + 1):
        pygame.draw.rect(screen,BLACK,(Z+12/23*ANCHO_TECLA,ALTO_PANTALLA-ALTO_TECLA, 16/23*ANCHO_TECLA,95/150*ALTO_TECLA)) # C#
        pygame.draw.rect(screen,BLACK,(Z+40/23*ANCHO_TECLA,ALTO_PANTALLA-ALTO_TECLA, 16/23*ANCHO_TECLA,95/150*ALTO_TECLA)) # D#
        pygame.draw.rect(screen,BLACK,(Z+80/23*ANCHO_TECLA,ALTO_PANTALLA-ALTO_TECLA, 16/23*ANCHO_TECLA,95/150*ALTO_TECLA)) # F#
        pygame.draw.rect(screen,BLACK,(Z+108/23*ANCHO_TECLA,ALTO_PANTALLA-ALTO_TECLA, 16/23*ANCHO_TECLA,95/150*ALTO_TECLA)) # G#
        pygame.draw.rect(screen,BLACK,(Z+136/23*ANCHO_TECLA,ALTO_PANTALLA-ALTO_TECLA, 16/23*ANCHO_TECLA,95/150*ALTO_TECLA)) # A#
        
        
        Z += ANCHO_TECLA * 7


#%%  def clase PrintNoteBla  y PrintNoteNeg
class PrintNoteBla():
    def __init__(self, note):
        self.note = note
        self.coord = coord_nota_35[note]
        self.tecl = "Blanca"
        self.encendido = False
        self.draw = pygame.Rect(self.coord,ALTO_PANTALLA-ALTO_TECLA, ANCHO_TECLA-1, ALTO_TECLA)
        self.color = WHITE
        
class PrintNoteNeg():
    def __init__(self, note):
        self.note = note
        self.coord = coord_nota_35[note]
        self.tecl = "Negra"
        self.encendido = False
        self.draw = pygame.Rect(self.coord, ALTO_PANTALLA - ALTO_TECLA, 16/23* ANCHO_TECLA,  95/150 * ALTO_TECLA)  
        self.color = BLACK
            
    
        
#%% creo diccionario de notas a encender


diccionario = {}
for i in tecl_bla:
    diccionario[i] = PrintNoteBla(i)
for i in tecl_neg:
    diccionario[i] = PrintNoteNeg(i)                

            
#%%  bucle principal

# pygame setup
pygame.init()
screen = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
clock = pygame.time.Clock()
running = True

MSJS = read_midi(file_midi_path)   

recorder = ScreenRecorder(ANCHO_PANTALLA,ALTO_PANTALLA,FPS  )


while running:
    for event in pygame.event.get(): # itera sobre cada evento (movimiento de mouse y precion de tecla)
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)

    
    
    
    if MSJS:
        if MSJS[0][1]*TICK <= pygame.time.get_ticks():
            
            lanzar.append(MSJS[0])
            MSJS.remove(MSJS[0])
            
    if lanzar:
        for i in lanzar:
            pygame.draw.rect(screen,BLUE,i[4])
            i[4].y += VELOCIDAD
            
            
            if i[4].top >= FINAL_RECORRIDO - i[4].height:
                
                diccionario[i[0]].color = GREEN

                        
            if i[4].top >= FINAL_RECORRIDO :
                if diccionario[i[0]].tecl == "Blanca":
                    diccionario[i[0]].color = WHITE
                else:
                    diccionario[i[0]].color = BLACK
                
                
            if i[4].top >= FINAL_RECORRIDO + (i[4].height ):
                lanzar.remove(i)
    
    for i in tecl_bla:
        pygame.draw.rect(screen,diccionario[i].color,diccionario[i].draw)
    for i in tecl_neg:
        pygame.draw.rect(screen,diccionario[i].color,diccionario[i].draw)        
    
    recorder.capture_frame(screen)
    
    # # flip() the display to put your work on screen
    pygame.display.update()
    pygame.display.flip() # siempre va antes de clock.tick() , no despues
    
    clock.tick(FPS)  # limits FPS to 60


# Stop the screen recording
recorder.end_recording()
pygame.quit()
    

#reproducir y grabar archivo de video tipo windows media player

