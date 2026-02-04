#
# @lc app=leetcode id=3677 lang=cpp
#
# [3677] Count Binary Palindromic Numbers
#

# @lc code=start
#include <cmath>
#include <string>
#include <bitset>
#include <sstream>

class Solution {
public:
    int countBinaryPalindromes(long long n) {
        int count = 0;
        int maxBits = std::floor(std::log2(n)) + 1; // Calculate maximum bits needed for n
        for (int len = 1; len <= maxBits; ++len) { // Length of binary palindrome halves
            long long maxHalf = 1LL << ((len + 1) / 2);
            for (long long half = 0; half < maxHalf; ++half) {
                std::stringstream ss;
                ss << std::bitset<64>(half).to_string();
                std::string halfStr = ss.str();
                halfStr.erase(0, halfStr.find_first_not_of('0'));
                if (halfStr.empty()) halfStr = "0";
                
                // Mirror the half string to create full palindrome
                std::string fullPalindrome = halfStr + std::string(halfStr.rbegin() + (len % 2), halfStr.rend());
                long long palindromeNum = std::stoll(fullPalindrome, nullptr, 2);
                if (palindromeNum > n) continue; // Continue instead of return to check all possible lengths
                ++count;
            }
        }
        return count;
    }
};
# @lc code=end