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
        self.teclas_blancas, self.teclas_negras = self._crear_lista_teclas(nota_min, nota_max) 
        self.config.setFinalRecorrido(self.alto_tecla_blanca)
        self.config.setAnchoTecla(self.ancho_tecla_blanca,self.ancho_tecla_negra)
        self.config.setAltoTeclaBlanca(self.alto_tecla_blanca)
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
            #teclas_blancas = [n for n in range(nota_min, nota_max+1) if n % 12 in [0,2,4,5,7,9,11]]
            octava = (nota - nota_min)  // 12
            pos = (nota - nota_min) % 12
            x = octava *(7* self.ancho_tecla_blanca) + (self.ancho_tecla_blanca * patron_octava[pos])
            mapa[nota] = int(x)
            #print(f"nota: {nota}, octava: {octava}, x:{x} ")        
        #print(f"mapa completo: {mapa}, ancho tecla blanca: {self.ancho_tecla_blanca}")        
        return mapa
        
    def _crear_lista_teclas(self, nota_min, nota_max):
        teclas_blancas = []
        teclas_negras = []
        for nota in range(nota_min, nota_max + 1):
            
            if nota % 12 in [0,2,4,5,7,9,11]:
                color = self.config.WHITE
                tecla = Tecla(nota, self.coordenadaX[nota],self.ancho_tecla_blanca-1,self.alto_tecla_blanca, color)
                teclas_blancas.append(tecla)
            else :
                color = self.config.BLACK
                tecla = Tecla(nota, self.coordenadaX[nota],self.ancho_tecla_negra,self.alto_tecla_negra, color)
                teclas_negras.append(tecla)
        return teclas_blancas, teclas_negras
    
    def dibujar(self, pantalla):
        # Teclas blancas
        for tecla in self.teclas_blancas:
            x = tecla.coordX
            y = pantalla.get_height() - self.alto_tecla_blanca
            ancho = tecla.ancho
            alto = tecla.alto
            pygame.draw.rect(pantalla, tecla.mostrarColor, (x, y, ancho, alto))
        
        # Teclas negras (más pequeñas)
        for tecla in self.teclas_negras:
            x = tecla.coordX
            y = pantalla.get_height() - self.alto_tecla_blanca
            ancho = tecla.ancho
            alto = tecla.alto
            pygame.draw.rect(pantalla, tecla.mostrarColor, (x, y, ancho, alto))
                
    