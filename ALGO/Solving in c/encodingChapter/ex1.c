#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
int random(int lower , int higher){
    int toReturn = 0;
    if (higher > lower ) toReturn = rand() % (higher - lower +1 ) + 1 ;
    return toReturn; 
}
char *getString(int code , int base)  {
    
     
}
int getNumber(char *code , int base){}
int main () {
    srand(time(0));
    for(int i=0;i<6;i++) printf("%d \n" ,  random(20, 99) );
}