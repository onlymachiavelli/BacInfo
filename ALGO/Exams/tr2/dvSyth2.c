#include <stdio.h>
#include <string.h>

int main() {
    FILE* shit = fopen("toCrypt.txt", "r");
    char* line;
    while (fscanf(shit, "%s", line) != EOF) {
        printf("%s \n", line);
        printf("%d", line == "\n");

    }
    fclose(shit);
}