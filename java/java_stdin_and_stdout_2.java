/*******************************************************************************
HackerRank - Java Tutorial
java_stdin_and_stdout_2.java
*******************************************************************************/

/*
# INPUT 1:
42
3.1415
Welcome to HackerRank's Java tutorials!

# OUTPUT 1:
String: Welcome to HackerRank's Java tutorials!
Double: 3.1415
Int: 42
*/

import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        // read in an int, double, string:
        // read in 1st line:
        int my_int = scan.nextInt();
        
        // read in 2nd line:
        double my_double = scan.nextDouble();
        // scan the \n char from the my_double line
        scan.nextLine();
        
        // read in the 3rd line:
        String my_string = scan.nextLine();
        
        // print out the three variables:
        System.out.println("String: " + my_string);
        System.out.println("Double: " + my_double);
        System.out.println("Int: " + my_int);
    }
}
