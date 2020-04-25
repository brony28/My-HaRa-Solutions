#include<stdio.h>
int main(){
    int t,n[100],i,a[100];
    scanf("%d",&t);
    for(i=0;i<t;i++){
        scanf("%d",&n[i]);
    }
    for (i = 0; i < t; i++) {
      a[i] = n[i]+ 1;
      printf("%d\n", a[i]);
    }
   
    return 0;
}

