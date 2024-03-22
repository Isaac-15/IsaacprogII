lista_vacia = []

lista_con_cinco = ['Isaac','carmona','blanco','limon','1505','manzana','pera']

print("la longitud de la primera lista es de: ",len(lista_vacia))

print("la longitud de la segunda lista es de: ",len(lista_con_cinco))

print("el primer elemento es: " ,lista_con_cinco[0])

print("el elemento del medio es: ",lista_con_cinco[3])

print("el ultimo elemento es: ",lista_con_cinco[6])

Datos_personales = ['Isaac','18','1.70','soltero','Mz 138 lt 23']

Datos_personales.append('venezuela')

print(Datos_personales)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' ,'Amazon']

it_companies.insert(0,'cocacola')

if 'Facebook' in it_companies:
    
     print(True)
     

it_companies.sort()

print(it_companies)

it_companies.reverse()

print(it_companies)

it_companies.pop(2)

print(it_companies)

it_companies.clear

print (it_companies)