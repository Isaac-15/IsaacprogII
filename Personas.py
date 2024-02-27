class Persona:

    def __init__(self, nombre, apellido, cedula, correo, telefono):

            self.nombre = nombre
            self.apellido = apellido
            self.cedula = cedula
            self.correo = correo
            self.telefono = telefono

    
P= Persona("Isaac","Carmona"," 1043967918","isaaccarmona281@gmail.com"," 301619461")

print("mi nombre es "+P.nombre," mi apellido es "+P.apellido," mi cedula es "+P.cedula," mi correo es "+P.correo," y mi telefono "+P.telefono)

