#include <bits/stdc++.h> 
using namespace std ;
#define Main int main


float pi(float e) {
    int i = 1;
    float  s=0, s1 = 0;
    do{
        s = s1;
        s1 += 1/pow(i,2);
        i +=1 ; 
    }
    while(abs(sqrt(s1*6) -sqrt(s*6))> e) ;

    return sqrt(s1*6);
}

float wallis(float ep) {

    int n = 3;
    float s = (2/1)*(2/3);
    float s1 = s+((2*2)/(2*2-1))*((2*2)/(2*2+1));
    do {
        s = s1;
        s1 += ((2*n)/(2*n-1)) *((2*n)/(2*n)/(2*n+1)) ;
        n++;
    }
    while(s1*2-s*2 > ep) ;
    return s1*2 ;
}

Main(){
    float ep = 0.00000001;
    cout << wallis(ep);
    return 1 ;
}