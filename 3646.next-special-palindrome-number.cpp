#
# @lc app=leetcode id=3646 lang=cpp
#
# [3646] Next Special Palindrome Number
#
# @lc code=start
class Solution {
public:
    long long specialPalindrome(long long n) {
        vector<long long> allPalindromes;
        
        vector<int> evens = {2, 4, 6, 8};
        vector<int> odds = {1, 3, 5, 7, 9};
        
        // Case 1: Only evens (non-empty)
        for (int evenMask = 1; evenMask < 16; evenMask++) {
            vector<int> counts(10, 0);
            for (int i = 0; i < 4; i++) {
                if (evenMask & (1 << i)) {
                    counts[evens[i]] = evens[i];
                }
            }
            generatePalindromes(counts, allPalindromes);
        }
        
        // Case 2: Zero or more evens + exactly one odd
        for (int evenMask = 0; evenMask < 16; evenMask++) {
            for (int odd : odds) {
                vector<int> counts(10, 0);
                for (int i = 0; i < 4; i++) {
                    if (evenMask & (1 << i)) {
                        counts[evens[i]] = evens[i];
                    }
                }
                counts[odd] = odd;
                generatePalindromes(counts, allPalindromes);
            }
        }
        
        sort(allPalindromes.begin(), allPalindromes.end());
        
        for (long long p : allPalindromes) {
            if (p > n) return p;
        }
        
        return -1;
    }
    
    void generatePalindromes(vector<int>& counts, vector<long long>& result) {
        int total = 0;
        int oddDigit = -1;
        for (int d = 0; d < 10; d++) {
            total += counts[d];
            if (counts[d] % 2 == 1) {
                oddDigit = d;
            }
        }
        
        if (total == 0) return;
        
        bool isOdd = (total % 2 == 1);
        
        string half;
        for (int d = 0; d < 10; d++) {
            int halfCnt = counts[d] / 2;
            for (int i = 0; i < halfCnt; i++) {
                half += ('0' + d);
            }
        }
        
        if (half.empty()) {
            if (isOdd && oddDigit >= 0) {
                result.push_back(oddDigit);
            }
            return;
        }
        
        sort(half.begin(), half.end());
        
        do {
            if (half[0] == '0') continue;
            
            string palindrome = half;
            if (isOdd) {
                palindrome += ('0' + oddDigit);
            }
            string revHalf = half;
            reverse(revHalf.begin(), revHalf.end());
            palindrome += revHalf;
            
            if (palindrome.length() <= 18) {
                long long num = stoll(palindrome);
                result.push_back(num);
            }
            
        } while (next_permutation(half.begin(), half.end()));
    }
};
# @lc code=end