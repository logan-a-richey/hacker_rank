#include <vector>
#include <iostream>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> v;
    for (int i = 0; i < n; i++) {
        int val;
        std::cin >> val;
        v.push_back(val);
    }

    // q1: remove element at position 'x'
    int x;
    std::cin >> x;
    v.erase(v.begin() + x - 1);

    // q2: remove elements in the range [a, b)
    int a, b;
    std::cin >> a >> b;
    v.erase(v.begin() + a - 1, v.begin() + b - 1);

    // output line 1: Size of the remaining vector
    std::cout << v.size() << std::endl;

    // output line 2: Elements of the vector
    for (int i = 0; i < v.size(); i++) {
        std::cout << v[i];
        if (i != v.size() - 1) {
            std::cout << " ";
        }
    }
    std::cout << std::endl;

    return 0;
}

