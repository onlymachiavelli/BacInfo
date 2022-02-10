
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
    int* datas;
    FILE* myFile = fopen(source, "rb");
    fread(datas, sizeof(datas), n, myFile);
    fclose(myFile);
    return datas;


}

void sync(char* source, Travelers* travelers, int n) {
    FILE* myFile = fopen(source, "wb");
    int* datas = chargeData(source, n);
    datas[n + 1] = travelers;
    fwrite(datas, sizeof(datas), n + 1, myFile);
    fclose(myFile);
}

