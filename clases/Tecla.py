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
    
    def set_rect(self,y):
        objeto_rect = pygame.Rect(self.coordX,y, self.ancho, self.alto)
        self.rect = objeto_rect 
                
    def Encender(self):
        self.mostrarColor = self.config.GREEN
        
    def Apagar(self):
        self.mostrarColor = self.color
        
    