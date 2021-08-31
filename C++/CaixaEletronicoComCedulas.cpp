#include <iostream>
/*Programa feito em C++ para um caixa eletrônico. O programa perguntar ao usuário a valor do saque e depois informa quantas notas de cada valor serão fornecidas.
As notas disponíveis são as de 1, 5, 10, 50 e 100 reais. O valor mínimo do saque é de 10 reais e o máximo de 600 reais. O programa não se preocupar com a quantidade de
notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.*/

using namespace std;

int main(int argc, char** argv) {
	int valor_saque=0;
	int restante=0;
	int unidade=0;
	int decimal=0;
	int centena=0;
	int qunt_notas1=0;
	int qunt_notas5=0;
	int qunt_notas10=0;
	int qunt_notas50=0;
	int qunt_notas100=0;
	bool condicao_saque;
	
	cout<<"\t\tBem vindo ao caixa eletronico!\n";
	
	do{
	condicao_saque = false;
	cout<<"Quanto voce quer sacar ?";
	cin>>valor_saque;
	
	if(valor_saque < 10 || valor_saque > 600){
		condicao_saque = true;
		cout<<"Voce deve sacar no minimo R$10 e no maximo R$600\n";
	}
	}while(condicao_saque);
	
	restante = valor_saque;
	
	unidade = restante%10;
	restante = restante - unidade;
	decimal = restante%100;
	restante = restante - decimal;
	centena = restante;
	
if(unidade > 5){
	qunt_notas5++;
	unidade = unidade - 5;
	qunt_notas1 = qunt_notas1 + unidade;
}

else if(unidade == 5){
	qunt_notas5++;
}

else{
	qunt_notas1 = qunt_notas1 + unidade;
}

if(decimal > 50){
	qunt_notas50++;
	decimal = decimal - 50;
	qunt_notas10 = qunt_notas10 + (decimal/10);
}

else if(decimal == 50){
	qunt_notas50++;
}

else{
	qunt_notas10 = qunt_notas10 + (decimal/10);
}

if(valor_saque >= 100){
	qunt_notas100 = qunt_notas100 + (centena/100);
}

if (qunt_notas1 > 0){
	cout << "Voce sacou "<<qunt_notas1<< " nota(s) de R$1"<<endl;
}
if (qunt_notas5 > 0){
	cout << "Voce sacou "<<qunt_notas5<< " nota(s) de R$5"<<endl;
}
if (qunt_notas10 > 0){
	cout << "Voce sacou "<<qunt_notas10<< " nota(s) de R$10"<<endl;
}
if (qunt_notas50 > 0){
	cout << "Voce sacou "<<qunt_notas50<< " nota(s) de R$50"<<endl;
}
if (qunt_notas100 > 0){
	cout << "Voce sacou "<<qunt_notas100<< " nota(s) de R$100"<<endl;
}
	
	
	
	
	
	
	return 0;
}
