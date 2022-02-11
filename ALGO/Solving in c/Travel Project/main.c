#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include "funcs.h"

#define Main int main
Main(){

    char* Id, fileSource = "shit.dat";
    int answer, dataSizes = 0;
    bool check, quit = false;
    Travelers array[100], trData;
    char* Menu = "Menu Control\n1:Total Traverlers\n2:Fill Traveler\n3:Charge Data\n4:Find Traveler\n5:Add Traveler\n6:Delete Traveler\n7:Libr\n";
    printf(Menu);
    do{
        check = false;
        //verify the answer
        while (!check) {
            printf("Enter the option : ");
            scanf("%d", &answer);
            check = ((answer >= 1) && (answer <= 8)) ? true : check;
        }
        if (answer < 8) {

            switch (answer) {
            case 1:totalTravelers(fileSource); break;
            case 2:fillTraveler(&trData);break;
            case 3:
                chargeData(fileSource, dataSizes, array);
                for (int i = 0; i < dataSizes; i++) printf("Name:%s\nID:%s\nAdress:%s\nTotal%d\n", array[i].name, array[i].ID, array[i].adress, array[i].total);
                break;
            case 4:
                printf("Enter ID \n");
                scanf(&Id);
                printf("%d", findTraveler(array, Id, dataSizes));
                break;
            case 5:
                addData(trData, array, dataSizes);
                break;

            case 6:
                printf("Enter traveler ID\n");
                scanf(&Id);
                deletetTraveler(&array, Id, &dataSizes);
                break;

            case 7:
                freeUp(&trData);
                break;

            }
        }
        else printf("Closing the program\n"); quit = true;
    } while (!quit);


    return 0;

}

/*


    FILE* myFile = fopen("test.dat", "wb");
    int age = 20;
    fwrite(&age, 1, sizeof(age), myFile);
    fclose(myFile);

    myFile = fopen("test.dat", "rb");
    int shit[1];
    fread(shit, sizeof(shit), 1, myFile);
    printf("%d", shit[0]);
    fclose(myFile);

*/