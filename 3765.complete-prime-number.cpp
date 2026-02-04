#
# @lc app=leetcode id=3765 lang=cpp
#
# [3765] Complete Prime Number
#

# @lc code=start
class Solution {
public:
    bool isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }
    bool completePrime(int num) {
        std::string s = std::to_string(num);
        int len = s.length();
        for (int i = 1; i <= len; ++i) {
            int prefix = std::stoi(s.substr(0, i));
            int suffix = std::stoi(s.substr(len - i));
            if (!isPrime(prefix) || !isPrime(suffix)) {
                return false;
            }
        }
        return true;
    }
}; 
# @lc code=end