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

Main(){
    float ep = 0.000001;
    cout << pi(ep);
    return 1 ;
}