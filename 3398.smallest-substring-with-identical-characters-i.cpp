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
        vector<int> count(2, 0); // count[0] for '0's, count[1] for '1's
        int l = 0, maxFreq = 0;
        // Sliding window approach
        for (int r = 0; r < n; ++r) {
            count[s[r] - '0']++; 
            maxFreq = max(maxFreq, count[s[r] - '0']);
            if (r - l + 1 - maxFreq > numOps) {
                count[s[l] - '0']--;
                l++; 
            }
        }
        return n - l; 
    }
}; 
# @lc code=end