/*******************************************************************************
HackerRank - Java Tutorial
java_loops_1.java
*******************************************************************************/

/*
TASK:
Print out the first 10 lines of the multiplication table for an integer `n`.

INPUT 1:
2

OUTPUT 1:
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
*/

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        
        // read in integer `n`:
        int my_int = Integer.parseInt(bufferedReader.readLine().trim());
        bufferedReader.close();
        
        // Print multiplication table for `n` using a for loop:
        for (int i = 1; i <= 10; i++) {
            System.out.println(my_int + " x " + i + " = " + (my_int * i));
        }
    }
}

