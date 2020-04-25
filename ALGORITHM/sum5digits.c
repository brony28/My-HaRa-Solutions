#include<stdio.h>
int main(){
    int p=0,a,n,m=0;

    scanf("%d",&a);
    n =a;
    while (n != 0)
   {
      
      m =  n%10;
      n  = n/10;
      p += m;
   }
    printf("%d",p);
    return 0;
}
