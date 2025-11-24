# -*- coding: utf-8 -*-
"""
falta:
- implementar en POO para 1 channel
- lograr que funcione con 4 channels como entrada maximo , no polifónico
- logra que funcione para midi polifónico
- el height del rect es chico, ver como agrandarlo
- ver si se puede agregarle música desde pygame directamente
"""
#%%  path cancion

file_midi_path = "./archivos midi/fc.mid"
#file_midi_path = "./archivos midi/saxo_1_mano_miqueas_6_8.mid"
#file_midi_path = "./archivos midi/voz_saxo_miqueas_6_8.mid"


import pygame
from mido import MidiFile
import time


# variables constantes     

pase = True
ANCHO_PANTALLA = 1280    
ALTO_PANTALLA = 720 
#colores en rgb
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
FUXIA = (255,0,128)
ORANGE = (255,165,0)
COLORS = [RED,BLUE,ORANGE,FUXIA]
# cantidad de teclas blancas : 35 (desde nota 36 a 95)
CANT_TECLAS_BL = 35  # OJO CON CAMBIARLA!!!!! vas a tener que revisar el diccionario con las coordenadas para la nueva cantidad de teclas, no probé si funciona para otra cantidad de teclas
MIN_MAX_TECLA = [36,95] # indica el primer y último número de tecla del piano
ANCHO_TECLA = ANCHO_PANTALLA / CANT_TECLAS_BL
ALTO_TECLA = ANCHO_TECLA*150/26
# si son 35 teclas blancas, arrancando de La 50 a la 85
FINAL_RECORRIDO = 509 # intenté poner algo asi como alto_pantalla-alto_tecla-nota.height, pero no funcionaba. Usmeando encontré que solo reconocía numeros enteros pares.
# de hecho si asignas a FINAL_RECORRIDO un número impar no funciona. No se porqué todavía.
t_inicio =0


#**********Meta mensajes**************
# MidiFil(type=1, ticks_per_beat=480, tracks=etc.)

TICKS_PER_BEAT = 0 #ticks_per_beat de los metamensajes
# 'time_signature'
NUMERATOR =1
DENOMINATOR = 4
CLOCK_PER_CLICK= 0
NOTATED_32ND_NOTES_PER_BEAT=0
TIME=0 # Time del metamensaje 'time_signature' unicamente

# 'key_signature' para cambio de clave. no los hice, no se para que me pueden servir
# KEY = F
# TIME = 0 

# 'set_tempo'
TEMPO = 0 #una funcion los define a partir de los metamensajes
# TIME=0 # tiempo en que cambia el tempo

# 'control_change' no lo uso por ahora
# 'midi_port' no lo uso por ahora
#*********** fin de metamensajes ************************

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!! PARAMETROS DE CONTROL!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
PULSOS_EN_PANTALLA = 5 # indica cuantos pulsos aparecen en la pantalla antes de ejecutarse.Ej 4, aparecen 4 tiempos en pantalla
AJUSTE_TEMPO_PORCENTAJE = 100  # 100 = tempo original, 150 = 50% más rápido, 50 = 50% más lento
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
PIXELES_X_PULSO = (ALTO_PANTALLA-ALTO_TECLA)/PULSOS_EN_PANTALLA # alto de la negra en pixeles


PPM = 0 # BPM una funcion lo calcula a partir de los metamensajes
lanzar = []
a_encender = []


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
x_tecl_neg = [ int(coord_nota_35[i]) for i in tecl_neg]


# funciones

def read_metamsg(file):
    '''
    Ajusta los parámetros default a los que provee el midi file
    '''
    global TICKS_PER_BEAT
    global TEMPO
    global PPM
    
    global NUMERATOR
    global DENOMINATOR
    global CLOCK_PER_CLICK
    global NOTATED_32ND_NOTES_PER_BEAT
    global TIME
    
    mid = MidiFile(file)
    TICKS_PER_BEAT = mid.ticks_per_beat
    for i,track in enumerate (mid.tracks):
        if i==0:
            for msg in track:
                if msg.type == "set_tempo":
                    TEMPO = msg.tempo           
                    PPM = 60000000 / TEMPO
                if msg.is_meta and msg.type == 'time_signature':
                    NUMERATOR = msg.numerator
                    DENOMINATOR = msg.denominator
                    CLOCK_PER_CLICK = msg.clocks_per_click
                    NOTATED_32ND_NOTES_PER_BEAT = msg.notated_32nd_notes_per_beat
                    TIME = msg.time
            
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
                     abre_acu += track.time
                     #ultimo_delta_tiempo = track.time
                     break
         
        if track.type == "note_on" and track.velocity == 0 and track.time == 0: #cierra nota SIN detalle de tiempo
            for j in MSJS: # busca el mensaje abierto e incompleto en elemento 2 para completarlo
                if j[0] == track.note and j[2] == 0:
                    j[2] = ultimo_delta_tiempo
                    ultimo_delta_tiempo = 0
                    break
        if track.is_meta and track.type == 'end_of_track':
            ## aca tengo que hacer algo porque cambia de channel
            abre_acu = 0
    
