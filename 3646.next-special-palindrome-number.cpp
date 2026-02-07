#
# @lc app=leetcode id=3646 lang=cpp
#
# [3646] Next Special Palindrome Number
#

# @lc code=start
class Solution {
public:
    long long specialPalindrome(long long n) {
        auto is_special = [](long long num) {
            string s = to_string(num);
            if (!equal(s.begin(), s.begin() + s.size() / 2, s.rbegin())) return false;
            map<char, int> count;
            for (char c : s) count[c]++;
            for (auto &[digit, cnt] : count) {
                if (cnt != digit - '0') return false;
            }
            return true;
        };
        n++;  // Start checking from n+1.
        while (true) {
            if (is_special(n)) return n;
            n++;  // Increment to find next candidate.
        }
    }
};
# @lc code=end