// HackerRank
// students_marks_sum.c

#include <stdio.h>
#include <stdlib.h>

/*
Sample Input 2
1
5
g

Sample Output 2
0
*/

//Complete the following function.
int marks_summation(int* marks, int number_of_students, char gender) {
    int sum = 0;

    /*
    Start index is determined by gender:
    'b' for boys starts at index 0
    'g' for girls starts at index 1.
    If gender is invalid, the loop doesn't execute.
    */
    
    for (int i = (gender == 'b' ? 0 : gender == 'g' ? 1 : -1); i < number_of_students; i += 2) {
        sum += marks[i];
    }
    return sum; // Return the calculated sum
}

int main() {
    int number_of_students;
    char gender;
    int sum;
  
    scanf("%d", &number_of_students);
    int *marks = (int *) malloc(number_of_students * sizeof (int));
 
    for (int student = 0; student < number_of_students; student++) {
        scanf("%d", (marks + student));
    }
    
    scanf(" %c", &gender);
    sum = marks_summation(marks, number_of_students, gender);
    printf("%d", sum);
    free(marks);
 
    return 0;
}
