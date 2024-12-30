// hacker rank problem

#include <iostream>
#include <vector>

using namespace std;

void print_number_description(int x) {
    vector<string> num_names = {
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    };
    
    if (x >= 1 && x <= 9) {
        cout << num_names.at(x) << endl;
    } else if (x > 9 && x % 2 == 0) {
        cout << "even" << endl;
    } else if (x > 9) {
        cout << "odd" << endl;
    }
}

int main() {
    int a, b;
    cin >> a >> b;

    // Process each number in the range [a, b]
    for (int i = a; i <= b; i++) {
        print_number_description(i);
    }
    
    return 0;
}

