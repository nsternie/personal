#include <stdio.h>
#include <stdint.h>
#include <stdlib.h> 

FILE* logfile;
FILE* raw;

int main(){

	while(1){
		logfile = fopen("speedslog.csv", "a")
		system("speedtest-cli --simple > temp.log");
		
	}
	



	printf("ARRAY_LENGTH was %d\r\n", ARRAY_LENGTH);
	system("speedtest-cli --simple > speedtest.log");
	return 0;
}