#
# @lc app=leetcode id=3399 lang=cpp
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
class Solution {
public:
    int minLength(string s, int numOps) {
        int n = s.size();
        int maxSeq = n; // Initialize with total length as maximum possible sequence
        // Edge cases
        if (numOps >= n) return 1; // If more or equal ops than length, we can make all characters different
        
        // Two pointers for sliding window approach
        int left = 0, right = 0;
        vector<int> counts(2, 0); // counts[0] for '0', counts[1] for '1' within current window
        while (right < n) {
            counts[s[right] - '0']++; // Increase count for current character
            while (min(counts[0], counts[1]) > numOps) { // More operations needed than allowed, slide left pointer
                counts[s[left] - '0']--; // Decrease count for left character as it slides out of window
                left++; 
            }
            maxSeq = min(maxSeq, right - left + 1); // Update max possible sequence based on current valid window size
            right++; 
        } 
        return maxSeq; 
    } 
}; 
# @lc code=end