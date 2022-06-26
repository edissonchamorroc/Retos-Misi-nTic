#diccionarios
diccionario = {1:'edisson',
               2:'chamorro',
               'aa':1234,
               ('secreto'):[1,2,3,4]}

print(diccionario['aa'])
print(diccionario.get('secreto'))
#añadir y eliminar datos de un diccionario
diccionario[2]='coral'
print(diccionario)
#eliminar
del diccionario[2]
print(diccionario)
diccionario.pop('aa')
print(diccionario)
#recorrer diccionarios
diccionario = {1:'edisson',
               2:'chamorro',
               'aa':1234,
               ('secreto'):[1,2,3,4]}
for i in diccionario:
    print(f'clave : {i} valor: {diccionario[i]}')