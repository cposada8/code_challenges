// https://www.hackerrank.com/challenges/easy-sum/submissions/code/22875868

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int t;
    long long int n, m, sum_mlessOne, entnm, resto, sumaresto, solucion;
    cin>>t;
    for(int i=0;i<t;i++){
        cin>>n>>m;
        sum_mlessOne= m*(m-1)/2;//sumation until m-1.
        entnm = (int)(n/m); //integer part of n/m.
        resto = n-entnm*m;
        sumaresto= resto*(resto+1)/2;
        solucion = sum_mlessOne*entnm+sumaresto;
        cout<<solucion<<endl;
    }
    return 0;
}
