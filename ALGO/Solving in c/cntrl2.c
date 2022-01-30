#include <stdio.h>;
#include <stdbool.h>;

char *boolString(bool var) return var ? "true" : "false";

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


int main () {

    int n = defN(), m = defM(n);
    printf("hello world");
    return 0;
}
