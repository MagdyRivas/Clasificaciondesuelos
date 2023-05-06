import pandas as pd #Pandas permite la manipulación y análisis de datos
import numpy as np #Numpy es una librería que se usa principalmente para crear, modificar matrices y hacer operaciones entre ellas con facilidad
import matplotlib.pyplot as plt #Matplotlib es una librería que sirve para la generación de gráficos en dos dimensiones
from scipy.interpolate import interp1d #Se utiliza para interpolar

def Granulometria():
    numero_malla=pd.Series(["No. 4","No. 10","No. 20","No. 40","No. 60","No. 140","No. 200"])
    numero_malla

    abertura=pd.Series([4.75,2,.85,.425,.25,.106,.075])
    abertura

    retenido=pd.Series([15.5,25.8,60.5,40.2,41.2,15.2,13.2])
    retenido

    otro=pd.DataFrame({
        "tamiz":numero_malla,
        "abertura (mm)":abertura,
        "% retenido":retenido
    })
    otro

    otro["retenido_acumulado"]=(otro["% retenido"]).cumsum()
    otro

    otro["pasa"]=(otro["% retenido"]).sum()-(otro["retenido_acumulado"])
    otro

    otro["% pasa"]=(otro["pasa"])/(otro["% retenido"]).sum()*100
    otro

    abertura=np.array(otro["abertura (mm)"]) #Se selecciona el titulo para la tabla de los datos correspondientes a la abertura
    pasa=np.array(otro["% pasa"]) #Se selecciona el titulo para la tabla de los datos correspondientes al % que pasa
    plt.figure(figsize=(14, 4)) # Es establece el tamaño de los ejes x y y, se coloca el eje x mas largo que el eje y
    plt.plot(abertura,pasa,linestyle='-', marker='o', color='black', fillstyle='none',label='Data') #Esta línea hace referencia a la gráfica de la línea granulométrica
    f=interp1d(pasa, abertura) #interp1d se utiliza para interpolar la linea granulométrica (asi se cnocen los valores D60, D50, D30 y D10)
    y1_coord=60
    y2_coord=50
    y3_coord=30
    y4_coord=10
    x1_coord=f(y1_coord)
    x2_coord=f(y2_coord)
    x3_coord=f(y3_coord)
    x4_coord=f(y4_coord)
    x1_formatted='{:.2f}'.format(x1_coord)
    x2_formatted='{:.2f}'.format(x2_coord)
    x3_formatted='{:.2f}'.format(x3_coord)
    x4_formatted='{:.2f}'.format(x4_coord)

    plt.scatter(x1_coord, y1_coord, marker='<', s=50, color='yellowgreen', label='D60='+x1_formatted) #Mediante esta línea y las próximas 3 se crea la tabla de convenciones.
    plt.scatter(x2_coord, y2_coord, marker='s', s=50, color='darkorange', label='D50='+x2_formatted)
    plt.scatter(x3_coord, y3_coord, marker='o', s=50, color='darkcyan', label='D30='+x3_formatted)
    plt.scatter(x4_coord, y4_coord, marker='>', s=50, color='fuchsia', label='D10='+x4_formatted)
    plt.title("",fontsize=12)
    plt.xlabel('Tamaño de las partículas (mm)',fontsize=8) #Se nombra el eje x
    plt.ylabel('Porcentaje que pasa (%)',fontsize=8) #Se nombre el eje y
    plt.title('CURVA GRANULOMÉTRICA',fontsize=12) #Se adigna un nombre para el título de la gráfica
    plt.legend() #Se crea una leyenda o una convención con respecto a la línea granulométrica
    plt.xscale("log")
    plt.xlim(0.001,100) #Se establecen los límites de la gráfica en el eje x
    plt.ylim(-10,100) #Se establecen los límites de la gráfica en el eje y
    plt.grid(color='black',lw='0.1',ls='-')
    x=[1, 10, 100, 5, 50, 20, 2, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001]
    plt.xticks(x, x, fontsize=8)
    ax1=plt.gca()
    ax1.invert_xaxis()

    plt.text(85,-7,r'Rocas', fontsize=7, rotation=90) #Mediante esta línea y las próximas 8 se establecen hasta donde llegan los límites de acuerdo al tamaño de las partículas
    plt.text(22,-7, 'Gravas (Gruesas)',fontsize=7, rotation=90)
    plt.text(5.4,-7,r'Gravas (Finas)',fontsize=7, rotation=90)
    plt.text(2.3,-7,r'Arenas (Gruesas)',fontsize=7, rotation=90)
    plt.text(0.5,-7,r'Arenas (Medianas)',fontsize=7, rotation=90)
    plt.text(0.085,-7,r'Arenas (Finas)',fontsize=7, rotation=90)
    plt.text(0.0115,-7,r'Coloides',fontsize=7, rotation=90)
    plt.text(0.0057,-7,r'Limos',fontsize=7, rotation=90)
    plt.text(0.00115,-7,r'Arcillas',fontsize=7, rotation=90)

    malla1=["3 pulg","2-1/2 pulg","2 pulg","1-1/2 pulg","1 pulg","3/4 pulg","1/2 pulg","3/8 pulg","No. 4","No. 6","No. 8","No. 10","No. 16","No. 20","No. 30","No. 40","No. 50","No. 60","No. 80","No. 100","No. 140","No. 170","No. 200"] #Se crea el eje x superior para el número de los tamices
    abertura1=([75, 63, 50, 37.5, 25, 19, 12.5, 9.5, 4.75,3.35,2.36, 2,1.18,.85,0.6, .425,0.3,.25,0.18,0.15,.106,.09,.075])
    ax2=ax1.twiny()
    ax2.set_xscale('log')
    ax2.set_xticks(abertura1)
    ax2.set_xticklabels(malla1, rotation=90, fontsize=8)
    y=(-10,0,20,40,60,80,100)
    ax1.set_yticklabels(y, fontsize=8)
    ax2.set_xlabel('Tamiz',fontsize=8)
    ax2.set_xlim(0.001,100)
    ax2.invert_xaxis()

    LL1=([75,75]) #En esta fila y en las próximas 9 se muestran grupos de valores
    LL2=([19,19]) 
    LL3=([4.75,4.75]) 
    LL4=([2,2]) 
    LL5=([0.425,0.425]) 
    LL6=([0.075,0.075]) 
    LL7=([0.01,0.01])  
    LL8=([0.005,0.005]) 
    LL9=([0.001,0.001]) 
    LL10=([-10,100])

    plt.plot(LL1, LL10,color='salmon', lw='0.9', ls='--') #Se establecen las líneas rojas en los tamices en donde se presentan cambios de tamaño de las partículas (cambio en el tipo de suelo)
    plt.plot(LL2, LL10,color='salmon', lw='0.9', ls='--')
    plt.plot(LL3, LL10,color='salmon', lw='0.9', ls='--')
    plt.plot(LL4, LL10,color='salmon', lw='0.9', ls='--') 
    plt.plot(LL5, LL10,color='salmon', lw='0.9', ls='--')
    plt.plot(LL6, LL10,color='salmon', lw='0.9', ls='--')
    plt.plot(LL7, LL10,color='salmon', lw='0.9', ls='--')
    plt.plot(LL8, LL10,color='salmon', lw='0.9', ls='--')
    plt.plot(LL9, LL10,color='salmon', lw='0.9', ls='--')

    plt.axvline(x=63, ymin=-10, ymax=100, color='blue', ls='-',lw='0.4') #Esta línea y las próximas 16 muestran las líneas azules de la gráfica que hacen referencia a los demás tamices
    plt.axvline(x=50, ymin=-10, ymax=100, color='blue', ls='-',lw='0.4')
    plt.axvline(x=37.5, ymin=-10, ymax=100, color='blue', ls='-',lw='0.4')
    plt.axvline(x=25, ymin=-10, ymax=100, color='blue', ls='-',lw='0.4')
    plt.axvline(x=12.5, ymin=-10, ymax=100, color='blue', ls='-',lw='0.4')
    plt.axvline(x=9.5, ymin=-10, ymax=100, color='blue', ls='-',lw='0.4')
    plt.axvline(x=3.35, ymin=-10, ymax=100, color='blue', ls='-',lw='0.4')
    plt.axvline(x=2.36, ymin=-10, ymax=100, color='blue', ls='-',lw='0.4')
    plt.axvline(x=1.18, ymin=-10, ymax=100, color='blue', ls='-',lw='0.4')
    plt.axvline(x=0.6, ymin=-10, ymax=100, color='blue', ls='-',lw='0.4')
    plt.axvline(x=0.85, ymin=-10, ymax=100, color='blue', ls='-',lw='0.4')
    plt.axvline(x=0.3, ymin=-10, ymax=100, color='blue', ls='-',lw='0.4')
    plt.axvline(x=.25, ymin=-10, ymax=100, color='blue', ls='-',lw='0.4')
    plt.axvline(x=.18, ymin=-10, ymax=100, color='blue', ls='-',lw='0.4')
    plt.axvline(x=.15, ymin=-10, ymax=100, color='blue', ls='-',lw='0.4')
    plt.axvline(x=.106, ymin=-10, ymax=100, color='blue', ls='-',lw='0.4')
    plt.axvline(x=.09, ymin=-10, ymax=100, color='blue', ls='-',lw='0.4')

    plt.show()