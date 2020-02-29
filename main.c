#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	int dizi[8]={4,-3,5,-2,-1,2,6,-2};
	int i,j;
	int max=0;
	int sum=0;
	for(i=0;i<8;i++){
		for(j=i+1;j<8;j++){
			sum=sum+dizi[j];
			if(max<sum){
				max=sum;
			}
		}
		sum=0;
		
	}
	
	printf("maximum alt dizi=%d",max);
	
	
	return 0;
}
