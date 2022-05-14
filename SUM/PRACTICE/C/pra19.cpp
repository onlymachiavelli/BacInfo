#include <bits/stdc++.h>
using namespace std;
struct thePpcm{
        int a;
        int b ;
        int ppcm;
};

int size() {
    int n;
    cin >> n;
    if (n<2 || n>100){
        return size();
    }
    return n;
}
void fillFile(FILE * myFile, int n ){
    
}
int main (){
    FILE *myFile = fopen("ppcm.bin", "wb");
    

    fclose(myFile);
    
}
