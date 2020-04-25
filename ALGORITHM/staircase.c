/*#include <stdio.h>
int main() {
  int n, i, j;

  scanf("%d", &n);

  for (i = 1; i <= n; i++) {
    for (j = 1; j <= n; j++) {
      if (i + j >= n) {
        printf("#");
      } else {
        printf(" ");
      }
    }
    printf("\n");
  }
  return 0;
}
*/

#include <stdio.h>
#include<string.h>
int main() {
  int n, i, j,k;

  scanf("%d", &n);

  for (i = 0; i < n; i++) {
     for (j = 0; j <n-1; j++) {
         printf(" ");
      } 
     for(k = 0; k < i; k++) {
         printf("#");
      }
      printf("\n");
   }
   return 0;
}
  


