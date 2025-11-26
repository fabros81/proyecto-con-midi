from .Tecla import Tecla
from .Config import Config
import pygame

class Teclado:
    def __init__(self, ancho_pantalla, nota_min=21, nota_max=108):
        if nota_min < 21 or nota_max >108 or nota_min % 12 not in [0,2,4,5,7,9,11] or nota_max % 12 not in [0,2,4,5,7,9,11]:
            raise "rango de teclado inválido. Rango debe estar contenido entre 21 y 108. Además, tienen que ser notas Blancas"
        self.config = Config()
        self.ancho_tecla_blanca =self._calcular_ancho_tecla_blanca(ancho_pantalla,nota_min,nota_max)
        self.coordenadaX_blancas, self.coordenadaX_negras = self._generar_mapa_teclas(nota_min, nota_max)
        self.ancho_tecla_negra = 16/26 * self.ancho_tecla_blanca
        self.alto_tecla_blanca = self.ancho_tecla_blanca * 150/26
        self.alto_tecla_negra = self.alto_tecla_blanca *95/150
        #self.teclas = self._crear_lista_teclas(nota_min, nota_max) 
               
    def _calcular_ancho_tecla_blanca(self,ancho_pantalla, nota_min,nota_max):
        cant_teclas_blancas = len([n for n in range(nota_min, nota_max+1) if n % 12 in [0,2,4,5,7,9,11]])
        ancho_tecla = ancho_pantalla / cant_teclas_blancas
        return ancho_tecla
    
    def _generar_mapa_teclas(self, nota_min =21, nota_max =108):
        mapa_blanco = {}
        mapa_negro = {}
        patron_octava = [0, 12/23, 1, 40/23, 2, 3, 80/23, 4, 108/23, 5, 136/23, 6]
        for nota in range (nota_min,nota_max +1):
            #teclas_blancas = [n for n in range(nota_min, nota_max+1) if n % 12 in [0,2,4,5,7,9,11]]
            octava = (nota - nota_min)  // 12
            pos = (nota - nota_min) % 12
            x = octava *(7* self.ancho_tecla_blanca) + self.ancho_tecla_blanca * patron_octava[pos]
            if nota % 12 in [0,2,4,5,7,9,11]:
                mapa_blanco[nota] = int(x)
            else:
                mapa_negro[nota] = int(x)
            print(f"nota: {nota}, octava: {octava}, x:{x} ")
                
        print(f"mapa completo: {mapa_blanco}")        
        print(f"mapa completo: {mapa_negro}")        
        return mapa_blanco, mapa_negro 
        
    '''
    def _crear_lista_teclas(self, nota_min, nota_max):
        teclas = []
        for nota in range(nota_min, nota_max + 1):
            # Determinar color según tipo de tecla
            color = self.config.WHITE if nota % 12 in [0,2,4,5,7,9,11] else self.config.BLACK
            # Crear tecla y agregar a lista
            tecla = Tecla(nota, self.coordenadaX[nota], color)
            teclas.append(tecla)
        return teclas
    '''


    def dibujar(self, pantalla):
        # Teclas blancas
        for tecla in self.teclas:
            if tecla.color == self.config.WHITE:
                x = int(tecla.coord)
                y = int(pantalla.get_height() - self.alto_tecla)
                ancho = int(self.ancho_tecla)
                alto = int(self.alto_tecla)
                pygame.draw.rect(pantalla, tecla.mostrarColor, (x, y, ancho, alto))
        
        # Teclas negras (más pequeñas)
        for tecla in self.teclas:
            if tecla.color == self.config.BLACK:
                x = int(tecla.coord)
                y = int(pantalla.get_height() - self.alto_tecla * 0.6)  # Más cortas
                ancho = int(self.ancho_tecla * 0.6)
                alto = int(self.alto_tecla * 0.6)
                pygame.draw.rect(pantalla, tecla.mostrarColor, (x, y, ancho, alto))
                
    def printCoordX(self):
        print(self.ancho_tecla_blanca)
        print("inicia")
        for i in self.coordenadaX:
            print(i) 
        print("termina")        
                