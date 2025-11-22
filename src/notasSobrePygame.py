#************* 3 tipos de mediciones de tiempo**********
#1 - ticks de 
# Propósito: tiempo real transcurrido 

pygame.init() # comienza a correr el conteo de ms
tiempo = pygame.time.get_ticks()  # captura los ms desde que comenzó el conteo


#2 -Control de fotogramas. Regula tiempo transcurrido entre frames
# Propósito: regular velocidad del juego
# Ejemplo: ~16.6 ms para 60 FPS
clock = pygame.time.Clock()
ms_entre_frames = clock.tick(60)

#3 Ticks Midi - unidades musicales abstractas
# Propósito: Precisión musical interna
# Relación con ms: Depende de BPM y ticks_per_beat

ticks_per_beat = 480
msg.time = 227  # Ticks MIDI (no ms!)

