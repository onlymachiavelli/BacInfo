
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

int* chargeData(char* source, int  n){
    Travelers* datas;
    FILE* myFile = fopen(source, "rb");
    fread(datas, sizeof(datas), n, myFile);
    fclose(myFile);
    return datas;


}

/*
void syncDatas(char* source, Travelers* travelers, int n) {
    FILE* myFile = fopen(source, "wb");
    int* datas = chargeData(source, n);
    n += 1;
    datas[n] = travelers;
    fwrite(datas, sizeof(datas), n + 1, myFile);
    fclose(myFile);
}
*/
int findTraveler(Travelers* array, char* ID, int n) {
    int indice = -1;
    for (int i = 0;i < n;i++) if (ID == array[i].ID) indice = i;
    return indice;
}
void AddData() {

}