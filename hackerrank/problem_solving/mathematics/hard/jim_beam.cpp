// https://www.hackerrank.com/challenges/jim-beam/submissions/code/22614129

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

double distancia(double x1, double y1, double x2, double y2){
    double dist= sqrt(pow(x1-x2,2)+pow(y1-y2,2));
    return dist;
}
double direccion(double xfin, double yfin){
    //double pi =3.14159265;
    double result = atan2 (yfin,xfin) ;
    return result;
}
double rotarPuntoX(double x, double y, double angulo){
    double xp;
    xp = x*cos(angulo)-y*sin(angulo);
    return xp;
}
double rotarPuntoY(double x, double y, double angulo){
    double yp;
    yp = x*sin(angulo)+y*cos(angulo);
    return yp;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int t, x1,y1,x2,y2,xm,ym;
    double mw, bw,mm, xmin, xmax, xintersection,yintersection, directionmirror, directionintersection;
    int auxx1, auxx2, auxy1, auxy2, auxxm, auxym;
    cin>>t;
    for(int T=0;T<t;T++){
        cin>>x1>>y1>>x2>>y2>>xm>>ym;  
        
        //verificar que esto sea posible, que x1!=x2
        /*if(x1==x2){
            //se cambia todo para que funcione
            cout<<T<<"  el muro es vertical"<<endl;
            auxx1=x1;
            auxy1=y1;
            auxx2=x2;
            auxy2=y2;
            auxxm=xm;
            auxym=ym;
            x1=auxy1;
            y1=auxx1;
            x2=auxy2;
            y2=auxx2;
            xm=auxym;
            ym=auxxm;
        }*/
        if((x1==x2)||xm==0){
            do{  
                //cada punto moverlo un grado hacia algun lado.

                x1=rotarPuntoX(x1, y1, 5);
                y1=rotarPuntoY(x1, y1, 5);

                x2=rotarPuntoX(x2, y2, 5);
                y2=rotarPuntoY(x2, y2, 5);

                xm=rotarPuntoX(xm, ym, 5);
                ym=rotarPuntoY(xm, ym, 5);                      
            }while((x1==x2)||xm==0);
            
        }
        
        xmin=min(x1, x2);
        xmax=max(x1, x2);
        //verificación que esto sea posible que xm!=0;
        mm= (ym+0.0)/xm;
        mw= (y2-y1+0.0)/(x2-x1);
        bw=-mw*x1+y1;
        //verificar que esto sea posible, que mm!=mu;
        if(mw!=mm){
            xintersection = (bw+0.0)/(mm-mw);
            yintersection = mm*xintersection;
            directionmirror=direccion(xm,ym);
            directionintersection=direccion(xintersection, yintersection);
            //cout<<"xintersection  " <<xintersection <<"   yintersection  " <<yintersection <<endl;
            //cout<<" espejo   "<<directionmirror <<"  intersection   "<< directionintersection <<endl<<endl;
            if(abs(directionmirror-directionintersection)>0.0001){
                //cout<<"entro aca"<<endl;
                cout<<"YES"<<endl;
            }else if(xintersection<xmin||xintersection>xmax){//si la intersección no pertenece a la recta
                cout<<"YES"<<endl;
            }else if(distancia(xintersection, yintersection,0,0)<=distancia(xm, ym,0,0)){
                cout<<"NO"<<endl;
            }else{
                cout<<"YES"<<endl;
            }
        }else{//las pendientes son iguales mu=mm
            //puede que estén en la misma recta o puede que no
            //verificar si están en la misma recta evaluando x1 en y=mmX, si resultado = y1 sí están en la misma recta
            if((mm*x1) == y1){
                //cout<<T<<" Están en la misma recta "<<endl;
                if(abs(xm)<abs(x1)&&abs(xm)<abs(x2)){
                    cout<<"YES"<<endl;
                }else{
                    cout<<"NO"<<endl;
                }
                
            }else{
                cout<<"YES"<<endl;
            }
        }
    } 
    return 0;
}