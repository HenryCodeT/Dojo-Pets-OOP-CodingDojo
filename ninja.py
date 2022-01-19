from mascota import Mascota

class Ninja(Mascota):
    def __init__(self, nombre, apellido, mascota, tipo, comida_mascota ):
        super().__init__( mascota, tipo, comida_mascota )
        self.nombre=nombre
        self.apellido=apellido
                	
    def pasear(self): 
        #walk the ninja's pet by invoking the play() pet method
        self.jugar() 
    def alimentar(self): 
        #feed the ninja's pet by invoking the eat() pet method 
        self.comer()
    def bañar(self): 
        #clean the ninja's pet by invoking the pet method sound()
        self.sonido()