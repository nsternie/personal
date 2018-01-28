#include <stdio.h>
#include <stdint.h>
#include <stdlib.h> 

#define ARRAY_LENGTH 5

uint8_t arr[ARRAY_LENGTH];

int main(){
	for(int n = 0; n < ARRAY_LENGTH; n++){
		arr[n] = 2*n;
	}
	printf("ARRAY_LENGTH was %d\r\n", ARRAY_LENGTH);
	system("speedtest-cli --simple > speedtest.log");
	return 0;
}