// https://www.hackerrank.com/challenges/summing-the-n-series/submissions/code/21506192

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int t;
    cin>>t;
    long long int n, n2, nmodulo, modular;
    modular = 1000000007;
    for(int T=0;T<t;T++){
        cin>>n;
        nmodulo= n%modular;
        n2 = (nmodulo*nmodulo);
        cout<< n2 % modular <<endl;
    }
    return 0;
}

