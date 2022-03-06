#include<stdio.h>
#include <stdbool.h>
#include <string.h>

void fillMatrix(char* source, int l, int c, char matrix[l][c]) {
    FILE* myFile = fopen(source, "r");
    char* line;
    int i = 0, j = 0;
    while (fgets(line, sizeof(line), myFile)){
        for (int k = 0;k < strlen(line);k++) {
            matrix[i][j] = line[k];
            j++;
            if (j == c) {
                j = 0;
                i++;
            }
        }
    }

    fclose(myFile);

}
int main() {

    int l, c;
    char matrix[l][c];
    return 0;
}