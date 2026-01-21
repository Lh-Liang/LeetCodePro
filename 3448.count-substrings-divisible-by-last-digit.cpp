#
# @lc app=leetcode id=3448 lang=cpp
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution {
public:
    long long countSubstrings(string s) {
        int n = s.length();
        long long ans = 0;
        
        // For divisibility by 3, 6 (uses mod 3), and 9
        vector<int> cnt3(3, 0), cnt9(9, 0);
        cnt3[0] = 1; // prefix[-1] = 0
        cnt9[0] = 1;
        int prefixSum = 0;
        
        // For divisibility by 7
        vector<int> cnt7(7, 0);
        
        for (int j = 0; j < n; j++) {
            int d = s[j] - '0';
            
            // Update cnt7: transform values for new ending position
            vector<int> newCnt7(7, 0);
            for (int r = 0; r < 7; r++) {
                newCnt7[(10 * r + d) % 7] += cnt7[r];
            }
            newCnt7[d % 7]++; // add current position as new starting point
            cnt7 = newCnt7;
            
            // Update prefix sum
            prefixSum += d;
            
            if (d == 0) {
                // Skip substrings ending with 0
            } else if (d == 1 || d == 2 || d == 5) {
                // All substrings ending with 1, 2, or 5 are divisible
                ans += j + 1;
            } else if (d == 4) {
                // Divisible by 4 depends on last 2 digits
                ans += 1; // single digit
                if (j >= 1 && (s[j-1] - '0') % 2 == 0) {
                    ans += j; // all substrings of length >= 2
                }
            } else if (d == 8) {
                // Divisible by 8 depends on last 3 digits
                ans += 1; // single digit
                if (j >= 1 && ((s[j-1] - '0') * 10 + 8) % 8 == 0) {
                    ans += 1; // 2-digit substring
                }
                if (j >= 2 && ((s[j-2] - '0') * 100 + (s[j-1] - '0') * 10 + 8) % 8 == 0) {
                    ans += j - 1; // 3+ digit substrings
                }
            } else if (d == 3 || d == 6) {
                // Divisible by 3 (for d=6, already divisible by 2)
                ans += cnt3[prefixSum % 3];
            } else if (d == 9) {
                // Divisible by 9
                ans += cnt9[prefixSum % 9];
            } else if (d == 7) {
                // Divisible by 7
                ans += cnt7[0];
            }
            
            // Update cnt3 and cnt9 for future queries
            cnt3[prefixSum % 3]++;
            cnt9[prefixSum % 9]++;
        }
        
        return ans;
    }
};
# @lc code=end