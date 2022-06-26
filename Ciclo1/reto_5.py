import csv, json


def concepto(lista):
    if (float(lista[4]) -float(lista[1])>0):
        return 'SUBE'
    elif (float(lista[4]) -float(lista[1])<0):
        return 'BAJA'
    else:
        return 'ESTABLE'

def promedioPrecio(lista):
    return (float(lista[2])-float(lista[3]))/2

def menorPrecioAccion(registro):
    menor=float(registro[0][3])
    fecha=''
    for fila in range(0,len(registro),1):
        if float(registro[fila][3]) < menor:
            menor=float(registro[fila][3])
            fecha=registro[fila][0]
    return fecha, menor

def mayorPrecioAccion(registro):
    mayor=float(registro[0][2])
    fecha=''
    for fila in range(0,len(registro),1):
        if float(registro[fila][2]) > mayor:
            mayor=float(registro[fila][2])
            fecha=registro[fila][0]
    return fecha,mayor

def conteoTendeciaAcciones(registro):
    sube=0
    baja=0
    estable=0
    for fila in range(0,len(registro),1):
        if registro[fila][1] == 'SUBE':
            sube+=1
        elif registro[fila][1] == 'BAJA':
            baja+=1
        else:
            estable+=1
    
    return sube,baja,estable

def solucion():
    registrosParaCsv=[]
    registrosDeCsv=[]
    cabecera=['Fecha','Comportamiento de la accion','Punto medio HIGH-LOW']
    detallesJson={}

    with open('Ciclo1\GLOBANT.csv','r') as archivoCsv:
        lector=csv.reader(archivoCsv)
        next(lector)
        for fila in lector:
            registrosDeCsv.append(fila)
            registrosParaCsv.append([fila[0],concepto(fila),promedioPrecio(fila)])


    with open('Ciclo1/analisis_archivo.csv','w') as archivoSalida:
        escritor = csv.writer(archivoSalida,delimiter='\t')    
        escritor.writerow(cabecera)
        for registro in registrosParaCsv:
            escritor.writerow(registro)

    detallesJson["date_lowest_price"]=menorPrecioAccion(registrosDeCsv)[0]
    detallesJson["lowest_price"]=menorPrecioAccion(registrosDeCsv)[1]
    detallesJson["date_highest_price"]=mayorPrecioAccion(registrosDeCsv)[0]
    detallesJson["highest_price"]=mayorPrecioAccion(registrosDeCsv)[1]
    detallesJson["cantidad_veces_sube"]=conteoTendeciaAcciones(registrosParaCsv)[0]
    detallesJson["cantidad_veces_baja"]=conteoTendeciaAcciones(registrosParaCsv)[1]
    detallesJson["cantidad_veces_estable"]=conteoTendeciaAcciones(registrosParaCsv)[2]

    with open('Ciclo1/detalles.json','w') as archivoJson:
        json.dump(detallesJson,archivoJson, indent=3)
    
solucion()