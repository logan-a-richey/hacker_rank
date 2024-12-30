/*******************************************************************************
HackerRank - Java Tutorial
java-stdin-and-stdout-1.java
*******************************************************************************/

/*
TASK:
Read in 3 lines of data consisting of a single integer.
Print those integers of data on separate lines.
*/

import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();
        
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
    }
}
