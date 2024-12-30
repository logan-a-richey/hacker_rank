// hacker rank problem

#include <iostream>
#include <map>

void print_number_description(int x) {
    std::map<int, std::string> num_map = {
       {0, "zero"},
       {1, "one"},
       {2, "two"},
       {3, "three"},
       {4, "four"},
       {5, "five"},
       {6, "six"},
       {7, "seven"},
       {8, "eight"},
       {9, "nine"}
    };
    
    if (x >= 1 && x <= 9) {
        std::cout << num_map[x] << std::endl;
    } else if (x > 9 && x % 2 == 0) {
        std::cout << "even" << std::endl;
    } else if (x > 9) {
        std::cout << "odd" << std::endl;
    }
}

int main() {
    int a, b;
    //std::cin >> a >> b;
    a = 2;
    b = 13;

    // Process each number in the range [a, b]
    for (int i = a; i <= b; i++) {
        print_number_description(i);
    }
    
    return 0;
}

