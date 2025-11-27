from mido import MidiFile

class Archivo:
    def __init__(self, file):
        
        self.file_name = file
        self.byte = file
        self.mid = MidiFile (self.file_name)
        
        

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
        
        self.mid
                    
        print(" ")
        if argumento == None and channel == None:
            print(self.mid)
            quit()
        
        if argumento == None and channel != None:
                print(f"Channel's disponibles en cada índice")
                print(f"cantidad de tracks: {len(self.mid.tracks)}")
                for i in range(0,len(self.mid.tracks)):
                    for j in self.mid.tracks[i]:
                        if j.type == 'program_change':
                            print(f"indice: {i}, channel: {j.channel}")
                quit()
        if argumento == "note_on" and channel == None:
            for i, track in enumerate(self.mid.tracks):
                print(track)
            quit()   
        if argumento == "note_on" and channel != None:
            try:
                
                for i, track in enumerate(self.mid.tracks[channel]):
                    print(track)
            except:
                print(f"Exception: channel deberia ser un indice int de los siguientes disponibles")
                print(f"cantidad de tracks: {len(self.mid.tracks)}")
                for i in range(0,len(self.mid.tracks)):
                    for j in self.mid.tracks[i]:
                        if j.type == 'program_change':
                            print(f"indice: {i}, channel: {j.channel}")
                raise Exception("indice fuera de rango")


            quit()   
        
     