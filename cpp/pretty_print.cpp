#include <iostream>
#include <iomanip> 

int main() {
    int T;
    std::cin >> T;

    // Set common formatting flags
    std::cout << std::setiosflags(std::ios::uppercase) 
              << std::setw(0xf) << std::internal;

    while (T--) {
        double A, B, C;
        std::cin >> A >> B >> C;

        // Output A in hexadecimal format, left-aligned, with base prefix
        std::cout << std::hex << std::left << std::showbase << std::nouppercase;
        std::cout << static_cast<long long>(A) << std::endl;

        // Output B in decimal, right-aligned, with precision and padding
        std::cout << std::dec << std::right << std::setw(15) 
                  << std::setfill('_') << std::showpos 
                  << std::fixed << std::setprecision(2);
        std::cout << B << std::endl;

        // Output C in scientific notation, uppercase, with precision
        std::cout << std::scientific << std::uppercase 
                  << std::noshowpos << std::setprecision(9);
        std::cout << C << std::endl;
    }

    return 0;
}

