class lote:
    
    def __init__(self,largo,ancho,constructora):
        
        self.largo = largo
        self.ancho = ancho
        self.constructora = constructora
    
    def printlote (self):
            
     print(self.largo,self.ancho,self.constructora)
        
    def calcular_area(self):
            
     x= self.largo * self.ancho
     
     print(x)
             
class casa (lote):
    
    def __init__(self, largo, ancho, constructora,propietario,telefono):
        
        self.propietario = propietario
        self.telefono = telefono
        
        super().__init__(largo, ancho, constructora)
        
    def printcasa(self):
            
     print(self.propietario,self.telefono)
        
v = casa (25,30,"Iscabo","Isaac",3016191461)

v.printlote()
v.printcasa()
v.calcular_area()

