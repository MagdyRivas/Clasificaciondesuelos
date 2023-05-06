import matplotlib.pyplot as plt
import numpy as np

def cartaPlasticidad():
    #valores de entrada
    Limite_liquido = 60
    Indice_plasticidad = 40

    # Con los datos del limite liquido y el Indice de plasticidad se grafica la ubicación del suelo en la carta de plasticidad.
    plt.plot(Limite_liquido,Indice_plasticidad,'ro')
    plt.vlines(Limite_liquido,0,60,'k','--')
    plt.annotate(' LL ',(Limite_liquido,55))
    plt.annotate(' IP ', (20,Indice_plasticidad + 2))
    plt.hlines(Indice_plasticidad,0,100,'k','--')

    # # Se establecen los limites de los ejes x,y.
    plt.xlim(0,100)
    plt.ylim(0,60)

    # Para graficar las lineas de la carta de plasticidad utilizamos las ecuaciones conocidas para la Linea A y la Linea U:
    x=np.array([0,100])
    LineaA =0.73*(x-20)
    LineaU = 0.9*(x-8)
    plt.annotate('Linea A', (90,50),rotation=38) # Etiqueta de la linea A
    plt.annotate('Linea U', (60,45),rotation=45) # Etiqueta de la linea U

    # # Estas lineas gráfican las lineas A y U de forma estética
    plt.plot(x, LineaA, 'darkblue', label = "Linea A" )
    plt.plot(x, LineaU, 'k:', label = "Linea U")

    # # # Graficamos lineas frontera de la carta de plasticidad donde se encuentran los suelos CL-ML
    plt.hlines(7,15.7,29.5,'m')
    plt.hlines(4,12.4,25.5,'m')

    # # # Estas lineas permiten que se muestren en la gráfica las etiquetas de las diferentes zonas.
    plt.annotate('CL-ML', (15,5))
    plt.annotate('MH', (80,20))
    plt.annotate('CL', (30,15))
    plt.annotate('CH', (62,40))
    plt.annotate('ML', (35,5))
    plt.annotate('NO EXISTE', (15,35))

    # # # Divide la gráfica cuando el limite liquido es igual a 50 para diferenciar si el suelo es de plasticidad alta o baja
    plt.vlines(50,0,60,'g')

    # Estas lineas mejoran la estetica de la gráfica, hacen que se sombreen las diferentes zonas de la carta de plasticidad
    # Dentro de las variables de la d a la m se guardan las coordenadas que delimitan cada zona.
    d=[50,50,100,100]
    e=[0,22,58,0]
    plt.fill(d,e,'pink')
    f=[25.5,12.4,8,20,50,50]
    g=[4,4,0,0,0,22]
    plt.fill(f,g,'lightgray')
    h=[50,100,100,75,50]
    i=[22,58,60,60,38]
    plt.fill(h,i,'lightgreen')
    j=[29.5,15.7,12.4,25.5]
    k=[7,7,4,4]
    plt.fill(j,k,'m')
    l=[15.7,29.5,50,50]
    m=[7,7,22,38]
    plt.fill(l,m,'bisque')

    # # Se grafica la grilla, el titulo y las etiquetas de los ejes.

    # plt.grid()
    plt.title("Carta de plasticidad",fontsize=10)
    plt.xlabel("Limite liquido",fontsize=10)
    plt.ylabel("Indice de plasticidad",fontsize=10)
    plt.legend()
    plt.show()
                 