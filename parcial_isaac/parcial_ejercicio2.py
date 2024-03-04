#creear una clase padre llamada factura con los atributos ID,vendedor y fecha compra,dentro de esta clase padre crear una funcion que imprima el vendedor y otro de la fecha compra. 
#luego crear una clase hija que detalle factura,producto,precio,cantidad y total
#crear una funcion que calcule el total 

class factura:
    
    def __init__(self,Id,vendedor,fechacompra):
        
        self.Id = Id
        self.vendedor = vendedor
        self.fechacompra = fechacompra
    
    def printfactura (self):
            
     return(self.Id,self.vendedor,self.fechacompra)
        
   
class detalle (factura):
    
    def __init__(self, Id,vendedor,fechacompra,producto,precio,cantidad,total=0):
        
        self.producto = producto
        self.precio = precio
        self.cantidad= cantidad
        self.total = total
        
        super().__init__(Id, vendedor,fechacompra)
        
    def detalle(self):
            
     return(self.producto,self.precio,self.cantidad)
 
    def FTotal (self):
        
       return(self.cantidad * self.precio)
        
d = detalle (1043967918,"Isaac","4/03/24","leche",3600,2)

print(" El id del producto es: ", d.Id ,"\n El vendedor es: ", d.vendedor ,"\n la fecha de la compra fue el dia: ", d.fechacompra , "\n el producto es: ", d.producto ,"\n el precio del producto es: ", d.precio , "\n la cantidad de los productos fue: ", d.cantidad)
print(f" el total de la venta fue: {d.FTotal()} ")