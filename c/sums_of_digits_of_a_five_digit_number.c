// HackerRank
// sums_of_digits_of_a_five_digit_number.c

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

/*
Sample Input 0
10564

Sample Output 0
16
*/

int main() {
    int num, sum = 0;
    scanf("%d", &num);
    
    while(num != 0) {
        sum += num % 10;
        num /= 10;
    }
    
    printf("%d", sum);
}
