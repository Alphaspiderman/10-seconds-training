#include <stdio.h>
// For a given number, return the sum of the 3rd, 4th digit without using extra variables
void main(){
    int n = 5321641;
    while(n > 9999){
        n = n / 10;
    }
    printf("%d\n", n % 10 + (n / 10) % 10);
}