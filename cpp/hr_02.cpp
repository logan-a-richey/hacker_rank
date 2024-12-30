#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/*
INPUT:
4
1 3 2 4

OUTPUT:
4 2 3 1
*/

int main() {
    int n;
    cin >> n;
    vector<int> num_vec;

    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        num_vec.push_back(num);
    }  
    
    reverse(num_vec.begin(), num_vec.end());

    for (int num : num_vec) {
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}

