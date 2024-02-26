class Persona:

    def __init__(self, nombre, apellido, cedula, correo, telefono):

            self.nombre = nombre
            self.apellido = apellido
            self.cedula = cedula
            self.correo = correo
            self.telefono = telefono

    def ObtenerInfo(self):
        return f"Mi nombre es: {self.nombre}\n Mi apellido es: {self.apellido}\n Mi cedula es: {self.cedula}\n Mi correo es: {self.correo}\n Mi telefono es: {self.telefono}"

P= Persona("Isaac","Carmona"," 1043967918","isaaccarmona281@gmail.com"," 301619461")

print(P.ObtenerInfo())

