#
# @lc app=leetcode id=3779 lang=cpp
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#

# @lc code=start
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int operations = 0;
        while (nums.size() > 0) {
            unordered_set<int> seen;
            bool allDistinct = true;
            for (int num : nums) {
                if (seen.count(num)) {
                    allDistinct = false;
                    break;
                }
                seen.insert(num);
            }
            if (allDistinct) break; // Stop if all elements are distinct
            nums.erase(nums.begin(), nums.begin() + min(3, static_cast<int>(nums.size())));
            ++operations; // Increment operation count
        }
        return operations;
    }
};
# @lc code=end