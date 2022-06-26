estudiante1={
    'cédula':'12345',
    'nombre':'pepito',
    'nota_fundamentos':4.3
}
estudiante2={
    'cédula':'23456',
    'nombre':'fulanito',
    'nota_fundamentos':3
}
estudiante3={
    'cédula':'98765',
    'nombre':'pancho',
    'nota_fundamentos':5
}
estudiante4={
    'cédula':'3784365',
    'nombre':'pancho',
    'nota_fundamentos':2.4
}
estudiante5={
    'cédula':'980039765',
    'nombre':'pancho',
    'nota_fundamentos':4.4
}
estudiante6={
    'cédula':'9876003335',
    'nombre':'pancho',
    'nota_fundamentos':4.4
}

grupo =[estudiante1,estudiante2,estudiante3,estudiante4,estudiante5,estudiante6]
#verficar las tres notas más altas
#obtener su cedula y ponerlo en el cuadro de honor
#verificar tres notas repetidas y poner cedulas en cuadro de honor
def 𝑐𝑎𝑙𝑐𝑢𝑙𝑎𝑟_𝑝𝑟𝑜𝑚𝑒𝑑𝑖𝑜_𝑦_𝑐𝑢𝑎𝑑𝑟𝑜_ℎ𝑜𝑛𝑜𝑟(𝑔𝑟𝑢𝑝𝑜):
    notas=[]
    promedio=0.0
    cuadro_honor ={
        1:[],
        2:[],
        3:[]
    }

    #CODIGO PARA OBTENER NOTAS SIN REPETIR

    for estudiante in grupo:
        notas.append(estudiante['nota_fundamentos'])

    promedio=sum(notas)/len(notas)

    notas = list(set(notas))
    notas.sort(reverse=True)
    notas=notas[0:3:1]
    #print(f'notas sin eliminar {notas}')
    
    #codigo para buscar estudiantes con notas altas
    ciclo=1
    for nota in notas:
        for estudiante in grupo:
            if estudiante['nota_fundamentos'] == nota:
                cuadro_honor[ciclo].append(estudiante['cédula'])
        ciclo+=1

    return (promedio,cuadro_honor)

print(calcular_promedio_y_cuadro_honor(grupo))