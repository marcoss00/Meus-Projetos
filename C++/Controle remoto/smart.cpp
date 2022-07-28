#include "tv.cpp"

using namespace std;

class Smart : public TV{
	
	public:
	
	
int trocar_canal(int canal1){
	canal = canal1;

	return canal; 	
}
int trocar_canal(string canal2){
	if(canal2=="Fox"){
		canal = 301;
	} else if(canal2=="HBO"){
		canal = 382;
	} else if(canal2=="TLC"){
		canal = 522;
	}
	return canal;
}	
		
string exibir_detalhes(){
	stringstream Resultado;
	Resultado << canal;
	string c;
	c="Canal:"+Resultado.str()+"\nVolume:"+volume+"\nAno: "+ano+"\nMarca:"+marca+"\nNumero de Serie: "+numero_de_serie;
	return c;
}

};
