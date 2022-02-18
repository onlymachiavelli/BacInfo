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
int toDecimal(char *code, int base, int i){
    if (i < strlen(code)) {
        return (atoi(code[i]) * pow(base, strlen(code) -i-1)) + toDecimal(code / basde , base , i+1) ;
    }
    return 0; 
}
char *fromDec(int code, int base) {
    
    if (code >= 0 ) return fromDec(code / base, base) +  code%base  ;
    return "";
}
int getNumber(char *code , int base){}
int main () {
    printf("%d", toDecimal("1011100100", 2, 0)) ;
    srand(time(0));
    int n =  random(10,30);
    randomDecimal(n);
}