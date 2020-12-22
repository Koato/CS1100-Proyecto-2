import math 

def nota_max(matriz,reopcion):
    max=0
    print('\n')
    print(reopcion)
    for i in range(len(matriz)):
        if( matriz[i][reopcion] > max):
            max=matriz[i][reopcion]
    count=0
    for i in range(len(matriz)):
        if( matriz[i][reopcion] == max):
           count = count + 1 
    return "Nota maxima : " + str(max) + " , cantidad de alumnos con esa nota : " + str(count)


def nota_min(matriz,reopcion):
    min=20
    print('\n')

    for i in range(len(matriz)):
        if( matriz[i][reopcion] < min):
            min=matriz[i][reopcion]
    count=0
    for i in range(len(matriz)):
        if( matriz[i][reopcion] == min):
           count = count + 1 
    return "Nota minima : " + str(min) + " , cantidad de alumnos con esa nota : " + str(count)


def promedio(matriz,reopcion):
    suma=0
    print('\n')
    for i in range(len(matriz)):
        suma = suma + matriz[i][reopcion]

    return "El  promedio es : " + str(float(suma/len(matriz)))

def moda(matriz,reopcion):
    lista=[]
    print('\n')
    for i in range(len(matriz)):
        lista.append(matriz[i][reopcion])

    list_rep=[]
    for i in range(len(lista)):
        cant_max=1
        for j in range(i):
            if(lista[i]==lista[j]):
                cant_max=cant_max+1        
        list_rep.append(cant_max)
    
    
    mayor=0
    pos=0
    for i in range(len(list_rep)):
        if(mayor<list_rep[i]):
            mayor=list_rep[i]
            pos=i
    

    return "La moda es : " + str(lista[pos])


def desviacion_media(matriz,reopcion):
    promedio=0
    print('\n')
    for i in range(len(matriz)):
        promedio = promedio + matriz[i][reopcion]

    promedio=float(promedio/len(matriz))

    for i in range(len(matriz)):
        if(matriz[i][reopcion] - promedio < 0):
            print((matriz[i][reopcion]-promedio * -1))
        else:
            print((matriz[i][reopcion]-promedio))            
        return str(matriz[i][1]) + "  : Desviacion con respecto a la media "

def varianza(matriz,reopcion):
    promedio=0
    print('\n')
    for i in range(len(matriz)):
        promedio = promedio + matriz[i][reopcion]

    promedio=float(promedio/len(matriz))
    suma_total=0
    for i in range(len(matriz)):
        suma_total= suma_total + (matriz[i][reopcion] - promedio) ** 2
    
    return "La varianza es " + str(float(suma_total/len(matriz)))

def desviacion_standard(matriz,reopcion):
    promedio=0
    print('\n')
    for i in range(len(matriz)):
        promedio = promedio + matriz[i][reopcion]

    promedio=float(promedio/len(matriz))
    suma_total=0
    for i in range(len(matriz)):
        suma_total= suma_total + (matriz[i][reopcion] - promedio) ** 2

    suma_total = math.sqrt(float(suma_total/len(matriz)))            

    return "La deviacion estandar es " + str(suma_total)
