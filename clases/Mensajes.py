import pygame
from .Nota import Nota

class Mensajes:
    def __init__(self,config,archivo, teclado):
        self.c = config
        self.mid = archivo.mid
        self.t = teclado
        self.msj1 = self._msj(self.mid)# lista de objetos Nota
        self.lanzar = []
        self._read_metamsg(self.mid)        
    
    # toma cada mensaje de Archivo.mi lo mete en una instancia de Nota y genera las 4 listas de reproducción.
    def printMsj1(self): 
        for i in self.msj1:
            print(i.nota)
    
    def ticks_a_ms(self, ticks_midi):
        """Convierte ticks MIDI a milisegundos con ajuste de tempo"""
        microsegundos_por_pulso = self.c.TEMPO / self.c.TICKS_PER_BEAT
        # APLICAR AJUSTE DE TEMPO
        factor_ajuste = self.c.AJUSTE_TEMPO/100
        milisegundos_por_tick = (microsegundos_por_pulso / 1000.0) * factor_ajuste
        return ticks_midi * milisegundos_por_tick
    
    def _read_metamsg(self, mid):
        '''
        Ajusta los parámetros default a los que provee el midi file en config
        '''
             
        mid = self.mid
        TICKS_PER_BEAT = mid.ticks_per_beat
        TEMPO = 0
        PPM = 0
        NUMERATOR = 0
        DENOMINATOR = 0
        CLOCK_PER_CLICK = 0
        NOTATED_32ND_NOTES_PER_BEAT = 0
        TIME = 0
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
        self.c.setMetamsg(TICKS_PER_BEAT,TEMPO,PPM,NUMERATOR,DENOMINATOR,CLOCK_PER_CLICK,NOTATED_32ND_NOTES_PER_BEAT,TIME)
            
    def _msj(self,mid):
        '''
        pre: toma self.file_name como parámetro
        post: ordena los datos para ser dibujados en las 4 listas de mensajes [msj1, msj2,msj3,msj4]
        
        formato de salida = [nota,abre acumulado, cierra (ms),channel, 
                            Rect(left,top,width,height),
                            encendido(ms o pixeles, no se aún), apagado), Color figura(mano der/izq)]
        '''
             
        
        if len(self.mid.tracks) >4:
            raise "El máximo de canales permitido es 4. Ajuste el archivo"
        # ACA HAY QUE HACER UN FOR PARA QUE ITERE SOBRE LOS 4 CHANNELS DISPONIBLES. o que en un msj solo entren todos los canales
                
        salida =[]
        MSJS = []
                
        abre_acu = 0 # esta en tick´s
        ultimo_delta_tiempo = 0 #cuando hay polifonía los msjs midi se pueden cerrar en un mismo tiempo varias notas. Solo la primer nota de ese tiempo acumulado lleva valor de duración , el resto no lo tiene
        for i, track in enumerate(self.mid.tracks[0]):
            
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
            # Rect(left, top, width, height) -> Rect
            # Rect(coord x, coord y , ancho figura, alto figura)
            if i[0] % 12 in [0,2,4,5,7,9,11]:
                i.append(pygame.Rect(self.c.COORDENADAX[i[0]]+1 , self.c.PIXELES_X_PULSO * -( i[2]/self.c.TICKS_PER_BEAT), self.c.ANCHO_TECLA_BLANCA -1, self.c.PIXELES_X_PULSO * ( i[2]/self.c.TICKS_PER_BEAT)))
            else:
                i.append(pygame.Rect(self.c.COORDENADAX[i[0]]+1 , self.c.PIXELES_X_PULSO * -( i[2]/self.c.TICKS_PER_BEAT), self.c.ANCHO_TECLA_NEGRA -1, self.c.PIXELES_X_PULSO * ( i[2]/self.c.TICKS_PER_BEAT)))
        
        # le agrego el valor de encendido a cada MSJ. Tiene que ser FINAL_RECORRIDO - el alto del rect

        for i in MSJS:
            i.append(self.c.FINAL_RECORRIDO - i[4].height)   # encender
            #i.append(i[2]) # para descontar en encender
        
        
        
        for i in MSJS:
            n = Nota(i[0],i[1],i[2],i[3],i[4],i[5],self.c.BLUE)
            
            salida.append(n)
        
            
        return salida        
        
    def dibujar(self,pantalla):
        if (len(self.msj1) >0):
            if self.ticks_a_ms(self.msj1[0].abreAcu) <= (pygame.time.get_ticks()- self.c.TIEMPO_INICIO):
                self.lanzar.append(self.msj1[0])               
                self.msj1.remove(self.msj1[0])
        for i in self.lanzar:
            pygame.draw.rect(pantalla, self.c.RED, i.objeto)
        
    def actualizar(self):
        for i in self.lanzar: # se lanzan objetos notas
            i.objeto.y += 5
            if i.objeto.bottom >= self.c.FINAL_RECORRIDO:
                self.t.Encender(i.nota)
                
            if i.objeto.y > self.c.FINAL_RECORRIDO :
                self.t.Apagar(i.nota)
                self.lanzar.remove(i)
            
            
        
            
            
            
        
        

        