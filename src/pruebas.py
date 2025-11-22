file_midi_path = "./archivos midi/fc.mid"

# file_midi_path = "C:/Users/Fabianr/Desktop/UNSAM/programación 1/proyecto con midi/roca_fuerte.mid"


import pygame
from mido import MidiFile
import time



def read_metamsg(file):
    '''
    Ajusta los parámetros default a los que provee el midi file
    '''
    global MS_X_NEGRA
    global TEMPO
    global PPM
    
    mid = MidiFile(file)
    MS_X_NEGRA = mid.ticks_per_beat
    for i,track in enumerate (mid.tracks):
        if i==0:
            for msg in track:
                if msg.type == "set_tempo":
                    TEMPO = msg.tempo           
                    PPM = 60000000 / TEMPO
    print(f"ms x negra : {MS_X_NEGRA}, tempo: {TEMPO}, bpm: {PPM}.")
    
    
def mirarMidi(file):
    mid = MidiFile(file)
    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        for msg in track:
            print(msg)   
#mirarMidi(file_midi_path)
read_metamsg(file_midi_path)    


