from math import cos, sin, tan, pow, log, e, log10

a=float(input('LIMITE MINIMO: '))
b=float(input('\nLIMITE MAXIMO: '))
precisao=float(input('\nPrecisao: '))
numMaxInteracao=int(input('\nNumero maximo de interacoes: '))
numeroAtuaisInteracao, c = 0, 0

def fx(valor):
    return pow(valor,3)+pow(valor,2)-valor#RAIZ:0 e 0.6... [-1,0.3] e [0.4,0.8]
    #return (valor*log10(valor)-1).real #RAIZ:2.5... [2,3]
    #return pow(valor,3)-9*valor+3 #RAIZ:0.337618004 [0,1]
    #return pow(valor,2)+valor-6#RAIZ:1.99998 [1.5,2.5]

if(abs(fx(a)) < precisao):
    c=a
else:
    if(abs(float(fx(b))) < precisao or abs(float(b-a)) < precisao):
        c=b
    else:
        CPFX=0
        while(numeroAtuaisInteracao < numMaxInteracao and CPFX==0):
            c=b-(float(fx(b))*float(b-a))/(float(fx(b))-float(fx(a)))
            if(abs(float(fx(c))) < precisao or abs(float(c-b)) < precisao):
                CPFX=1
            a=b
            b=c
            numeroAtuaisInteracao+=1
            
print("RAIZ: " + str(c))
print("NUMERO DE INTERACOES: " + str(numeroAtuaisInteracao))
    



