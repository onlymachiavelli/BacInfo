#include <stdio.h>;
#include <stdbool.h>;


int defN() {
    int n ;
    printf("Enter N ! \n");
    scanf("%d", &n) ;
    if (400 < n <  1000) return n;
    else return defN();
}
int defM(int n ) {
    int m ;
    return m ;
}

int main () {

    int n = defN();
    printf("hello world");
    return 0;
}
