// https://www.hackerrank.com/challenges/sherlock-and-counting/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int t;
    long n, k;
    cin>>t;
    long long solucion;
    double pa,pb;
    long long int inta, intb;
    long long int sumleft,sumright;
    for(int cases=0;cases<t;cases++){
        cin>>n>>k;
        
        if(n-4*k<=0){
            //entregue n-1
            //cout<<"Entr[e aca   "<<endl;
            solucion= n-1;   
            cout<<solucion<<endl;
        }else{
            pa= (n-sqrt(n*n-4*k*n)+0.0)/(2);
            pb= (n+sqrt(n*n-4*k*n)+0.0)/(2);
            inta=floor(pa);
            intb=ceil(pb);
            if(inta>=1){
                sumleft = inta;
            }else{
                sumleft = 0;
            }

            if(n-intb>=0){
                sumright = n-intb;
            }else{
                sumright = 0;
            }
            solucion= sumleft+sumright;
            //cout<<pa<< endl;
            //cout<<pb<< endl;
            cout<<solucion<< endl;
        }
    }
    
    return 0;
}