// https://www.hackerrank.com/challenges/is-fibo/submissions/code/22405458

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int nfb=55;
    unsigned long int fibo[nfb];
    fibo[0]=1;
    fibo[1]=1;
    for(int i=2;i<nfb;i++){
        fibo[i]=fibo[i-1]+fibo[i-2];
    }
    long long int T,n;
    cin>>T;
    bool esfibo;
    for(int t=0;t<T;t++){
        cin>>n;
        esfibo=false;
        for(int i=0;i<nfb;i++){
            if(n==fibo[i]){
                esfibo=true;
                break;
            }
            //if(fibo[i]>n){
            //    break;
            //}
        }
        if(esfibo==true){
            cout<<"IsFibo"<<endl;
        }else{
            cout<<"IsNotFibo"<<endl;
        }
        
    }
    return 0;
}