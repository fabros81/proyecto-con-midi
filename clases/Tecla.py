from .Config import Config

class Tecla():
    def __init__(self, note,coord_nota, color):
        self.note = note
        self.coord = coord_nota
        self.encendido = False
        self.color = color
        self.mostrarColor = self.color
        self.config = Config()
        
    def setEncender(self):
        self.mostrarColor = self.config.GREEN
        
    def setApagar(self):
        self.mostrarColor = self.color
        
    