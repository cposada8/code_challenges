// https://www.hackerrank.com/challenges/circle-city/problem

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t,r,k;
    int contEnt;
    double y;
    cin>>t;
    for(int cases=0;cases<t;cases++){
        cin>>r>>k;
        double rmax= (sqrt(r));
        contEnt=0;
        for(int i=0;i<rmax;i++){
            y= sqrt(r-pow(i,2));
            if(round(y)==y){
                contEnt++;
            }
        }
        if(contEnt*4<=k){
            cout<<"possible"<<endl;
        }else{
            cout<<"impossible"<<endl;
        }       
    }
    return 0;
}
