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
char *boolFuck(bool func)
{
    return (func ? "true" : "false");
}

bool isPrime(int n, int i)
{
    if (n > 1)
    {
        if (i <= n / 2)
        {
            if (n % i == 0)
                return false;
            return isPrime(n, i + 1);
        }
        return true;
    }
    return false;
}
void superPrime()
{
}
main()
{
    printf("%s ", boolFuck(isPrime(4, 2)));
}
