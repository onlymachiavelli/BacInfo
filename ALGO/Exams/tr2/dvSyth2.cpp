#include <bits/stdc++.h>

using namespace std ;

int size() {
    return 0;
}
void fillMatrix() {}
#define Main int main 

Main (){
    cout << "hello world" << endl;
    int n = 0;
    vector<vector<char>> matrix;
    FILE *myFile = fopen("toCrypt.txt", "r") ;
    char * line ; 
    string lines ;
    while (fscanf(myFile, line) != EOF) {
        cout << line << endl;   
        lines += line ;
    }
    fclose(myFile);
    cout << lines  << endl;

    
}   