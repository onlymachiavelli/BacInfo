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

void randomDecimal(int n) {
    FILE *myFile = fopen("dec.txt", "w") ;
    for (int i=0;i<n;i++)fprintf(myFile, "%d \n" , random(99, 999));
    fclose(myFile); 

}
int getNumber(char *code , int base){}
int main () {
    srand(time(0));
    int n =  random(10,30);
    randomDecimal(n);
}