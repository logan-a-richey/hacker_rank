/*******************************************************************************
HackerRank - Java Tutorial
java_loops_2.java
*******************************************************************************/

/*
TASK:

We use the integers a,b,n to create the following series:
{
    (a + 2**0 * b),
    (a + 2**0 * b + 2**1 * b),
    ... 
    (a + 2**0 * b + 2**1 * b + ... + 2**(n-1) * b)
}

We are given t tasks in the form of a,b,n.
For each task, print the series as a single line of n space-separated integers.

INPUT 1
2
0 2 10
5 3 5

OUTPUT 1:
2 6 14 30 62 126 254 510 1022 2046
8 14 26 50 98
*/

import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int i = 0; i < t; i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            
            // build and print output line:
            int res = a;
            StringBuilder output = new StringBuilder();
            for (int j=0; j<n; j++){
                res += (int)(Math.pow(2, j) * b);
                output.append(res).append(" ");
            }
            System.out.println(output.toString().trim());
        }
        // loop until all lines have been printed
        
        in.close();
    }
}

