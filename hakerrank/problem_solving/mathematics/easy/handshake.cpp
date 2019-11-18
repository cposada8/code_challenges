// https://www.hackerrank.com/challenges/handshake/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int t, n;
    cin>>t;
    for(int cases=0;cases<t;cases++){
        cin>>n;
        int resp = n*(n-1)/2;
        cout<<resp<<endl;
    }
    
    
    
    return 0;
}
