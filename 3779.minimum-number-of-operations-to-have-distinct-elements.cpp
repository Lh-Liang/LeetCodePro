#
# @lc app=leetcode id=3779 lang=cpp
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#
# @lc code=start
class Solution {
public:
    int minOperations(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        if (numSet.size() == nums.size()) return 0; // Already unique
        int ops = 0;
        while (nums.size() > numSet.size()) {
            ops++;
            nums.erase(nums.begin(), nums.begin() + min(3, (int)nums.size())); // Remove first three or less if size < 3
            numSet = unordered_set<int>(nums.begin(), nums.end()); // Update set with current nums
        }
        return ops;
    }
};
# @lc code=end