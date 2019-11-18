// https://www.hackerrank.com/challenges/difference-and-product/submissions

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool parejaDiferente(double x1, double y1, double x2, double y2){
    bool resp;
    if( (x1!=x2) || (y1!=y2)){
        resp = true;
    }else{
        resp = false;
    }
    return resp;
}
bool parejaEntera(double x1, double y1){
    bool resp;
    if( (x1==floor(x1)) && (y1==floor(y1))){//if both x1 and y1 are integers
        resp= true;
    }else
        resp = false;
    return resp;
}
bool parejaValida(double x1, double y1, long long int D, long long int P){
    double dif, product;
    dif=abs(x1-y1);
    product = x1*y1;
    bool resp = (parejaEntera(x1, y1) && dif == D && product ==P)? true : false;
    return resp;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int t, cont;
    long long int D, P;
    double a11, a12, a21, a22, b11, b12, b21, b22, disc;
    int validas[4];
    cin>>t;
    for(int i=0;i<t;i++){
        cin>>D>>P;
        cont =0;
        for(int k=0;k<4;k++){
            validas[k]=0;
        }
        disc= pow(D, 2)+4*P;
        if(D<0 || disc<0){
            cont =0;
        }else{
            b11 = (sqrt(disc)+0.0)/2-(D+0.0)/2;
            b12 = -(sqrt(disc)+0.0)/2-(D+0.0)/2;
            a11 = D+b11;
            a12 = D+b12;
                       
            b21 = (sqrt(disc)+0.0)/2+(D+0.0)/2;
            b22 = -(sqrt(disc)+0.0)/2+(D+0.0)/2;
            a21 = b21-D;
            a22 = b22-D;
            
            if(parejaValida(a11, b11, D, P)){
                validas[0]=1;
            }
            
            if(parejaValida(a12, b12, D, P) && parejaDiferente(a12, b12, a11, b11) ){
                validas[1]=1;
            }
            
            if(parejaValida(a21, b21, D, P) && parejaDiferente(a21, b21, a11, b11) && parejaDiferente(a21, b21, a12, b12)){
                validas[2]=1;
            }
            
            if(parejaValida(a22, b22, D, P) && parejaDiferente(a22, b22, a11, b11) && parejaDiferente(a22, b22, a12, b12) &&parejaDiferente(a22, b22, a21, b21)){
                validas[3]=1;
            }
            for(int k=0;k<4;k++){
                cont=cont+validas[k];
            }
        }
        cout<<cont<<endl;
    }
    return 0;
}
