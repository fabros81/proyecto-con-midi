from mido import MidiFile


class Archivo:
    def __init__(self, file):
        self.file_name = file
        self.byte = file
        self.parse = self._parseo()
        
        

    def _parseo(self):
        return MidiFile(self.byte)
    
    def printParse(self):
        for i in self.parse:
            print(i)
    def printByte(self):
        for i in self.byte:
            print(i)           
            
    def showOnlyRawMidi(self,argumento = None, channel = None):
        '''
            muestra los mensajes midi en diferentes formatos
                parámetros:
                - argumento: "None". imprime el archivo midi tal cual lo devuelve Mido
                             "note_on". imprime todos los mensajes que contengan "note_on"
                - channel: 
        '''
        
        print(" ")
        print(f"archivo: {self.file_name}")
        print(" ")
        
        mid = MidiFile(self.file_name)
        
        print(f"cantidad de tracks: {len(mid.tracks)}")
        for i in range(0,len(mid.tracks)):
            for j in mid.tracks[i]:
                if j.type == 'program_change':
                    print(f"indice: {i}, channel: {j.channel}")
            
        print(" ")
        if argumento == None and channel == None:
            print(mid)
            quit()
        if argumento == "note_on" and channel == None:
            for i, track in enumerate(mid.tracks):
                print(track)
            quit()   
        if argumento == "note_on" and channel != None:
            try:
                
                for i, track in enumerate(mid.tracks[channel]):
                    print(track)
            except:
                print(f"Exception: channel deberia ser un indice int de los siguientes disponibles")
                print(f"cantidad de tracks: {len(mid.tracks)}")
                for i in range(0,len(mid.tracks)):
                    for j in mid.tracks[i]:
                        if j.type == 'program_change':
                            print(f"indice: {i}, channel: {j.channel}")
                raise Exception("indice fuera de rango")


            quit()   

#mid = MidiFile(file_midi_path)