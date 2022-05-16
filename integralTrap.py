from ast import Div
from concurrent.futures import ThreadPoolExecutor
from sys import flags

#funcion = input("Ingrese funcion ")
#minimo = float(input("ingrese valor minimo "))
#maximo = float(input("ingrese valor maximo "))

lista = []

def operacionHilo(funcion, posMin, posMax):
    x = posMin
    global lista
    baseMen= eval(funcion)
    x= posMax
    baseMay= eval(funcion)
    resultado = (baseMay + baseMen)*(posMax-posMin)/2
    lista.append(resultado) 

def HallarInt(funcion, minimo, maximo):
    minimo = float(minimo)
    maximo = float(maximo)
    
    resultado = 0.0
    global lista
    error = 0.000000001
    div = 2
    errorResultado = 1
    while (errorResultado > error):
        
        nuevoResultado = 0.0
        dif = (maximo - minimo)/div
        pos1 = minimo
        ejecutor = ThreadPoolExecutor(max_workers=20)
        for i in range(div):
            pos2 = pos1 + dif
            ejecutor.submit(operacionHilo,funcion,pos1,pos2)
            pos1 = pos2

        ejecutor.shutdown()
        for j in lista:
            nuevoResultado =  nuevoResultado + j
        
        lista = []
        #print("Con ", div, "  v1: ", resultado, "   v2: ", nuevoResultado )
        errorResultado = abs((nuevoResultado - resultado)/nuevoResultado)
        resultado = nuevoResultado
        #print("Con ", div, "  v1: ", resultado, "   v2: ", nuevoResultado, "   error: ",errorResultado )
        div = div+1

    print ("EL resultado es: ", nuevoResultado)
    print ("Cantidad de divisiones: ", div-1)
    return str(nuevoResultado), str(div-1)