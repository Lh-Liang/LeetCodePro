#
# @lc app=leetcode id=3765 lang=cpp
#
# [3765] Complete Prime Number
#
# @lc code=start
class Solution {
public:
    bool completePrime(int num) {
        auto isPrime = [](int n) {
            if (n < 2) return false;
            for (int i = 2; i * i <= n; ++i) {
                if (n % i == 0) return false;
            }
            return true;
        };
        std::string s = std::to_string(num);
        int len = s.length();
        for (int i = 1; i <= len; ++i) {
            int prefix = std::stoi(s.substr(0, i));
            int suffix = std::stoi(s.substr(len - i));
            if (!isPrime(prefix) || !isPrime(suffix)) return false;
        }
        return true;
    }
};
# @lc code=end