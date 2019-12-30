#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

// https://www.hackerrank.com/challenges/find-point/problem

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n;
    int x1, y1, x2, y2;
    double x1n, y1n;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>x1>>y1>>x2>>y2;
        x1n = x1+(x2-x1)*2;
        y1n = y1+(y2-y1)*2;
        
        cout<<x1n<<" "<<y1n<<endl;
    }
    
    return 0;
}
