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
        if (n == 0) return 1;
        
        // Function to generate palindrome from half and return its value
        auto generate_palindrome = [](long long half, bool odd_length) -> long long {
            std::string half_str = std::bitset<50>(half).to_string();
            half_str.erase(0, half_str.find_first_not_of('0'));
            std::string reversed_half = half_str;
            std::reverse(reversed_half.begin(), reversed_half.end());
            if (odd_length) half_str.pop_back();
            
            std::string full_palindrome = half_str + reversed_half;
            return std::stoll(full_palindrome, nullptr, 2);
        };
        
        // Generate palindromes by mirroring halves
        for (int length = 1; ; ++length) {
            long long start = (1LL << ((length - 1) / 2));
            long long end = (1LL << ((length + 1) / 2));
            for (long long i = start; i < end; ++i) {
                long long palindrome = generate_palindrome(i, length % 2);
                if (palindrome > n) return count;
                ++count;
            }
        }
    }
};
# @lc code=end