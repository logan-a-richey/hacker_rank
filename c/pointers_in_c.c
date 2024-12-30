// HackerRank
// pointers_in_c.c

#include <stdio.h>
#include <stdlib.h>

/*
Sample Input
4
5

Sample Output
9
1
*/

void update(int *a,int *b) {
    int sum,diff;
    sum = *a+*b;
    diff = abs(*a-*b);
    *a = sum;
    *b = diff;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);
    
    return 0;
}

