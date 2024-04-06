perro = {}

perro["Nombre"] = "Ares"
perro["Color"] = "Rojo"
perro["Raza"] = "Husky"
perro["Edad"] = "3"

estudiante = {
    
     "nombre" : "Isaac",
     "apellido" : "Carmona",
     "sexo" : "Masculino",
     "edad" : "18",
     "estado civil" : "Soltero",
     "habilidades" : ['lectura','comprension','eficacia','paciencia'],
     "país" : "Colombia",
     "ciudad" : "cartagena",
     "dirección" : "Mz 138 Lt 23"
 }

print(len(estudiante))

print(estudiante["habilidades"])

print(type(estudiante["habilidades"]))

estudiante["habilidades"] = ['lectura','comprension','eficacia','paciencia','comunicacion']

claves = estudiante.keys()

valores = estudiante.values()

print(claves)
print(valores)

print(estudiante.items())

estudiante.popitem()

del perro