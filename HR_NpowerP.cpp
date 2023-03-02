#include <iostream>
#include <cmath>
#include <stdexcept>

using namespace std;

int power(int n, int p) {
    if (n < 0 || p < 0) {
        throw invalid_argument("n and p should be non-negative");
    }
    
    return pow(n, p);
}

int main() {
    int t;
    cin >> t;
    
    for (int i = 0; i < t; i++) {
        int n, p;
        cin >> n >> p;
        
        try {
            int ans = power(n, p);
            cout << ans << endl;
        } catch (invalid_argument& e) {
            cout << e.what() << endl;
        }
    }
    
    return 0;
}
# this one too popping compilation error 
#Solution.cpp:19:5: error: ‘Calculator’ was not declared in this scope
#     Calculator myCalculator=Calculator();
#     ^~~~~~~~~~
#Solution.cpp:25:24: error: ‘myCalculator’ was not declared in this scope
#                int ans=myCalculator.power(n,p);
