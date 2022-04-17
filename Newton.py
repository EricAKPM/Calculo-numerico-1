from cmath import log10, sqrt
from math import cos, sin, tan, pow, log, e

x0=float(input('DIGITE x0: '))
precisao=float(input('DIGITE A PRECISAO: '))
iteracao=int(input('DIGITE A QUANTIDADE DE INTERACOES: '))
k=0
def calcularfx(valor):
    #return pow(valor,3)+pow(valor,2)-valor#RAIZ:0 e 0.6... [0,0.3] e [0.4,0.8]
    return (valor*log10(valor)-1).real #RAIZ:2.5... [2,3]
    #return pow(valor,3)-9*valor+3 #RAIZ:0.337618004 [0,1]
    #return pow(valor,2)+valor-6#RAIZ:1.99998 [1.5,2.5]

def calcularfxlinha(valor):
    #return 3*pow(valor,2)+2*valor-1
    return (log(valor)+1).real
    #return 3*pow(valor,2)-9
    #return 6*valor

fx=(float)(calcularfx(x0).real)
if abs(fx) > precisao:
    fxlinha=(float)(calcularfxlinha(x0))
    x1=x0-((float)(calcularfx(x0))/fxlinha)
    fx=(float)(calcularfx(x1))
    CPFX=0
    while (abs(fx) > precisao and abs(x1-x0) > precisao and k <= iteracao):
        k+=1
        x0=x1
        fxlinha=(float)(calcularfxlinha(x0))
        x1=x0-((float)(calcularfx(x0)/fxlinha))
        fx=calcularfx(x1)
    raiz=x1
else:
    raiz=x0
print("RAIZ: " + str(raiz))
print("NUMERO DE INTERACOES: " + str(k))