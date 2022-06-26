# 13 45 - 10 30 - 15 60 - 8 15
def solucion(edad,peso):
    #ACÁ INICIA LA FUNCIÓN SOLUCIÓN (En este espacio debes entregar tu solución)
    situacionNutricional=''
    diasDieta = 0
    pesoIdeal = 0
    pesoDieta=0.0
    pesoNutricional = 1
    pc = 0.0
    pp = 0.0
    pv = 0.0
    ac = 0.0601
    ap = 0.0305
    av = -0.0244
    #edad =int(input("Indicar la edad del paciente:"))
    #peso = float(input("Indicar el peso del paciente en kilogramos:"))
 
    if (edad>=5 and edad<= 10):
        if peso < 16:
            situacionNutricional = 'A'

            pesoIdeal = 22.0
        elif peso > 28:
            situacionNutricional = 'B'

            pesoIdeal = 24.0
        else:
            situacionNutricional = 'C'

            pesoIdeal = 28.0
    elif (edad > 10 and edad <= 13):
        if peso < 30:
            situacionNutricional = 'A'

            pesoIdeal = 32.0

        elif peso > 50:
            situacionNutricional = 'B'

            pesoIdeal = 43.0
        else:
            situacionNutricional = 'C'

            pesoIdeal = 50.0
    elif (edad > 13 and edad <= 17):
        if peso < 51:
            situacionNutricional = 'A'

            pesoIdeal = 56.0
        elif peso > 63:
            situacionNutricional = 'B'

            pesoIdeal = 58.0
        else:
            situacionNutricional = 'C'

            pesoIdeal = 63.0

    if situacionNutricional == 'A':
      
        pc = 2
        pp = 1
        pv = 2
        
    elif situacionNutricional == 'B':
        pc = 0.6
        pp = 1
        pv = 4
    else:
        pc = 0.5
        pp = 0.7
        pv = 2
    
    while True:
        
        
        if (situacionNutricional!='B' and int(peso) == pesoIdeal):
            break
        elif(situacionNutricional=='B' and peso < pesoIdeal):
            break
        else:
            peso += (ac*pc+ap*pp+av*pv)
            diasDieta += 1

    if situacionNutricional == 'A' or situacionNutricional == 'B':
        print(
            f'El estado nutricional del paciente es {situacionNutricional} y se requieren {diasDieta} días de dieta para que alcance un peso saludable')
    else:
        print(
            f'El estado nutricional del paciente es {situacionNutricional} y se requieren {diasDieta} días de dieta para que alcance el peso máximo')

edad =int(input("Indicar la edad del paciente:"))
peso = float(input("Indicar el peso del paciente en kilogramos:"))
solucion(edad,peso)