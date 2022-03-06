#include<stdio.h>
#include <stdbool.h>
#include <string.h>

int main() {
    FILE* myFile = fopen("toCrypt.txt", "r");
    char* line;
    while (fgets(line, sizeof(line), myFile)){
        printf(line);
    }
    fclose(myFile);
    return 0;
}