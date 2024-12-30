// HackerRank
// digit_frequency.c

/*
Sample Input 1
lw4n88j12n1

Sample Output 1
0 2 1 0 1 0 0 0 2 0 

Sample Input 2
1v88886l256338ar0ekk

Sample Output 2
1 1 1 2 0 1 2 0 5 0 
*/

#include <stdio.h>
#include <string.h>

int main() {
    char s[1000];
    int freq[10] = {0}; 

    scanf("%[^\n]", s); 
    for (int i = 0; i < strlen(s); i++) {
        if (s[i] >= '0' && s[i] <= '9') {
            freq[s[i] - '0']++;
        }
    }

    for (int i = 0; i < 10; i++) {
        printf("%d ", freq[i]);
    }
    
    return 0;
}
