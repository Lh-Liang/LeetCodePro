#
# @lc app=leetcode id=3721 lang=cpp
#
# [3721] Longest Balanced Subarray II
#

# @lc code=start
class Solution {
public:
    int longestBalanced(vector<int>& nums) {
        unordered_map<int, int> difference_index;
        difference_index[0] = -1; // initial condition for zero difference
        int maxLength = 0, evenCount = 0, oddCount = 0;
        
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] % 2 == 0) {
                evenCount++; // increment if even number
            } else {
                oddCount++; // increment if odd number
            }
            int diff = evenCount - oddCount; // calculate current difference
            
            if (difference_index.find(diff) != difference_index.end()) {
                maxLength = max(maxLength, i - difference_index[diff]); // calculate max length from previous occurrence of same diff
            } else {
                difference_index[diff] = i; // store first occurrence of this diff in map
            }
        }
        return maxLength; // return the maximum length found
    }
};
# @lc code=end