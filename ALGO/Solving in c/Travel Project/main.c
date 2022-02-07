#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include "funcs.h"
typedef struct Traverlers{
    char* ID;
    char* name;
    char* adress;
    int* totalTravels;

} Traverlers;
int TotalTravellers(char* source){

    FILE* shit;
    int n = 0;
    shit = fopen("data.dat", "rb");
    if (shit != NULL){
    }

    return n;
}

void fillTraveller(Traverlers* Object){
    bool check = false;
    while (!check){
        printf("Enter Id \n ");
        scanf(Object->ID);
        printf("Enter the name \n ");
        scanf(Object->name);
        printf("Enter adress \n");
        scanf(Object->adress);
        printf("Total Travels \n");
        scanf("%d", Object->totalTravels);
        check = strlen(Object->name) > 0 && strlen(Object->adress) > 0 && strlen(Object->ID) > 0 && Object->totalTravels >= 0;

    }
}
void saveDatas(char* source, Traverlers* Object, int n){

    FILE* myFile = fopen(source, "a");
    int pointer;
    fwrite(myFile, pointer, Object, n);

    fclose(myFile);

}

int findTraveler(Traverlers* Object, char* ID, int n) {
    int indice = -1;
    FILE* myFile = fopen("data.dat", "r");

    for (int i = 0;i < n;i++) {

    }
    fclose(myFile);
    return indice;
}
int main() {
    printf("%d \n", age());
    Traverlers dataHolder;
    int answer;
    char* source = "data.dat";
    int n;
    char* menu = "The menu :\n 1:Total travelers \n 2:Add traveler \n 3:charge Datas \n  4:Find Traveller \n 5:add traveller \n 6: Delete Traveller \n 7:Libr \n any alphabet quit ";
    printf("%s", menu);

    switch (answer){
    case 1:TotalTravellers(source);break;
    case 2:
        saveDatas(source, &dataHolder, n);break;
    case 3:break;
    }

    return 0;

}
