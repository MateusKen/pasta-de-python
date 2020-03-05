----------------------------------------------------------------------------------------------------
#include <iostream>
using namespace std;
int main(){
    cout<< "Hello World";
    return 0;
}
----------------------------------------------------------------------------------------------------
#include <iostream>
using namespace std;
float a,b,op;
float r;
int main(){
    cin>>a>>b>>op;
    if(op==1){
        r=a+b;
    }else{
        r=a-b;
    }
    if(op==3){
        r=a*b;
    }else if(op>=4){
        r=a/b;
    }
    cout<<r;
    return 0;
}
------------------------------------------------------------------------------------------------------
#include <iostream>
#include <math.h>
using namespace std;
int a,b,op;
float r;
int main(){
    cin>>a>>b>>op;
    if(op==1)r=a+b;
    else if(op==2)r=a-b;
    else if(op==3)r=a*b;
    else if(op==4)r=(float)a/b;
    else if(op==5)r=sqrt(a);
    else if(op==6)r=pow(a,(float)1/b);
    cout<<r;
    return 0;
}
--------------------------------------------------------------------------------------------------------
