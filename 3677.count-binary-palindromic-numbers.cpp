#
# @lc app=leetcode id=3677 lang=cpp
#
# [3677] Count Binary Palindromic Numbers
#
# @lc code=start
class Solution {
public:
    int countBinaryPalindromes(long long n) {
        int count = 0;
        for (long long i = 0; i <= n; ++i) {
            std::string bin = std::bitset<64>(i).to_string();
            bin.erase(0, bin.find_first_not_of('0')); // Remove leading zeros
            std::string rev_bin = bin;
            std::reverse(rev_bin.begin(), rev_bin.end());
            if (bin == rev_bin) {
                ++count;
            }
        }
        return count;
    }
};
# @lc code=end