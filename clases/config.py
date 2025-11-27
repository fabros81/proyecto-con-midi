class Config:
    def __init__(self):
        self.ANCHO_PANTALLA = 1280
        self.ALTO_PANTALLA = 720
        self.PULSOS_PANTALLA = 5 # indica cuantos pulsos aparecen en la pantalla antes de ejecutarse.Ej 4, aparecen 4 tiempos en pantalla
        self.AJUSTE_TEMPO = 1 #valor porcentual. 1 = tempo original, 1.5 = 50% más rápido, 0.5 = 50% más lento
        self.COLORS = [(255,0,0), (0,0,255)]
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.GREEN = (0,255,0)
        self.RED = (255,0,0)
        self.BLUE = (0,0,255)
        self.FUXIA = (255,0,128)
        self.ORANGE = (255,165,0)
        self.COLORS = [self.RED,self.BLUE,self.ORANGE,self.FUXIA]
        # lo inicializa Teclado.py con el metodo ...
        self.FINAL_RECORRIDO = None
        # lo inicializa Mensajes.py con el metodo ...
        self.TICKS_PER_BEAT = None
        self.TEMPO = None
        self.PPM = None
        self.NUMERATOR = None
        self.DENOMINATOR = None
        self.CLOCK_PER_CLICK = None
        self.NOTATED_32ND_NOTES_PER_BEAT = None
        self.TIME = None
        
        
    def actualizar_tempo(self, nuevo_tempo):
        self.AJUSTE_TEMPO = nuevo_tempo
        
    def colors(self, channel):
        return self.COLORS[channel]
    
    def setFinalRecorrido(self,altoTeclaBlanca):
        self.FINAL_RECORRIDO = self.ALTO_PANTALLA - altoTeclaBlanca

    def setMetamsg(self,ticks, tempo, ppm, num, den, clock,notated32,time):
        self.TICKS_PER_BEAT = ticks
        self.TEMPO = tempo
        self.PPM = ppm
        self.NUMERATOR = num
        self.DENOMINATOR = den
        self.CLOCK_PER_CLICK = clock
        self.NOTATED_32ND_NOTES_PER_BEAT = notated32
        self.TIME = time