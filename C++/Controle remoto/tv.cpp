#include <string>
#include <stdlib.h>
#include <sstream>

using namespace std;

class TV{
	public:
		int canal;
		string volume;
		string ano;
		string marca;
		string numero_de_serie;
		
		

TV(){
	canal = 10;
	volume = "10";
	marca="Samsung";
	ano="2017";
}
public:
	
string exibir_detalhes(){
	stringstream Resultado;
	Resultado << canal;
	string b;
	b="Canal:"+Resultado.str()+"\nVolume:"+volume+"\nAno: "+ano+"\nMarca:"+marca;
	return b;
}
string exibir_display(){
	stringstream Resultado;
	Resultado << canal;
	string a;
	a = "Volume:"+volume + " Canal:" + Resultado.str();
	
	return a;
}
void gerar_numero_de_serie(){
	char v[5]= {'a', 'e', 'i', 'o', 'u'};
	char c[21]= {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'};
	int alev;
	int alec;
	int alec1;
	int alec2;
	int alec3;
	string y[10];
	int x,x1;
	x = rand()%10;
	x1 = rand()%10;
	y[0]="0";
	y[1]="1";
	y[2]="2";
	y[3]="3";
	y[4]="4";
	y[5]="5";
	y[6]="6";
	y[7]="7";
	y[8]="8";
	y[9]="9";
	
	alev=rand()%5;
	alec=rand()%21;
	alec1=rand()%21;
	alec2=rand()%21;
	alec3=rand()%21;
	numero_de_serie= y[x]+y[x1]+v[alev]+"2018"+c[alec]+c[alec1]+c[alec2]+c[alec3];
	
}
	
};
