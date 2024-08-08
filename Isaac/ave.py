from Recorderis import Animal

class ave(Animal):
    
    def __init__(self,Nombre,Peso,ano_nacimiento,propietario):

        super().__init__(Nombre,Peso)
        self.ano_nacimiento = ano_nacimiento
        self.propietario = propietario
    
    def calcularedad(self):
        
        edad = 2024 - self.ano_nacimiento
        
        if (edad>5):
            
            print(f'La edad es {edad}, es mayor de edad')
        else:
            print(f'La edad es {edad}, es menor de edad')


ave1= ave('loro','1KG',2022,'Isaac')
ave1.calcularedad()
ave1.mostrarnombre()



