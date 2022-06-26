#tuplas un vez creadas no se pueden modificar


tupla=(1,2,0,'c',True,'hola',[1,2,3])
#me permite modificar lo que hay dentro de una lista interna
tupla[-1][0]=7
print(tupla)
#recorrer tupla
for i in range(len(tupla)):
    print(tupla[i])
#una forma para modificar un tupla
lista = list(tupla)
print(lista)
#conjuntos eliminan datos repetidos y los ordena
conjunto = {9,5,1,2,3,4,1,2,3,4}
print(conjunto)
#añadir y eliminar datos en un conjunto
conjunto.add(10)#añade de a uno
print(conjunto)
conjunto.add((1,2,3))
print(conjunto)
conjunto.update([11,2,3,4,12])#añadir varios datos
print(conjunto)
conjunto.remove(1)
print(conjunto)
conjunto.discard(20)#busca el dato y lo elimina, si no está sigue su ciclo
print(conjunto)
#convertir una lista en conjunto
lista =[1,2,3,3,4,2,4,5,2,1.1]
conjunto = set(lista)
print(conjunto)
