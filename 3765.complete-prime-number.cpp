#
# @lc app=leetcode id=3765 lang=cpp
#
# [3765] Complete Prime Number
#
# @lc code=start
class Solution {
public:
    bool completePrime(int num) {
        // Helper function to check if a number is prime
        auto isPrime = [](int x) {
            if (x <= 1) return false;
            if (x == 2) return true; // 2 is the only even prime number
            if (x % 2 == 0) return false;
            for (int i = 3; i * i <= x; i += 2) {
                if (x % i == 0) return false;
            }
            return true;
        };
        
        std::string s = std::to_string(num);
        int len = s.length();
        std::unordered_set<int> checkedNumbers; // Track checked numbers to avoid redundancy
        
        // Check all prefixes for primality
        for (int i = 1; i <= len; ++i) {
            int prefix = std::stoi(s.substr(0, i));
            if (checkedNumbers.find(prefix) == checkedNumbers.end()) { // Check only if not already verified
                if (!isPrime(prefix)) return false;
                checkedNumbers.insert(prefix); // Mark as checked
            }
        }
        
        // Check all suffixes for primality
        for (int i = 0; i < len; ++i) {
            int suffix = std::stoi(s.substr(i));
            if (checkedNumbers.find(suffix) == checkedNumbers.end()) { // Check only if not already verified
                if (!isPrime(suffix)) return false;
                checkedNumbers.insert(suffix); // Mark as checked
            }
        }
        
        return true; // All checks passed, it's a Complete Prime Number.
    } 
}; 
# @lc code=end