
#include <stdio.h>
#include<stdbool.h>

typedef struct  Travelers {
    char* ID;
    char* name;
    char* adress;
    int total;

}Travelers;


int totalTravelers(char* source)  {
    int total = 0;
    FILE* myFile = fopen(source, "rb");

    fclose(myFile);
    return total;

}

