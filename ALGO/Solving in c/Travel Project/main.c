#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include "funcs.h"

#define Main int main
Main(){

    char* fileSource = "shit.dat";
    int dataSizes = 0;
    int answer;
    bool check, quit = false;
    Travelers array[100];
    Travelers trData;
    char* Menu = "Menu Control\n1:Total Traverlers\n2:Fill Traveler\n3:Charge Data\n4:Find Traveler\n5:Add Traveler\n6:Delete Traveler\n7:Libr\n";
    //show the menu
    printf(Menu);
    while (!quit){
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
            case 3: break;

            case 4: break;

            case 5: break;

            case 6:
                break;

            case 7:
                break;

            }
        }
        else printf("Closing the program\n"); quit = true;
    }
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