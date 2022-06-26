

def eliminarCaracteresEspeciales(lista_texto):
    lista_texto_modificada=[]
    caracteres=['-','¿','?','.',',','¡','!',':','"','–']
    for palabra in lista_texto:
        for caracter in caracteres:
            palabra=palabra.lower().replace(caracter,"")           
        lista_texto_modificada.append(palabra)
    return lista_texto_modificada

def buscarPalabra(diccionario,palabra):
    esta=False
    for clave in diccionario:
        if clave==palabra:
            esta=True
    return esta
    
def conteoPalabras(lista_texto):
    lista_texto=eliminarCaracteresEspeciales(lista_texto)
    palabra_cantidad={}
    for palabra in lista_texto:
        if buscarPalabra(palabra_cantidad,palabra) and palabra!='':
            palabra_cantidad[palabra]+=1
        else:
             palabra_cantidad[palabra]=1
    
    return palabra_cantidad

def palabrasFrecuentes(diccionario):
    lista_conteo=[]
    lista=sorted(diccionario.items(),key=lambda x:x[1],reverse=True)
    lista.remove('')
    print('----------------------------------------------')
    limite=0
    for tupla in lista:
        if limite<20:
            lista_conteo.append(list(tupla))
            limite+=1

    return lista_conteo


def main(lista_texto):
    # ACÁ INICIA LA FUNCIÓN main
    diccionario=conteoPalabras(lista_texto)
    lista_conteo=palabrasFrecuentes(diccionario)

    # ACÁ TERMINA LA FUNCIÓN main
    # NO MODIFICAR LA SIGUIENTE LÍNEA
    return lista_conteo

cuento=['Habia','una','vez,','un','animal','muy','bonito.','¿Se','acabo?.','animal','muy','bonito.','¿Se','acabo?.','animal','muy','bonito.','¿Se','acabo?.']

print(main(cuento))