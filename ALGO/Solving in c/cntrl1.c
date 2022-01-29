
#include <stdio.h>


int main (){

    FILE *test;
    test = fopen("test.dat", "wb");
    int a = 5;
    int b = 7;
    fprintf(a, b , a+b , test);

    fclose(test);


    test=  fopen("test.dat", "rb");
    char aa[70];
    while (fscanf(test, "%d %d %d", aa) != EOF){
        printf(a);
    }
    fclose(a);
    return 0 ;
}
