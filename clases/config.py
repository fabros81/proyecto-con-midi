import pygame

class Config:
    def __init__(self):
        self.ANCHO_PANTALLA = 1280
        self.ALTO_PANTALLA = 720
        self.PULSOS_PANTALLA = 5 # indica cuantos pulsos aparecen en la pantalla antes de ejecutarse.Ej 4, aparecen 4 tiempos en pantalla
        self.AJUSTE_TEMPO = 75  #valor porcentual. 1 = tempo original, 1.5 = 50% más rápido, 0.5 = 50% más lento
        self.COLORS = [(255,0,0), (0,0,255)]
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.GREEN = (0,255,0)
        self.RED = (255,0,0)
        self.BLUE = (0,0,255)
        self.FUXIA = (255,0,128)
        self.ORANGE = (255,165,0)
        self.COLORS = [self.RED,self.FUXIA,self.ORANGE,self.BLUE]
        # lo inicializa Archivo.py con el metodo ...
        self.TICKS_PER_BEAT = None
                
        
        # lo inicializa Teclado.py con el metodo ...
        self.FINAL_RECORRIDO = None
        self.PIXELES_X_BEAT = None
        self.COORDENADAX = None
        self.ANCHO_TECLA_BLANCA = None
        self.ALTO_TECLA_BLANCA = None
        self.ANCHO_TECLA_NEGRA = None
        
        
        # lo inicializa Mensajes.py con el metodo ...
        # setTimeSignature
        self.NUMERATOR = None
        self.DENOMINATOR = None
        self.CLOCK_PER_CLICK = None
        self.NOTATED_32ND_NOTES_PER_BEAT = None
        
        #setTempo
        self.TEMPO = None #60,000,000 / 
        self.BPM = None
                
        self.TIEMPO_INICIO = None
        self.DT_ms = None
        self.DT_s = None
        self.PPS = None #velocidad de caida de notas
        
    #def actualizar_tempo(self, nuevo_tempo):
    #    self.AJUSTE_TEMPO = nuevo_tempo
        
    def colors(self, channel):
        return self.COLORS[channel]
    
    def setFinalRecorrido(self):
        self.FINAL_RECORRIDO = self.ALTO_PANTALLA - self.ALTO_TECLA_BLANCA

    # msj = ['time_signature',track.numerator,track.denominator, track.clocks_per_click, track.notated_32nd_notes_per_beat]
    def setTimeSignature(self,num, den, clock, notated32):
        self.NUMERATOR = num
        self.DENOMINATOR = den
        self.CLOCK_PER_CLICK = clock
        self.NOTATED_32ND_NOTES_PER_BEAT = notated32

    def setConstantes(self, tempo):
        self.TEMPO = tempo
        self.BPM = 60000000 / self.TEMPO
        self.PPS = self.FINAL_RECORRIDO / ((60.0 / self.BPM) * (100.0 / self.AJUSTE_TEMPO) * self.PULSOS_PANTALLA)
            
    def setAnchoTecla(self, ancho_bla, ancho_neg):
        self.ANCHO_TECLA_BLANCA = ancho_bla
        self.ANCHO_TECLA_NEGRA = ancho_neg
    def setAltoTeclaBlanca(self,alto):
        self.ALTO_TECLA_BLANCA = alto
        
    def setTickPerBeat(self,tick) :
        self.TICKS_PER_BEAT = tick
    
    def setPixelesPorPulso(self):
        self.PIXELES_X_BEAT = int((self.ALTO_PANTALLA - self.ALTO_TECLA_BLANCA)/ self.PULSOS_PANTALLA)
        
    def setCoordenadaX(self,coordx):
        self.COORDENADAX = coordx
        
    def setTiempoInicio(self):
        self.TIEMPO_INICIO = pygame.time.get_ticks()
        
    def dt(self,reloj):
        self.DT_ms = reloj.tick(60)
        self.DT_s = self.DT_ms /1000
        
    
        
    def verAtributosEnNone(self):
        for attr, value in vars(self).items():
            if value is None:
                print(f"!!!!!!!!!!!!!!!!!!⚠️ {attr} es None!!!!!!!!!!!!!!!!!!!!!!!!!")
            else:
                print(f"{attr}: {value}") 
                
        quit()
    