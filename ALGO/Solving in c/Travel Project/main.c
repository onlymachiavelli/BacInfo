#include <stdio.h>

typedef struct Traverlers
{
    char *ID;
    char *name;
    char *adress;
    char *totalTravels;

} Traverlers;
int travelers(char *source)
{

    FILE *shit;
    int n = 0;
    shit = fopen("data.dat", "rb");
    if (shit != NULL)
    {
    }

    return n;
}

int main()
{
    int answer;
    char *menu = "The menu : \n 1:Total travelers \n 2:Add traveler \n 3:charge Datas \n ";
    return 0;
}
