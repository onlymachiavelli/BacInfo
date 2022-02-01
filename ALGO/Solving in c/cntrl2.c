#include <stdio.h>
#include <stdbool.h>

char *boolString(bool var) { return (var ? "true" : "false"); }

int defN()
{
    int n;
    printf("Enter N ! \n");
    scanf("%d", &n);
    if ((400 < n) && (n < 1000))
        return n;
    return defN();
}
int defM(int n)
{
    int m;
    printf("Enter M \n");
    scanf("%d", &m);
    if ((n > m) && (m > 400))
        return m;
    return defM(n);
}

int isPrime(int n, int i)
{
    if (n > 1)
    {
        if (i >= n / 2)
            return true;
        if (n % i == 0)
            return false;
        return isPrime(n, i + 1);
    }
    return false;
}

char *primeStuffs(int n)
{
    int res = 1, i = 2;
    char *result, *fuck, *op = "";
    while (res != n)
    {
        printf("%s \n", result);
        if (isPrime(i, 2))
        {
            res *= i;
            sprintf(fuck, "%d *", i);
            // result += fuck;
            sprintf("%s %s ", result, fuck);
        }

        if (res + 1 == n)
        {
            op = "+";
            res++;
        }
        else
        {
            op = "-";
            res--;
        }

        i++;
    }
    // result = "#" + fuck + op + result ;
    sprintf(result, "# %s %s %s", fuck, op, result);
    return result;
}
int main()
{
    printf("fuck you");
    int q = 3;
    q += 4;
    printf("%d", q);
    int i;

    return 0;
}
