#include <iostream>
#include <set>

/*
Sample Input
8
1 9
1 6
1 10
1 4
3 6
3 14
2 6
3 6

Sample Output
Yes
No
No
*/


int main() {
    int Q;
    std::cin >> Q;
    std::set<int> s;

    for (int i = 0; i < Q; i++) {
        int x, y;
        std::cin >> x >> y;

        if (x == 1) {
            // Insert the value into the set
            s.insert(y);
        } else if (x == 2) {
            // Erase the value from the set
            s.erase(y);
        } else if (x == 3) {
            // Check if the value exists in the set
            std::set<int>::iterator it = s.find(y);
            if (it != s.end()) {
                std::cout << "Yes" << std::endl;
            } else {
                std::cout << "No" << std::endl;
            }
        }
    }

    return 0;
}

