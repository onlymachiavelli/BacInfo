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
    FILE* myFile = open(source, "r");
    char* line;
    int i = 0, j = 0;
    while (fgets(line, sizeof(line), myFile)){
        for (int k = 0;k < strlen(line);k++){
            i += 0;
        }
    }
    fclose(myFile);
}
int main() {

    FILE* file = open("toCrypt.txt", "r");
    char* line;
    bool check;
    while (fgets(line, sizeof(line), file)){
        if (line[strlen(line)] == "\n"){
            printf("Yes @ \n");
        }
        else {
            printf("nope");
        }
    }
    fclose(file);
    //shits
    int l, c;
    while (true) {
        l = size(7, 20);
        c = size(l, 20);
        if (l * c >= 60)  break;
    }

    char matrix[l][c];


}