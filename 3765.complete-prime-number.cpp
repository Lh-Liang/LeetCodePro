#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    bool isPrime(int n) {
        if (n < 2) return false;
        if (n % 2 == 0) return n == 2;
        if (n % 3 == 0) return n == 3;
        for (long long i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }

    bool completePrime(int num) {
        string s = to_string(num);
        int n = (int)s.size();

        for (int k = 1; k <= n; k++) {
            int prefix = stoi(s.substr(0, k));
            int suffix = stoi(s.substr(n - k, k));
            if (!isPrime(prefix) || !isPrime(suffix)) return false;
        }
        return true;
    }
};
// @lc code=end
