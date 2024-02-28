class Persona:

    def __init__(self, nombre, apellido, cedula, correo, telefono):

            self.nombre = nombre
            self.apellido = apellido
            self.cedula = cedula
            self.correo = correo
            self.telefono = telefono

    
P= Persona("Isaac","Carmona"," 1043967918","isaaccarmona281@gmail.com"," 301619461")

print(" mi nombre es: "+P.nombre,"\n mi apellido es: "+P.apellido,"\n mi cedula es: "+P.cedula,"\n mi correo es: "+P.correo,"\n mi numero de telefono: "+P.telefono)

