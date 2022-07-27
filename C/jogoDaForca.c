#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	char palavras[10][30] = {"brasil","alemanha", "arabia saldita"};
	char stickman[30];
	char letraDigitada;	
	
	int i;
	int j;
	int c;
	
	int x;
	int y;	
	
	int acertos;
	int vida;
	int encontrada;
	acertos =0;
	vida = 6;
	encontrada = 0;
	
	srand(time(0));
		
	printf("\t\tJogo da Forca!!!\n");
	printf("palavras ja inclusas:\n");
	puts(palavras[0]);
	puts(palavras[1]);
	puts(palavras[2]);
	
	i=3;
		
	while(i<10){
		printf("\nInsira a %da palavra:", i+1);
		gets(palavras[i]);
		i++;
	}
	
	printf("Pressione qualquer tecla para continuar");
	system("pause>null");
	system("cls");
	
	x = rand()%10;  // sortia entre 0 e 9 uma palavra	
	y = strlen(palavras[x]); //quantidade de letras que a palavra sorteada tem
 	
 	j=0;
	while(j<y){		
		stickman[j] = '#';
		printf("%c",stickman[j]);
	 	j++;
	}
	
	while(vida != 0){
		printf("\nInsira uma letra:");
		scanf(" %c", &letraDigitada); // insira uma letra	 	 	
	 	
		for(c=0; c<y; c++){			
			if (palavras[x][c]==letraDigitada){				
				stickman[c] = letraDigitada;
				acertos++;
				encontrada = 1;				
			}						
			printf("%c", stickman[c]);
		}	
				
		if (encontrada == 0){
			vida--;
			switch(vida){
				case 5: {
					printf("\n %c\n",'o');
					break;
				}
				case 4: {
					printf("\n %c\n",'o');
					printf(" %c\n",'|');
					break;
				}
				case 3: {
					printf("\n %c\n",'o');
					printf("%c",'/');
					printf("%c\n",'|');
					break;
				}
				case 2: {
					printf("\n %c\n",'o');
					printf("%c",'/');
					printf("%c",'|');										
					printf("%c\n",'\\');
					break;
				}
				case 1: {
					printf("\n %c\n",'o');
					printf("%c",'/');
					printf("%c",'|');										
					printf("%c\n",'\\');			
					printf("%c\n",'/');
					break;
				}
				case 0: {
					printf("\n %c\n",'o');
					printf("%c",'/');
					printf("%c",'|');										
					printf("%c\n",'\\');			
					printf("%c",'/');
					printf(" %c\n",'\\');			
					break;
				}				
			}
		}				
		encontrada = 0;
				
		if(acertos==y){
			printf("\nGanhou!");
			break;
		}			
	}
	
	if(vida==0){
		printf("\nGame Over!");				
	}
		
	return 0;
}
