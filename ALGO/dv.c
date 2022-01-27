#include <stdio.h>
#include <stdbool.h>
typedef struct Numbers
{
    int num;
    bool isSuperPrime;

} Numbers;
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
bool isSuperPrime(int n)
{
    if (n > 1)
    {
        if (isPrime(n, 2))
            return isSuperPrime(n / 10);
        return false;
    }
    return true;
}
void saveResult(int n, int i, Numbers number)
{
    if (i <= n)
    {
        if (isPrime(i, 2))
        {
            number.num = i;
            number.isSuperPrime = isSuperPrime(i);
        }
    }
}
int main()
{
    printf("%s ", boolFuck(isSuperPrime(59399)));

    return 0;
}
