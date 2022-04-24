#include <bits/stdc++.h> 
using namespace std ;
#define Main int main


float pi(float e) {

    int i = 1;
    float s = 0;
    float s1 =  1/(pow(i,2));
    do {    
        s = s1;
        s1 += 1/(pow(i,2));
    }while (abs(s*6-s1*6) > e) ;
    return s1 ;
}

Main(){
    float ep = 0.00001;
    cout << pi(ep);
    return 1 ;
}