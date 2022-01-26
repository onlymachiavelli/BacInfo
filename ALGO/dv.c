#include <stdio.h>
#include <stdbool.h>

int size()
{
    int n;
    printf("Enter Number! \n ");
    scanf("%d", &n);
    if ((40 < n) && (n < 100))
    {
        return n;
    }
    return size();
}

main()
{
}
