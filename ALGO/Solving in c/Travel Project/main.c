#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include "funcs.h"

#define Main int main
Main(){
    char* fileSource = "shit.dat";
    int dataSizes = 0;
    int answer;
    bool check;
    Travelers array[100];
    char* Menu = "Menu Control\n1:Total Traverlers\n2:Fill Traveler\n3:Charge Data\n4:Find Traveler\n5:Add Traveler\n6:Delete Traveler\n7:Libr\n";
    //show the menu
    printf(Menu);
    while (true){
        check = false;
        //verify the answer
        while (!check) {
            printf("Enter the option");
            scanf("%d", answer);
            check = answer >= 1 && answer <= 7;
        }
        if (answer < 9) {

            switch (answer) {
            case 1:totalTravelers(fileSource); break;

            case 2: break;

            case 3: break;

            case 4: break;

            case 5: break;

            case 6:
                break;

            case 7:
                break;

            }
        }
        else printf("Clossing the program\n"); break;
    }
    return 0;



}