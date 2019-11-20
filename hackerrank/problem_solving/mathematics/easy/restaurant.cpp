// https://www.hackerrank.com/challenges/restaurant/problem


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
    int n, l, b, resp;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>l>> b;
        resp= b*l/(gcd(b,l)*gcd(b,l));
        cout<< resp<<endl;
    }
  
    return 0;
}
