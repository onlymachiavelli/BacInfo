#include <bits/stdc++.h>
using namespace std;
struct thePpcm{
        int a;
        int b ;
        int ppcm;
};

int size() {
    int n;
    cout << "Enter Size"  << endl;
    cin >> n;
    if (n<2 || n>100){
        return size();
    }
    return n;
}
int num(){
    return 0;
}
void fillFile(FILE * myFile, int n ){
    thePpcm obj;
    for (int i=0;i<n;i++){
        obj.a = num();
        obj.b = num();
    }   
}
int main (){
    FILE *myFile = fopen("ppcm.bin", "wb");
    
    int n = size();
    fclose(myFile);
    
}
