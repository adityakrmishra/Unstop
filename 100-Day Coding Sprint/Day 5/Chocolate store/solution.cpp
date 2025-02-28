#include <bits/stdc++.h>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int Q;
    cin >> Q; 
    unordered_map<string, int> chocolateStock; 

    while (Q--) {
        int queryType;
        string chocolateType;
        int quantity;
        cin >> queryType >> chocolateType >> quantity;

        if (queryType == 1) {
            chocolateStock[chocolateType] += quantity;
        } else if (queryType == 2) {
            int available = chocolateStock[chocolateType];
            if (available >= quantity) {
                cout << quantity << endl;
                chocolateStock[chocolateType] -= quantity;
            } else {
                cout << available << endl;
                chocolateStock[chocolateType] = 0;
            }
        }
    }

    return 0;
}
