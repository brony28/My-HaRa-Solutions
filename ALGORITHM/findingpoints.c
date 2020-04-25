#include<stdio.h>


int main() {
  int px[10], py[10], qx[10], qy[10], rx, ry, n, i;

  printf("Enter no of iterations");
  scanf("%d", &n);
  printf("Enter the coordinates");
for (i = 0; i < n; i++) {
   
   scanf("%d%d%d%d",&px[i],&py[i],&qx[i],&qy[i]);
}
  for (i = 0; i < n; i++) {
   // printf("Enter the coordinates");
   //scanf("%d%d%d%d", &px, &py, &qx, &qy);
    rx = 2 * qx[i] - px[i];
    ry = 2 * qy[i] - py[i];
    printf("%d\t",rx);
	
    printf("%d\n",ry);
	
  }

  return 0;
}