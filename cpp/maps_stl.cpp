#include <iostream>
#include <map>

int main() {
    int q;
    std::cin >> q;

    std::map<std::string, int> mp;  // Map to store name -> marks

    for (int i = 0; i < q; i++) {
        int type;
        std::cin >> type;

        if (type == 1) {
            std::string name;
            int marks;
            std::cin >> name >> marks;
            mp[name] += marks;
        } else if (type == 2) {
            std::string name;
            std::cin >> name;
            mp.erase(name);
        } else if (type == 3) {
            std::string name;
            std::cin >> name;

            std::cout << mp[name] << std::endl;
        }
    }

    return 0;
}

