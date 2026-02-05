#
# @lc app=leetcode id=3765 lang=cpp
#
# [3765] Complete Prime Number
#
# @lc code=start
class Solution {
public:
    bool isPrime(int n) {
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        for (int i = 3; i * 1LL * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
    bool completePrime(int num) {
        std::string s = std::to_string(num);
        int n = s.size();
        // Check all prefixes
        for (int i = 1; i <= n; ++i) {
            int prefix = std::stoi(s.substr(0, i));
            if (!isPrime(prefix))
                return false;
        }
        // Check all suffixes
        for (int i = 0; i < n; ++i) {
            int suffix = std::stoi(s.substr(i));
            if (!isPrime(suffix))
                return false;
        }
        return true;
    }
};
# @lc code=end