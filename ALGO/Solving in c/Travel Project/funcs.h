
#include <stdio.h>
#include<stdbool.h>
#include <string.h> 

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
void fillTraveler(Travelers* traveler) {
    printf("EEnter ID\n");
    scanf(&traveler->ID);
    printf("Enter Name\n");
    scanf(&traveler->name);
    printf("Enter Adress\n");
    scanf(&traveler->adress);
    printf("Enter total Travels\n");
    scanf("%d", &traveler->total);
    if ((strlen(traveler->ID) == 0) && (strlen(traveler->adress) == 0) && (strlen(traveler->name) == 0))  fillTraveler(&traveler);
}

void chargeData(char* source, int  n, Travelers array[]){
    Travelers* datas;
    FILE* myFile = fopen(source, "rb");
    fread(datas, sizeof(datas), n, myFile);
    fclose(myFile);


}


int findTraveler(Travelers* array, char* ID, int n) {
    int indice = -1;
    for (int i = 0;i < n;i++) if (ID == array[i].ID) indice = i;
    return indice;
}

void syncDatas(char* source, Travelers* travelers, int n) {
    FILE* myFile = fopen(source, "wb");
    int datas[100];
    chargeData(source, n, datas);
    n += 1;
    datas[n] = travelers;
    fwrite(datas, sizeof(datas), n + 1, myFile);
    fclose(myFile);
}

void addData(Travelers travelers, Travelers array[], int n){
    bool exist = false;

    for (int i = 0; i < n; i++) {
        if (array[i].ID == travelers.ID)
            printf("This traveler is already in the list  \n");
        exist = true;
        break;
    }
    if (!exist) {
        n++;
        array[n - 1] = travelers;
        printf("Added to the list ");

    }
}
void deletetTraveler(Travelers datas[], char* Id, int n) {
    FILE* myFile = fopen("shit.dat", "rb+");
    fread(&datas, sizeof(datas), n, myFile);
    for (int i = 0; i < n - 1; i++){
        if (datas->ID == Id) {
            for (int j = i; j < n - 1; i++) datas[j] = datas[j + 1];
            n = n - 1;
            printf("Deleted %s \n", datas[i].ID);
        }
    }
    fwrite(&datas, sizeof(datas), n, myFile);
    fclose(myFile);
}
void freeUp(Travelers* traveler) {
    traveler->ID = "";
    traveler->name = "";
    traveler->adress = "";
    traveler->total = 0;
    printf("Freed !\n");

}

