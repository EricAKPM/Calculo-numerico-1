#include <iostream>
#include <math.h>

double funcao(double valor){
	return pow(valor,3)+pow(valor,2)-valor; //RAIZ:0 e 0.6... [0,0.3] e [0.4,0.8]
    //return valor*log10(valor)-1; //RAIZ:2.5... [2,3]
    //return pow(valor,3)-9*valor+3; //RAIZ:0.337618004 [0,1]
    //return pow(valor,2)+valor-6;//RAIZ:1.99998 [1.5,2.5]
}

double formula(double a, double b, double menor, double maior ){
	return ((a * maior) - (b * menor)) / (maior - menor);
}

int main(){
	double a = 0.0, b = 0.0, x = 0.0, delta = 0.0, fx = 0.0, m = 0.0;
	int interacoes = 0, k = 0;
	
	printf("Entre com o intervalo a: ");
	scanf("%lf", &a);
	printf("Entre com o intervalo b: ");
	scanf("%lf", &b);
	printf("Entre com o delta:");
	scanf("%lf", &delta);
	printf("Entre com o numero maximo de interacoes: ");
	scanf("%d", &interacoes);

	while(funcao(a)*funcao(b) > 0){
    	printf("Entre com o intervalo a: ");
		scanf("%lf", &a);
		printf("Entre com o intervalo b: ");
		scanf("%lf", &b);
	}
	if((fabs(b - a) < delta) || fabs(funcao(a)) < delta || fabs(funcao(b)) < delta){
		printf("RAIZ: %lf\n", a);
		printf("NUMERO DE INTERACOES: 0:\n");
	}else {
		do{
			k++;
			m = funcao(a);
			x = formula(a, b, funcao(a), funcao(b));
			fx = funcao(x);
			if(m * fx > 0){
				a = x;	
			}else{
				b = x;
			}
			if(fabs(funcao(x)) < delta){
				printf("RAIZ: %lf e %lf\n",a, b);
				printf("NUMERO DE INTERACOES: %d:\n",k);
				printf("x = %lf", x);
			}
		}while(fabs(funcao(x)) > delta && k <= interacoes);
	}
}
