// https://www.hackerrank.com/challenges/rectangular-game/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin>>n;
    
    long x;
    long y;
    long minx=1000000;
    long miny=1000000;
    
    for(int moves=0;moves<n;moves++){
        cin>>x>>y;
        if(x<minx){
            minx=x;
        }
        if(y<miny){
            miny=y;
        }
    }
    
    long long result= minx*miny;
    cout<<result<<endl;
    
    
    return 0;
    
}
