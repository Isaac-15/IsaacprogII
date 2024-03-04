#crear una clase llamada animales con los siguientes atributos: nombre,numero de patas,fecha de vacuna,propietario
#crear una funcion que imprima en consola los atributos mediante un mensaje personalizado

class animales:
    
    def __init__(self, nombre, numero_de_patas, fecha_de_vacunas, propietario):
    
       self.nombre = nombre
       self.numero_de_patas = numero_de_patas
       self.fecha_de_vacunas = fecha_de_vacunas
       self.propietario = propietario
       
       
    def printnombre(self):
        
     return (self.nombre)
     
    def printpatas(self):
            
      return(self.numero_de_patas)
      
    def printfecha_de_vacunas(self):
        
     return (self.fecha_de_vacunas)  
              
    def printpropietario(self):
            
       return (self.propietario)
       
a = animales ("caballo",4,"26/10/22","isaac")

print(" el nombre del animal es: ",a.printnombre(),"\n el numero de patas es: ",a.printpatas(),"\n la fecha de la vacuna es: ",a.printfecha_de_vacunas(),"\n el nombre del propietario es: ",a.printpropietario())