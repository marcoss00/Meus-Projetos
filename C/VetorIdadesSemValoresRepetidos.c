#include <stdio.h>
#include <stdlib.h>



int main(int argc, char *argv[]) {
	int idade[10];
	int aleatorio;
	int i;
	int j;
	int k;
	srand(time(0));

	
	
	
	for(i = 0; i<10; i++){
		j=0;

		idade[i] = (rand()%13)+18;
		
		while(j<i){
			
			if(idade[i] == idade[j]){
				j=0;
				idade[i] = (rand()%13)+18;
			
				
			}
			else{
				j++;
			}
		}
	}
	
	for(k=0; k<10; k++){
		printf("%d\n", idade[k]);
	}
	
	
	return 0;
}
