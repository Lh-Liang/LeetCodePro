#
# @lc app=leetcode id=3646 lang=cpp
#
# [3646] Next Special Palindrome Number
#
# @lc code=start
class Solution {
public:
    long long specialPalindrome(long long n) {
        n++; // Start checking from the next number
        while (true) {
            if (isPalindrome(n) && hasSpecialDigitCounts(n)) {
                return n;
            }
            n++;
        }
    }
    
    bool isPalindrome(long long num) {
        std::string s = std::to_string(num);
        int len = s.size();
        for (int i = 0; i < len / 2; ++i) {
            if (s[i] != s[len - 1 - i]) return false;
        }
        return true;
    }
    
    bool hasSpecialDigitCounts(long long num) {
        std::unordered_map<int, int> count; // Stores count of each digit
        while (num > 0) {
            int digit = num % 10;
            count[digit]++;
            num /= 10;
        } 
        for (const auto& [digit, c] : count) {
            if (digit != c) return false; // Digit must appear exactly as many times as its value. 
        } 
        return true; 
    } 
};  # @lc code=end