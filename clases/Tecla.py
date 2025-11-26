from .Config import Config
import pygame

class Tecla():
    def __init__(self, note,x,ancho,alto, color):
        self.note = note
        self.coordX = x
        self.ancho = ancho
        self.alto = alto
        self.encendido = False
        self.color = color
        self.mostrarColor = self.color
        self.config = Config()
        self.rect = None
    
    def set_rect(self, x, y, ancho, alto):
        self.rect = pygame.Rect(x, y, ancho, alto)
                
    def setEncender(self):
        self.mostrarColor = self.config.GREEN
        
    def setApagar(self):
        self.mostrarColor = self.color
        
    