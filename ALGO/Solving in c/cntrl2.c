#include <stdio.h>;
#include <stdbool.h>;

char *boolString(bool var){ return (var ? "true" : "false");}

int defN() {
    int n ;
    printf("Enter N ! \n");
    scanf("%d", &n) ;
    if ((400 < n) && ( n<  1000))return n;
    return defN();
}
int defM(int n ) {
    int m ;
    printf("Enter M \n");
    scanf("%d", &m);
    if ((n>m) && (m>400)) return m ;
    return defM(n);
}

int isPrime(int n , int i ){
    if (n > 1 ) {
        if (i >= n/2 ) return true;
        if (n%i == 0) return false;
        return isPrime(n, i+1);
    }
    return false ;
}

char *primeStuffs(int n){
    int res = 1, i=2 ;
    char*result , fuck;
    char op[1]= "";
    while (res!= n){
        if (isPrime(i, 2)){
            res *= i;
            sprintf(fuck, "%d *", i);
            result += fuck ;
        }

        if (res+1 == n ){
            op[0] = "+";
            res++;
        }
        else {
            op[0]= "-";
            res -- ;
        }



        i++;
    }
    result = "#" + fuck + op + result ;
    return result;
}
int main () {

    printf("%s /n", boolString(isPrime(9, 2)));
    int n = defN(), m = defM(n);


    int i ;
    for (i = m; i<=n;i++){
        printf("%s \n" ,  primeStuffs(i));
    }
    return 0;
}
