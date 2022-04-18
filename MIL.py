from math import cos, sqrt, sin, tan, pow, log, e

a=float(input('CHUTE INICIAL: '))
precisao=float(input('\nPrecisao: '))
numMaxInteracao=int(input('\nNumero maximo de interacoes: '))
numeroAtuaisInteracao=0
b=0
#b guarda a raiz

def fx(x):
    return x*x-x-2
    #return float(pow(x,3)-9*x+3)

#fi de x
def calcularfx(valor):
    return sqrt(2+valor) #x*x-x-2
    #return float(pow(valor,3)/9+1/3)

# precisao inicial for suficiente
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
print("NUMERO DE INTERACOES: " + str(numeroAtuaisInteracao))