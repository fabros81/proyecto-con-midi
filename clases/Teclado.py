from .Tecla import Tecla

import pygame

class Teclado:
    def __init__(self, config , nota_min=21, nota_max=108):
        if nota_min not in [24, 36, 48, 60, 72, 84, 96, 108 ] or nota_max >108 or  nota_max % 12 not in [0,2,4,5,7,9,11] :
            raise "rango de teclado inválido. nota minima tiene que ser una de las siguientes [24, 36, 48, 60, 72, 84, 96, 108].La nota máxima es < 108"
        self.config = config
        self.ancho_tecla_blanca =self._calcular_ancho_tecla_blanca(config.ANCHO_PANTALLA, nota_min,nota_max)
        self.coordenadaX = self._generar_mapa_teclas(nota_min, nota_max)
        self.ancho_tecla_negra = int(16/26 * self.ancho_tecla_blanca)
        self.alto_tecla_blanca = int(self.ancho_tecla_blanca * 150/26)
        self.alto_tecla_negra = int(self.alto_tecla_blanca *95/150)
        self.config.setAnchoTecla(self.ancho_tecla_blanca,self.ancho_tecla_negra)
        self.config.setAltoTeclaBlanca(self.alto_tecla_blanca)
        self.config.setFinalRecorrido()
        self.teclas_blancas, self.teclas_negras = self._crear_lista_teclas(nota_min, nota_max) #no cambiar el orden , esta encadenado con otros procesos
        self.config.setPixelesPorPulso()
        self.config.setCoordenadaX(self.coordenadaX)               
    def _calcular_ancho_tecla_blanca(self,ancho_pantalla, nota_min,nota_max):
        cant_teclas_blancas = len([n for n in range(nota_min, nota_max+1) if n % 12 in [0,2,4,5,7,9,11]])
        ancho_tecla = ancho_pantalla / cant_teclas_blancas
        return int(ancho_tecla)
    
    def _generar_mapa_teclas(self, nota_min =21, nota_max =108):
        mapa = {}
        patron_octava = [0, 12/23, 1, 40/23, 2, 3, 80/23, 4, 108/23, 5, 136/23, 6]
        for nota in range (nota_min,nota_max +1):
            
            octava = (nota - nota_min)  // 12
            pos = (nota - nota_min) % 12
            x = octava *(7* self.ancho_tecla_blanca) + (self.ancho_tecla_blanca * patron_octava[pos])
            mapa[nota] = int(x)
                   
        
        return mapa
        
    def _crear_lista_teclas(self, nota_min, nota_max):
        teclas_blancas = {}
        teclas_negras = {}
        for nota in range(nota_min, nota_max + 1):
            
            if nota % 12 in [0,2,4,5,7,9,11]:
                color = self.config.WHITE
                t = Tecla(nota, self.coordenadaX[nota],self.ancho_tecla_blanca-1,self.alto_tecla_blanca, color)
                t.set_rect(self.config.FINAL_RECORRIDO)
                teclas_blancas[nota] = t
                
            else :
                color = self.config.BLACK
                t = Tecla(nota, self.coordenadaX[nota],self.ancho_tecla_negra,self.alto_tecla_negra, color)
                t.set_rect(self.config.FINAL_RECORRIDO)
                teclas_negras[nota] = t
        return teclas_blancas, teclas_negras
    
    def dibujar(self, pantalla):
        # Teclas blancas
        for tecla in self.teclas_blancas:
            pygame.draw.rect(pantalla, self.teclas_blancas[tecla].mostrarColor, self.teclas_blancas[tecla].rect) #!!!!!!!!!!!!!
        
        # Teclas negras (más pequeñas)
        for tecla in self.teclas_negras:
            pygame.draw.rect(pantalla, self.teclas_negras[tecla].mostrarColor, self.teclas_negras[tecla].rect)
                
    
    def Encender(self,nota):
        
        if nota % 12 in [0,2,4,5,7,9,11]:
            self.teclas_blancas[nota].Encender()
            
        else:
            self.teclas_negras[nota].Encender()
        
    def Apagar(self,nota):
        if nota % 12 in [0,2,4,5,7,9,11]:
            self.teclas_blancas[nota].Apagar()
        else:
            self.teclas_negras[nota].Apagar()
    