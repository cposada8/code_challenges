// https://www.hackerrank.com/challenges/strange-grid/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    long long int r, resp, n;
    int c;
    cin>>r>>c;
    if(r%2==0){
        n=r/2;
        resp= 2*c-1+10*(n-1);
    }else{
        n=(r+1)/2;
        resp= 2*(c-1)+10*(n-1);
    }
    cout<<resp<<endl;
    return 0;
}
