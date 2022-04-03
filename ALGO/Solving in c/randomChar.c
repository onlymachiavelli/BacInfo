#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
int size() {
    int n;
    while (true) {
        printf("Enter the size of the File ");
        scanf("%d", &n);
        if (n >= 5 && n <= 20) {
            return n;
        }
        printf("Invalid size.\n");
    }
}
void fillFile(char* source, int n){
    srand(time(NULL));
    FILE* myFile = fopen(source, "w");
    if (myFile == NULL) {
        printf("Error opening file!\n");
        exit(1);
    }
    else {
        for (int i = 0; i < n; i++) {
            fprintf(myFile, "%c \n", rand() % 26 + 97);
        }
        fclose(myFile);
    }
    fclose(myFile);
}

void getDatas(char* source, int n) {
    FILE* myFile = fopen(source, "r");
    char* line;
    if (myFile == NULL) {
        printf("Error opening file!\n");
        exit(1);
    }
    else {
        for (int i = 0; i < n; i++) {
            fscanf(myFile, "%c \n", &line);
            printf("%c \n", line);
        }
        fclose(myFile);
    }
}
int main() {
    int n = size();
    char* src = "lettres.txt";
    fillFile(src, n);
    getDatas(src, n);

    return 1;
}