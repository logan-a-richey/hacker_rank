#include <vector>
#include <iostream>
#include <algorithm>

int main() {
    // first line of input
    int n;
    std::cin >> n;
    
    // second line of input
    std::vector<int> vec;
    for (int i = 0; i < n; i++) {
        int val;
        std::cin >> val;
        vec.push_back(val);
    }
    
    // sort the vector
    std::sort(vec.begin(), vec.end());
    
    // output the result
    for (int num : vec) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    return 0;
}

