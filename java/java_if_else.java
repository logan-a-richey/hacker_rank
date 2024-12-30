/*******************************************************************************
HackerRank - Java Tutorial
java_if_else.java
*******************************************************************************/

/*
# TASK:
For a positive integer n, if n is odd, print "Weird".
If n is even and in the range [2, 5], print "Not Weird".
If n is even and in the range [6, 20], print "Weird".
If n is even and greater than 20, print "Not Weird".

# INPUT 1:
3

# OUTPUT 1:
Weird

# INPUT 2:
24

# OUTPUT 2:
Not Weird
*/

import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read the integer n
        int n = scanner.nextInt();
        
        // Check if n is odd
        if (n % 2 == 1) {
            System.out.println("Weird");
        } else {
            // n is even, check the given ranges
            if (n >= 2 && n <= 5) {
                System.out.println("Not Weird");
            } else if (n >= 6 && n <= 20) {
                System.out.println("Weird");
            } else if (n > 20) {
                System.out.println("Not Weird");
            }
        }
        
        // Close the scanner
        scanner.close();
    }
}