# le agrego pygame.rect a cada MSJ
    
    for i in MSJS:
        
        if i[0] in tecl_neg:
            ancho_tecla = 16/26 * ANCHO_TECLA # ANCHO_TECLA es una variable en entorno con el ancho de la tecla blanca   
        else:
            ancho_tecla = ANCHO_TECLA
        
        # Rect(left, top, width, height) -> Rect
        # Rect(coord x, coord y , ancho figura, alto figura)
        
        i.append(pygame.Rect(coord_nota_35[i[0]]+1 , PIXELES_X_PULSO * -( i[2]/TICKS_PER_BEAT), ancho_tecla-1, PIXELES_X_PULSO * ( i[2]/TICKS_PER_BEAT)))                           

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



# funciones debug

def printConstantes():
    global FINAL_RECORRIDO
    global TICKS_PER_BEAT
    global TEMPO
    global PPM
    
    global NUMERATOR
    global DENOMINATOR
    global CLOCK_PER_CLICK
    global NOTATED_32ND_NOTES_PER_BEAT
    global TIME
    global RECORRIDO 
    global TIEMPO_POR_SEGUNDO
    global PPS 

    print(f"""
          Final recorrido:            {FINAL_RECORRIDO}
          Pixeles por negra:          {PIXELES_X_PULSO}
          Tempo:                      {TEMPO}          
          PPM:                        {PPM}          
          Ticks_per_beat: (por negra) {TICKS_PER_BEAT}  
          numerador:                  {NUMERATOR}        
          denominador:                {DENOMINATOR}
          clock_per_click:            {CLOCK_PER_CLICK}
          notated_32nd_notes_per_beat {NOTATED_32ND_NOTES_PER_BEAT}
          time: ('time_signature')    {TIME}
          recorrido (pix)             {RECORRIDO}   
          tiempo por segundo          {SEGUNDOS_POR_PULSO} 
          pps                         {PPS}
          """       
    )
 
def getMSJS(f):
    for i in f:
        print(i)
        
def showOnlyRawMidi(argumento = None):
    if argumento == None:
        mid = MidiFile(file_midi_path)
        print(f"archivo: {file_midi_path}")
        print(mid)
        quit()
    if argumento == "note_on":
        mid = MidiFile(file_midi_path)
        print(f"archivo: {file_midi_path}")
        for i, track in enumerate(mid.tracks[0]):
            if track.type == "note_on":
                print(track)
        quit()
        
#%%  bucle principal
#showOnlyRawMidi() #imprime en consola los mensajes crudos y finaliza el código

def ticks_a_milisegundos(ticks_midi):
    """Convierte ticks MIDI a milisegundos con ajuste de tempo"""
    microsegundos_por_pulso = TEMPO / TICKS_PER_BEAT
    # APLICAR AJUSTE DE TEMPO
    factor_ajuste = 100.0 / AJUSTE_TEMPO_PORCENTAJE
    milisegundos_por_tick = (microsegundos_por_pulso / 1000.0) * factor_ajuste
    return ticks_midi * milisegundos_por_tick

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
    dt_ms = reloj.tick(60)
    dt_s = dt_ms/1000
    
    
    for event in pygame.event.get(): # itera sobre cada evento (movimiento de mouse y precion de tecla)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
    
            if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:  # Tecla +
                AJUSTE_TEMPO_PORCENTAJE = min(200, AJUSTE_TEMPO_PORCENTAJE + 10)  # Máximo 200%
                print(f"Velocidad: {AJUSTE_TEMPO_PORCENTAJE}%")
                
            elif event.key == pygame.K_MINUS:  # Tecla -
                AJUSTE_TEMPO_PORCENTAJE = max(25, AJUSTE_TEMPO_PORCENTAJE - 10)  # Mínimo 25%
                print(f"Velocidad: {AJUSTE_TEMPO_PORCENTAJE}%")
                
            elif event.key == pygame.K_0:  # Tecla 0 para reset
                AJUSTE_TEMPO_PORCENTAJE = 100
                print("Velocidad: 100% (Normal)")            
            
        
    screen.fill(BLACK)

    if MSJS:
        for i in MSJS:        
            '''
            if MSJS[0][1] <= (pygame.time.get_ticks() - tInicio):
                lanzar.append(MSJS[0])
                MSJS.remove(MSJS[0])
            else: 
                break
            '''
            if ticks_a_milisegundos(MSJS[0][1]) <= (pygame.time.get_ticks() - tInicio): # me corria al doble de tempo. La ia, me encontro ese error de unidades. no lo entendí todavía
                lanzar.append(MSJS[0])
                MSJS.remove(MSJS[0])
            else: 
                break
            
    if lanzar:
        for i in lanzar:
            pygame.draw.rect(screen,COLORS[3],i[4])
            i[4].y += PPS  * dt_s
            
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
    
    
    
    # # flip() the display to put your work on screen
    pygame.display.update()
    pygame.display.flip() # siempre va antes de clock.tick() , no despues
    

pygame.quit()
    

#reproducir y grabar archivo de video tipo windows media player


