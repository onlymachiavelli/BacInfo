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


float form(int x) {
    return (2*x/(2*x-1))*(2*x/(2*x+1));
}
float wallis(float ep) {

    int n = 3;
    float s = form(1);
    float s1 = s*form(2);
    do {
        s = s1;
        s1 *= form(n) ;
        n++;
    }
    while(s1*2-s*2 > ep) ;
    return s1*2 ;
}

Main(){
    float ep = 0.00001;
    cout << wallis(ep);
    return 1 ;
}