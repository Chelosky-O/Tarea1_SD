import matplotlib.pyplot as plt
import numpy as np
import math

def graficar():
    valores = []
    
    with open('data.txt','r') as file:
        for line in file:
            curr_place = line[:-1]
            valores.append(curr_place)
    
    valores_count = len(valores)
    
    x = np.arange(0,valores_count,1)
    
    y = list(np.float_(valores))
    
    total = math.fsum(np.float_(valores))
    print("Total: " + str(total/60) + " minutos")
    
    plt.plot(x,y)
    plt.xlabel('Nro Peticion')
    plt.ylabel('Tiempo de respuesta')
    plt.title("Grafico tiempo de respuesta peticiones")
    plt.show()

graficar()