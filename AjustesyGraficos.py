#==============================================
#       Ismael Charpentier Martín
#---------------------------------------------
#       Conjunto de ajustes y funciones para 
#       optimizar el ajuste de datos
#---------------------------------------------
#       Fecha: 18/11/2021
#==============================================
import numpy as np
from scipy.optimize import curve_fit
#import matplotlib.pyplot as plt 


def main():
    print('Hello Wolrd!')

#===================================
#   Funciones polinómicas
#===================================

def recta(x, m=1, n=0):
    return m*x + n

def cuadratica(x, a2=1, a1=0, a0=0):
    '''Parábola por defecto'''
    return a2*x**2 + a1*x + a0

def cubica(x, a3=1, a2=0, a1=0, a0=0):
    return a3*x**3 + a2*x**2 + a1*x + a0


#===================================
#   Funciones armonicas (trig)
#===================================

def armonica_seno(x, w=1, fi=0, A=1, offset=0):
    return A*np.sin(w*x + fi) + offset

def armonica_coseno(x, w=1, fi=0, A=1, offset=0):
    return A*np.cos(w*x + fi) + offset


#=================================
#   Ajuste de datos a función
#=================================


#=================================================================================
#   Funcion que ajusta datos a una funcion matematica
# -------------------------------------------------------------------------------
#   Parametros:
#       - funcion: Funcion matematica a la que ajustar los datos 
#       - x_data: Vector de datos para variable indep (x)
#       - y_data: Vector de datos para variable depen (y)
#       - param0: Vector de valores para inicializar los 
#                 parametros de la funcion
#-------------------------------------------------------------------------------
#   Return:
#       - popt: valores optimos para los parámetros (metodo minimos cuadrados)
#       - pcov: matriz (2D array) de las varianzas de los parametros
#       - perr: error de los parámetros popt (raiz de la diagonal de pcov)
#=================================================================================
def ajuste(funcion, x_data, y_data, param0):
    popt, pcov = curve_fit(funcion, x_data, y_data, param0)
    perr = np.sqrt(np.diagonal(pcov))

    return popt, pcov, perr


def graf():

if __name__ == "__main__":
    main()

    