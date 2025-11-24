class Config:
    def __init__(self):
        self.ANCHO_PANTALLA = 1280
        self.ALTO_PANTALLA = 720
        self.PULSOS_PANTALLA = 5 # indica cuantos pulsos aparecen en la pantalla antes de ejecutarse.Ej 4, aparecen 4 tiempos en pantalla
        self.AJUSTE_TEMPO = 100 #valor porcentual. 100 = tempo original, 150 = 50% más rápido, 50 = 50% más lento
        self.COLORS = [(255,0,0), (0,0,255)]
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.GREEN = (0,255,0)
        self.RED = (255,0,0)
        self.BLUE = (0,0,255)
        self.FUXIA = (255,0,128)
        self.ORANGE = (255,165,0)
        self.COLORS = [self.RED,self.BLUE,self.ORANGE,self.FUXIA]
    
    def actualizar_tempo(self, nuevo_tempo):
        self.AJUSTE_TEMPO = nuevo_tempo
        
    def colors(self, channel):
        return self.COLORS[channel]