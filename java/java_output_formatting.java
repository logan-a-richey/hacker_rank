/*******************************************************************************
HackerRank - Java Tutorial
java-output-formatting.java
*******************************************************************************/
/*
## TASK:
Read in 3 lines and format print the data correctly:
Divider line consisting of 32 '=' characters.
The next 3 lines formated as follows:
    string left-alligned by 15 characters, fill with ' '
    integer right-alligned 3 characters, fill with '0'
Divider line consisting of 32 '=' characters.

## INPUT 1:
java 100
cpp 65
python 50

## OUTPUT 1:
================================
java           100 
cpp            065 
python         050 
================================
*/

import java.util.Scanner;

public class Solution {
    // Method to print the divider line
    public static void printDiv() {
        System.out.println("================================");
    }
    
    // Method to handle the formatted printing of each line
    private static void printFormatted(String line) {
        String[] parts = line.split(" "); // Split line into language and number
        String language = parts[0];
        String number = parts[1];

        // Print language left-aligned (15 spaces) and number right-aligned with leading zeros (3 digits)
        System.out.printf("%-15s%03d\n", language, Integer.parseInt(number));
    }
    
    // Main method:
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Reading three lines of input
        String line1 = scanner.nextLine();
        String line2 = scanner.nextLine();
        String line3 = scanner.nextLine();

        // Print the correct output:
        printDiv();
        printFormatted(line1);
        printFormatted(line2);
        printFormatted(line3);
        printDiv();
    }
}
