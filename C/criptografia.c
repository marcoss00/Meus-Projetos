#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	
	int resto;
	char palavra[50];
	char alfabeto[27];
	int i;
	
	resto = 30%26;
	
	alfabeto[1] = 'a';
	alfabeto[2] = 'b';
	alfabeto[3] = 'c';
	alfabeto[4] = 'd';
	alfabeto[5] = 'e';
	alfabeto[6] = 'f';
	alfabeto[7] = 'g';
	alfabeto[8] = 'h';
	alfabeto[9] = 'i';
	alfabeto[10] = 'j';
	alfabeto[11] = 'k';
	alfabeto[12] = 'l';
	alfabeto[13] = 'm';
	alfabeto[14] = 'n';
	alfabeto[15] = 'o';
	alfabeto[16] = 'p';
	alfabeto[17] = 'q';
	alfabeto[18] = 'r';
	alfabeto[19] = 's';
	alfabeto[20] = 't';
	alfabeto[21] = 'u';
	alfabeto[22] = 'v';
	alfabeto[23] = 'w';
	alfabeto[24] = 'x';
	alfabeto[25] = 'y';
	alfabeto[26] = 'z';
	
	for(i=0;i<50;i++){
		palavra[i]=' ';
	}

	scanf("%s", &palavra);
	

	for(i=0;i<50;i++){
		if(palavra[i] == 'a'){
			printf("%c", alfabeto[1+resto]);
		}
		else if(palavra[i] == 'b'){
			printf("%c", alfabeto[2+resto]);
		}
		else if(palavra[i] == 'c'){
			printf("%c", alfabeto[3+resto]);
		}
		else if(palavra[i] == 'd'){
			printf("%c", alfabeto[4+resto]);
		}
		else if(palavra[i] == 'e'){
			printf("%c", alfabeto[5+resto]);
		}
		else if(palavra[i] == 'f'){
			printf("%c", alfabeto[6+resto]);
		}
		else if(palavra[i] == 'g'){
			printf("%c", alfabeto[7+resto]);
		}
		else if(palavra[i] == 'h'){
			printf("%c", alfabeto[8+resto]);
		}
		else if(palavra[i] == 'i'){
			printf("%c", alfabeto[9+resto]);
		}
		else if(palavra[i] == 'j'){
			printf("%c", alfabeto[10+resto]);
		}
		else if(palavra[i] == 'k'){
			printf("%c", alfabeto[11+resto]);
		}
		else if(palavra[i] == 'l'){
			printf("%c", alfabeto[12+resto]);
		}
		else if(palavra[i] == 'm'){
			printf("%c", alfabeto[13+resto]);
		}
		else if(palavra[i] == 'n'){
			printf("%c", alfabeto[14+resto]);
		}
		else if(palavra[i] == 'o'){
			printf("%c", alfabeto[15+resto]);
		}
		else if(palavra[i] == 'p'){
			printf("%c", alfabeto[16+resto]);
		}
		else if(palavra[i] == 'k'){
			printf("%c", alfabeto[17+resto]);
		}
		else if(palavra[i] == 'r'){
			printf("%c", alfabeto[18+resto]);
		}
		else if(palavra[i] == 's'){
			printf("%c", alfabeto[19+resto]);
		}
		else if(palavra[i] == 't'){
			printf("%c", alfabeto[20+resto]);
		}
		else if(palavra[i] == 'u'){
			printf("%c", alfabeto[21+resto]);
		}
		else if(palavra[i] == 'v'){
			printf("%c", alfabeto[22+resto]);
		}
		else if(palavra[i] == 'w'){
			printf("%c", alfabeto[23+resto]);
		}
		else if(palavra[i] == 'x'){
			printf("%c", alfabeto[24+resto]);
		}
		else if(palavra[i] == 'y'){
			printf("%c", alfabeto[25+resto]);
		}
		else if(palavra[i] == 'z'){
			printf("%c", alfabeto[26+resto]);
		}
		else if(palavra[i] == ' '){
			break;
		}
	}
	
	
	
	
	
	
	return 0;
}
