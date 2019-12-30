// https://www.hackerrank.com/challenges/possible-path/problem

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
    long int a,b,x,y;
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
        cin>>a>>b>>x>>y;
        if(gcd(abs(a),abs(b))==gcd(abs(x),abs(y))){
            cout<<"YES"<<endl;
        }else{
            cout<<"NO"<<endl;
        }
    }
    return 0;
}
