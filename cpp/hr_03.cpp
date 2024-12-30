// hr_03.cpp

/*
2 2         // 2 lists, 2 queries
3 1 5 4     // list 1
5 1 2 8 9 3 // list 2
0 1         // query 1
1 3         // query 2

5           // m[0][1] 
9           // m[1][3]
*/

#include <iostream>
#include <vector>
//using namespace std;

int main() {
    int n, q, j, k;
    std::cin >> n >> q;
    
    // init 2D vector for storing lists
    std::vector<std::vector<int>> m;
    
    // Read the n lists
    for (int i = 0; i < n; i++) {
        int k;  // elements in this list
        std::cin >> k;
        
        vector<int> list;  // create a list for the current row
        for (int j = 0; j < k; j++) {
            int num;
            std::cin >> num;
            list.push_back(num);
        }
        
        // push the current list into the 2D vector
        m.push_back(list);
    }
    
    // Loop through queries
    for (int i = 0; i < q; i++) {
        std::cin >> j >> k;  // Read the query indices
        
        // Output the value at m[j][k]
        std::cout << m[i][j] << std::endl;
    }
    
    return 0;
}

