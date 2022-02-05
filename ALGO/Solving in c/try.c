#include <stdio.h>
#include <string.h>
char *sub(char *myString, int from, int too)
{
    char *newString = "";
    for (int i = from; i <= too; i++)
    {
        newString += myString[i];
    }

    return newString;
}

char *shit(int n, char *suite, int i)
{
    char *toReturn;
    if (n > 0)
    {
        if (i < strlen(suite))
        {
            return 0;
        }
        return shit(n - 1, suite, 0);
    }
    return suite;
}

int main()

{
    char *name = "alaa barka";
    printf("Hello world \n");
    printf("%s", sub(name, 1, 5));
    return 0;
}