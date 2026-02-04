#
# @lc app=leetcode id=3398 lang=cpp
#
# [3398] Smallest Substring With Identical Characters I
#

# @lc code=start
class Solution {
public:
    int minLength(string s, int numOps) {
        int n = s.size();
        if (numOps >= n) return 1; // Can flip all to same character
        int result = n; // Start with maximum possible length
        int left = 0;
        int maxIdentical = 0;
        vector<int> count(2, 0); // Counts for '0' and '1'
        
        for (int right = 0; right < n; ++right) {
            ++count[s[right] - '0'];
            maxIdentical = max(maxIdentical, count[s[right] - '0']);
            
            while ((right - left + 1) - maxIdentical > numOps) { // Too many flips needed
                --count[s[left] - '0'];
                ++left;
                maxIdentical = max(count[0], count[1]); // Update maxIdentical after shrinking
            }
            
            result = min(result, right - left + 1); // Minimize longest segment after adjustments
        }
        return result;
    }
};
# @lc code=end