#include <iostream>
#include "controleremoto.cpp"
#include <time.h>

using namespace std;

int main(int argc, char** argv) {
srand(time(0));	
ControleRemoto c;
c.s.gerar_numero_de_serie();



	return 0;
}
