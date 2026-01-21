#
# @lc app=leetcode id=3646 lang=cpp
#
# [3646] Next Special Palindrome Number
#
# @lc code=start
class Solution {
public:
    long long specialPalindrome(long long n) {
        vector<long long> candidates;
        
        // Generate all valid subsets of digits {1,2,...,9}
        for (int mask = 1; mask < (1 << 9); mask++) {
            vector<int> digits;
            int totalLen = 0;
            int oddCount = 0;
            
            for (int d = 1; d <= 9; d++) {
                if (mask & (1 << (d - 1))) {
                    digits.push_back(d);
                    totalLen += d;
                    if (d % 2 == 1) oddCount++;
                }
            }
            
            // Skip if more than one odd-count digit (can't form palindrome)
            if (oddCount > 1) continue;
            
            // Skip if total length too long
            if (totalLen > 20) continue;
            
            // Build the smallest palindrome for this subset
            long long palindrome = buildPalindrome(digits, totalLen);
            candidates.push_back(palindrome);
        }
        
        // Find the smallest candidate greater than n
        long long result = LLONG_MAX;
        for (long long cand : candidates) {
            if (cand > n && cand < result) {
                result = cand;
            }
        }
        
        return result;
    }
    
private:
    long long buildPalindrome(const vector<int>& digits, int totalLen) {
        bool isOddLen = (totalLen % 2 == 1);
        int oddDigit = -1;
        
        if (isOddLen) {
            for (int d : digits) {
                if (d % 2 == 1) {
                    oddDigit = d;
                    break;
                }
            }
        }
        
        vector<int> firstHalfDigits;
        for (int d : digits) {
            int count = d;
            if (d == oddDigit) {
                count--;
            }
            for (int i = 0; i < count / 2; i++) {
                firstHalfDigits.push_back(d);
            }
        }
        
        sort(firstHalfDigits.begin(), firstHalfDigits.end());
        
        string s = "";
        for (int d : firstHalfDigits) {
            s += to_string(d);
        }
        
        if (isOddLen) {
            s += to_string(oddDigit);
        }
        
        for (int i = firstHalfDigits.size() - 1; i >= 0; i--) {
            s += to_string(firstHalfDigits[i]);
        }
        
        return stoll(s);
    }
};
# @lc code=end