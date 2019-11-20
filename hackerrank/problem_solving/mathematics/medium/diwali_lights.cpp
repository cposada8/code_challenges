https://www.hackerrank.com/challenges/diwali-lights/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t,n;
    int resp;
    cin>>t;
    for(int i=0;i<t;i++){
        cin>>n;
        resp=1;
        for(int k=0;k<n;k++){
            resp=resp*2;
            resp=resp%100000;
        }
        resp--;   
        cout<<resp<<endl;
    }
    return 0;
}
