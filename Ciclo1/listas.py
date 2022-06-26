#adicionar a una lista
lista =[1,2,3,'c','hola']
print(lista)
lista.append('fna')
print(lista)
lista[0]='1'
print(lista)
#eliminar de una lista
del lista[5]#permite eliminar desde index o toda la lista
print(lista)
lista.remove('c')#elimina el objeto por su valor
print(lista)
#metodo pop para listas
lista.pop(2)#elimina por indice y retorna el valor eliminado
print(lista)
#recorrer listas
for i in range(len(lista)):
    print(lista[i], end=" ")#end sirve para definir el espaciador
#listas multidimensionales
print()
matriz =[[1,'c','hola'],[2.6,'mundo',3],[True,'feliz',4]]
for i in matriz:
    for j in i:
        print(j)
#indexado negativo
print(lista[-1])
#slicing
lista =[1,2,3,'c','hola']
listaSlice = lista[2:4:1]#inicio:final:incremento
print(listaSlice)
listaSlice = lista[::-1]
print(listaSlice)