from math import cos, sqrt, sin, tan, pow, log, e

a=float(input('CHUTE INICIAL: '))
precisao=float(input('\nPrecisao: '))
numMaxInteracao=int(input('\nNumero maximo de interacoes: '))
numeroAtuaisInteracao=0
b=0

def fx(x):
    #return x*x-x-2
    return float(pow(x,3)-9*x+3)

def calcularfx(valor):
    #return sqrt(2+valor) #x*x-x-2
    return float(pow(valor,3)/9+1/3)

if abs(fx(a)) < precisao:
    b=a
else:
    b=calcularfx(a)
    numeroAtuaisInteracao=1
    while numeroAtuaisInteracao < numMaxInteracao and (abs(b-a) > precisao or abs(fx(b)) > precisao):
        a=b
        b=calcularfx(a)
        numeroAtuaisInteracao+=1
        print("RAIZ: " + str(b))
print("RAIZ: " + str(b))
print("NUMERO DE INTERACOES: " + str(numeroAtuaisInteracao))