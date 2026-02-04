#
# @lc app=leetcode id=3779 lang=cpp
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#
# @lc code=start
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int ops = 0;
        while (!nums.empty()) {
            // Check if all elements are distinct
            unordered_set<int> s(nums.begin(), nums.end());
            if (s.size() == nums.size()) break;
            // Remove first three elements or all if less than three
            int rem = min(3, (int)nums.size());
            nums.erase(nums.begin(), nums.begin() + rem);
            ++ops;
        }
        return ops;
    }
};
# @lc code=end