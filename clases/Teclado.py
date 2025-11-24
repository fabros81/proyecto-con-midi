from .Tecla import Tecla
from .Config import Config
import pygame

class Teclado:
    def __init__(self, ancho_pantalla, nota_min=36, nota_max=95):
        self.config = Config()
        self.coordenadaX , self.ancho_tecla = self._generar_mapa_teclas(ancho_pantalla,nota_min, nota_max)
        self.alto_tecla = self.ancho_tecla * 150/26
        self.teclas = self._crear_lista_teclas(nota_min, nota_max) 
    
    
    
    def _crear_lista_teclas(self, nota_min, nota_max):
        teclas = []
        for nota in range(nota_min, nota_max + 1):
            # Determinar color según tipo de tecla
            color = self.config.WHITE if nota % 12 in [0,2,4,5,7,9,11] else self.config.BLACK
            # Crear tecla y agregar a lista
            tecla = Tecla(nota, self.coordenadaX[nota], color)
            teclas.append(tecla)
        return teclas
    
    def _generar_mapa_teclas(self, ancho_pantalla, nota_min=21, nota_max=108):
        # Calcular ancho_tecla basado en el ancho de pantalla y cantidad de teclas blancas
        cant_teclas_blancas = len([n for n in range(nota_min, nota_max+1) 
                                if n % 12 in [0,2,4,5,7,9,11]])
        ancho_tecla = ancho_pantalla / cant_teclas_blancas
        
        mapa = {}
        patron_octava = [0, 12/23, 1, 40/23, 2, 3, 80/23, 4, 108/23, 5, 136/23, 6]
        
        for nota in range(nota_min, nota_max + 1):
            octava = (nota - 21) // 12
            tecla = (nota - 21) % 12
            x = (octava * 7 + patron_octava[tecla]) * ancho_tecla
            mapa[nota] = x
        
        return mapa, ancho_tecla
    
    def dibujar(self, pantalla):
        # Primero teclas blancas (altura completa)
        for tecla in self.teclas:
            if tecla.color == self.config.WHITE:
                y = pantalla.get_height() - self.alto_tecla
                pygame.draw.rect(pantalla, tecla.mostrarColor, 
                            (tecla.coord, y, self.ancho_tecla, self.alto_tecla))
    
        # Luego teclas negras (más pequeñas y cortas)
        for tecla in self.teclas:
            if tecla.color == self.config.BLACK:
                ancho_neg = self.ancho_tecla * 0.6    # 60% ancho
                alto_neg = self.alto_tecla * 0.6      # 60% alto  
                y_neg = pantalla.get_height() - alto_neg  # Misma base
                pygame.draw.rect(pantalla, tecla.mostrarColor, 
                            (tecla.coord, y_neg, ancho_neg, alto_neg))           
             