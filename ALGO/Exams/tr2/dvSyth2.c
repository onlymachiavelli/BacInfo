#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int size(int min, int max) {
    printf("Entert N \n");
    int n;
    scanf("%d", &n);
    if (n > min && n < max) return n;
    return size(min, max);

}
void fillMatrix(char* source, int l, int c, char matrix[l][c]) {
    FILE* myFile = fopen(source, "r");
    char* line;
    int i = 0, j = 0;
    bool entered = false;
    while (fgets(line, sizeof(line), myFile)){
        if (!entered) {
            entered = true;
        }
        else matrix[i][j] = '#';j++;
        for (int k = 0;k < strlen(line);k++){
            if (j == c) j = 0;i++;
            matrix[i][j] = line[k];
            j++;

        }


    }
    while (i < l && j < c) {
        matrix[i][j] = "*";
        j++;
        if (j == c){
            i++;
            j = 0;
        }
    }
    fclose(myFile);
}
char* fromDecimal(int code, int base) {
    if (code >= 0) {
        return snprintf(NULL, 0, "%d", code % base) + fromDecimal(code / base, base);
    }
    return "";
}
int* toDecimal(char* code, int base, int index) {
    if (strlen(code) > 0) {
        //
    }
    return 0;
}
int main() {

    int l, c;
    while (true) {
        l = size(7, 20);
        c = size(l, 20);
        if (l * c >= 60)  break;
    }

    char matrix[l][c];


}