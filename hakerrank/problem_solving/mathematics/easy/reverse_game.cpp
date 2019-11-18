// https://www.hackerrank.com/challenges/reverse-game/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t, n, k, actualK;
    cin>>t;
    for(int cases=0;cases<t;cases++){
        cin>>n>>k;
        
        int arregloMayores [n];
        int arregloMenores [n];
        int arregloDefinit [n];
        for(int i=0;i<n;i++){
            arregloMenores[i]=i;
            arregloMayores[i]=n-1-i;
        }
        int contMayores=0;
        int contMenores=0;
        for(int i=0;i<n;i++){
            if(i%2==0){
                arregloDefinit[i]=arregloMayores[contMayores];
                contMayores++;

            }else{
                arregloDefinit[i]=arregloMenores[contMenores];
                contMenores++;
                
            }
        }
        
        for(int i=0;i<n;i++){
            if(arregloDefinit[i]==k){
                cout<<i<<endl;
                break;
            }
            
        }

    }
    return 0;
}
