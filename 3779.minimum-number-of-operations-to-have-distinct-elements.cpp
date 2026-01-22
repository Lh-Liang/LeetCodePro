#
# @lc app=leetcode id=3779 lang=cpp
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#
# @lc code=start
class Solution {
public:
    int minOperations(vector<int>& nums) {
        unordered_set<int> seen;
        int maxSecondLast = -1;
        
        // Scan from right to left
        for (int i = nums.size() - 1; i >= 0; i--) {
            if (seen.count(nums[i])) {
                // This is a non-last occurrence, must be removed
                maxSecondLast = max(maxSecondLast, i);
            } else {
                seen.insert(nums[i]);
            }
        }
        
        // If no duplicates found, no operations needed
        if (maxSecondLast == -1) {
            return 0;
        }
        
        // We need to remove indices 0 to maxSecondLast
        // Each operation removes 3 elements, so we need ceil((maxSecondLast+1)/3)
        return maxSecondLast / 3 + 1;
    }
};
# @lc code=end