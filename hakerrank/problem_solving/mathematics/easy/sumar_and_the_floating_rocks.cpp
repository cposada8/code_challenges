// https://www.hackerrank.com/challenges/harry-potter-and-the-floating-rocks/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    long int  x1, y1, x2, y2, dy, dx, resp;
    cin >>t;
    
    for(int n=0;n<t;n++){
        cin>>x1>> y1>> x2>> y2;
        //case wen x1==x2
        dy=y1-y2;
        dx=x1-x2;
        resp = gcd(abs(dy), abs(dx))-1;
        
        cout<<resp<<endl;
        
    }
    
    return 0;
}
