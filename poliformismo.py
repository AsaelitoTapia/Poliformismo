import os

os.system("cls")
class Consola:
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año
    
    def mostrar_datos(self):
        return self.nombre, self.año
        
class Play(Consola):
    def mostrar_datos(self):
        return super().mostrar_datos()
    
class Xbox(Consola):
    def mostrar_datos(self):
        return super().mostrar_datos()
    
def mostrar_datos(consola):
    print(consola.mostrar_datos())
    
# Ejemplo de uso
play=Play("Playstation",1400)
xbox=Xbox("XBox",1700)

mostrar_datos(play)
mostrar_datos(xbox)