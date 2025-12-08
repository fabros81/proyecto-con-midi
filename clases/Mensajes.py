import pygame
from .Nota import Nota

class Mensajes:
    def __init__(self,config,archivo, teclado):
        self.c = config
        self.mid = archivo.mid
        self.t = teclado
        self.msj1 = self._msj(self.mid)# lista de objetos Nota
        self.lanzar = []
        
    
    # toma cada mensaje de Archivo.mi lo mete en una instancia de Nota y genera las 4 listas de reproducción.
    def printMsj1(self): 
        print(self.msj1)
        '''
        for s in range(0,4):
            for i in self.msj1[s]:
                print(f"canal/indice{s}: {i}")
        '''
        quit()
    
        
    def ticks_a_ms(self, ticks_midi):
        """Convierte ticks MIDI a milisegundos con ajuste de tempo"""
        microsegundos_por_pulso = self.c.TEMPO / self.c.TICKS_PER_BEAT
        # APLICAR AJUSTE DE TEMPO
        factor_ajuste = self.c.AJUSTE_TEMPO/100
        milisegundos_por_tick = (microsegundos_por_pulso / 1000.0) * factor_ajuste
        return ticks_midi * milisegundos_por_tick
    
            
    def _msj(self,mid):
        '''
        pre: toma self.file_name como parámetro
        post: ordena los datos para ser dibujados en 1 lista de mensajes con el channel aclarado
        
        formato de salida = [nota,abre acumulado, cierra (ms),channel, 
                            Rect(left,top,width,height),
                            encendido(ms o pixeles, no se aún), apagado), Color figura(mano der/izq)]
        '''
             
        
        if len(self.mid.tracks) >4:
            raise "El máximo de canales permitido es 4. Ajuste el archivo"
        
        
        MSJS = {0:[],1:[],2:[],3:[]}
        for s in range (len(self.mid.tracks)):
            abre_acu = [0,0,0,0] # esta en tick´s
            ultimo_delta_tiempo = 0 #cuando hay polifonía los msjs midi se pueden cerrar en un mismo tiempo varias notas. Solo la primer nota de ese tiempo acumulado lleva valor de duración , el resto no lo tiene
            for i, track in enumerate(self.mid.tracks[s]):
                
                if track.is_meta and track.type == 'time_signature':
                        msj = ['time_signature',track.numerator,track.denominator, track.clocks_per_click, track.notated_32nd_notes_per_beat]
                        abre_acu[s] += track.time
                        MSJS[s].append(msj)
                        self.c.setTimeSignature(track.numerator,track.denominator,track.clocks_per_click,track.notated_32nd_notes_per_beat)
                        
                        
                if track.is_meta and track.type == "set_tempo":
                        msj = ['set_tempo', track.tempo]
                        abre_acu[s] += track.time
                        MSJS[s].append(msj)
                        self.c.setConstantes(track.tempo)
                        
                        
                
                if track.type == "note_on" and track.velocity > 0: #abre nota
                    # agrego al msj nota, tiempo inicio y dejo espacio en 0 para completar con el track.time de cierre
                    MSJS[s].append([track.note, track.time + abre_acu[s],0,track.channel])
                    abre_acu[s] += track.time
                    
            
                if track.type == "note_on" and track.velocity == 0 and track.time != 0: #cierra nota con detalle de tiempo
                    for j in MSJS[s]: # busca el mensaje abierto e incompleto en elemento 2 para completarlo
                        if j[0] == track.note and j[2] == 0:
                            j[2]= track.time
                            abre_acu[s] += track.time
                            #ultimo_delta_tiempo = track.time
                            
                
                if track.type == "note_on" and track.velocity == 0 and track.time == 0: #cierra nota SIN detalle de tiempo
                    for j in MSJS[s]: # busca el mensaje abierto e incompleto en elemento 2 para completarlo
                        if j[0] == track.note and j[2] == 0:
                            j[2] = ultimo_delta_tiempo
                            ultimo_delta_tiempo = 0
                            
                if track.is_meta and track.type == 'end_of_track':
                    abre_acu[s] +=  track.time
                    
                

            # le agrego pygame.rect a cada MSJ
            
            for i in MSJS[s]:
                
                if type(i[0]) == str:
                    pass
                else:
                    
                    # Rect(left, top, width, height) -> Rect
                    # Rect(coord x, coord y , ancho figura, alto figura)
                    if i[0] % 12 in [0,2,4,5,7,9,11]:
                        i.append(pygame.Rect(self.c.COORDENADAX[i[0]]+1 , self.c.PIXELES_X_BEAT * -( i[2]/self.c.TICKS_PER_BEAT), self.c.ANCHO_TECLA_BLANCA -1, self.c.PIXELES_X_BEAT * ( i[2]/self.c.TICKS_PER_BEAT)))
                        
                    else:
                        i.append(pygame.Rect(self.c.COORDENADAX[i[0]]+1 , self.c.PIXELES_X_BEAT * -( i[2]/self.c.TICKS_PER_BEAT), self.c.ANCHO_TECLA_NEGRA -1, self.c.PIXELES_X_BEAT * ( i[2]/self.c.TICKS_PER_BEAT)))
            
            # le agrego el valor de encendido a cada MSJ. Tiene que ser FINAL_RECORRIDO - el alto del rect

            for i in MSJS[s]:
                if type(i[0]) == str:
                    continue
                else:
                    i.append(self.c.FINAL_RECORRIDO - i[4].height)   # encender
                    #i.append(i[2]) # para descontar en encender
           
        
        return MSJS
        
    def dibujar(self,pantalla):
        # ajustar metamensaje que cambian variables en tiempo de ejecución. Estos mensajes son != a clase Nota, son una lista
        
        
        for i in range (0,4):
            if (len(self.msj1[i]) >0):
                                
                if self.msj1[i][0][0] == 'time_signature':
                    self.c.setTimeSignature(self.msj1[i][1],self.msj1[i][2],self.msj1[i][3],self.msj1[i][4])
                    self.msj1[i].pop(0)
                    continue
                
                if self.msj1[i][0][0] == 'set_tempo':
                    self.c.setConstantes(self.msj1[i][0][1])
                    self.msj1[i].pop(0)
                    continue
                
                if type(self.msj1[i][0][0]) != str and  self.msj1[i][0][1] <= (pygame.time.get_ticks()- self.c.TIEMPO_INICIO)* self.c.AJUSTE_TEMPO/100:
                    self.lanzar.append(self.msj1[i][0])               
                    self.msj1[i].pop(0)
        for j in self.lanzar:
            pygame.draw.rect(pantalla, self.c.COLORS[i], j[4])

    
        
    def actualizar(self):
        
        for i in self.lanzar: # se lanzan objetos notas
            i[4].y += self.c.PPS * self.c.DT_s
            if i[4].bottom >= self.c.FINAL_RECORRIDO:
                self.t.Encender(i.nota)
                
            if i[4].y > self.c.FINAL_RECORRIDO :
                self.t.Apagar(i[0])
                self.lanzar.remove(i)
            
            
    def channels(self):
        n = 0
        for i in range (len(self.mid.tracks)):
            print(n)
            #print(len(self.mid.tracks))
            n +=1
        quit()    
            

        
        

        